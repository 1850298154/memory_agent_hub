# Claude Code 任务完成邮件通知 — 完整配置指南

## 功能效果

每当 Claude Code 完成任务（Stop 事件），自动发送邮件通知：

```
标题: [项目名] 帮我写一个hello world函数
正文:
  项目: KAG

  用户问题:
  帮我写一个hello world函数

  助手回答:
  ```python
  print("Hello, World!")
  ```
```

- 自动提取**最后的用户问题**和**最后的助手回答**
- 支持**排除指定项目**（如隐私项目不发邮件）
- **跨项目通用**：全局配置 + 项目级配置双重保障
- 已踩过的坑全部记录在案，避免重蹈覆辙

---

## 踩坑记录（必读）

### 坑 1：Windows 下 `shell: "bash"` 导致 Hook 全部失败

**现象**：Hook 报错 `ENOENT: no such file or directory, uv_spawn 'C:\zss\important-software\Git\bin'`

**原因**：Claude Code 在 Windows 上查找 bash 时，把 `Git\bin` **目录**当成了 bash **可执行文件**，导致 uv_spawn 失败。**所有使用 `shell: "bash"` 的 Hook 在此环境下全部静默失败。**

**解决**：使用 `"shell": "powershell"`，这是 Windows 上唯一可靠的方式。

### 坑 2：Stop Hook 的 stdin 为空

**现象**：Stop Hook 触发了，但 stdin 读不到 JSON 数据。

**原因**：Hook 事件确实会传 stdin JSON（含 `session_id`, `transcript_path`, `cwd` 等），但当 bash shell 启动失败时，stdin 数据丢失。

**解决**：使用 PowerShell 后 stdin 正常传递。同时脚本做回退处理：先读 stdin，没有则根据 `os.getcwd()` 推算会话文件路径。

### 坑 3：UserPromptSubmit Hook 不触发

**现象**：配置了 `UserPromptSubmit` Hook 但从未触发。

**原因**：同坑 1，bash shell 启动失败导致所有 Hook 静默失败。

**解决**：统一使用 `"shell": "powershell"`。

### 坑 4：提取到倒数第二条用户问题，不是最后一条

**现象**：邮件中显示的问题不是当前问的，而是更早的问题。

**原因**：从 JSONL 末尾反向遍历时，最后一条 `type=user` 可能包含 `tool_result`（工具执行结果），脚本跳过 tool_result 后拿到了倒数第二条。

**解决**：反向遍历，找到第一个 `type=user` 且 content 中**不含 tool_result** 的条目，就是真正的最后用户问题。

### 坑 5：JSONL 文件未刷盘导致读到旧数据

**现象**：Hook 触发后提取的内容缺少最新一轮对话。

**原因**：Stop Hook 触发时，JSONL 文件可能还未完全写入磁盘。

**解决**：脚本中加入 `time.sleep(2)` 等待文件刷盘。

---

## 一键配置步骤

### 第 1 步：获取邮箱授权码

以 163 邮箱为例：

1. 登录 163 邮箱网页版 → **设置** → **POP3/SMTP/IMAP**
2. 开启 **SMTP 服务**
3. 点击 **生成客户端授权码**，复制保存

> 授权码 ≠ 登录密码，必须使用授权码。其他邮箱同理。

### 第 2 步：创建脚本目录

```bash
mkdir -p ~/.claude/scripts
```

### 第 3 步：创建邮件通知脚本

将以下内容保存为 `~/.claude/scripts/notify_email.py`：

```python
"""Claude Code 任务完成邮件通知脚本（全局 Hook 用）

读取 Hook stdin JSON（含 session_id, transcript_path, cwd 等），
从会话 JSONL 文件提取用户问题和助手回答，发送邮件通知。

邮件格式：
  标题: [项目名] 用户问题（前50字）
  正文: 项目名 + 用户问题 + 助手回答摘要
"""
import smtplib, ssl, json, sys, os
from email.mime.text import MIMEText
from pathlib import Path

# ========== 邮箱配置（必须修改）==========
SMTP_SERVER = "smtp.163.com"       # SMTP 服务器
SMTP_PORT = 465                     # SMTP 端口（SSL）
USER = "你的邮箱@163.com"           # 发件邮箱（也是收件邮箱）
PASSWORD = "你的授权码"              # 客户端授权码（非登录密码）

# ========== 排除项目（可选修改）==========
SKIP_PROJECTS = {"noval"}


def send(subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = USER
    msg["Subject"] = subject
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as s:
        s.login(USER, PASSWORD)
        s.sendmail(USER, [USER], msg.as_string())


def extract_from_transcript(transcript_path):
    """从 JSONL 末尾往前找：最后一条用户纯文本问题 + 最后一条助手文本回答"""
    user_query = ""
    assistant_answer = ""

    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return user_query, assistant_answer

    for line in reversed(lines):
        try:
            entry = json.loads(line)
            t = entry.get("type", "")

            # 找最后一条用户纯文本问题（跳过 tool_result）
            if t == "user" and not user_query:
                msg = entry.get("message", {})
                content = msg.get("content", "")
                if isinstance(content, str) and content.strip():
                    user_query = content.strip()[:500]
                elif isinstance(content, list):
                    has_tool_result = any(
                        isinstance(item, dict) and item.get("type") == "tool_result"
                        for item in content
                    )
                    if not has_tool_result:
                        texts = []
                        for item in content:
                            if isinstance(item, dict) and item.get("type") == "text":
                                txt = item.get("text", "").strip()
                                if txt:
                                    texts.append(txt)
                        if texts:
                            user_query = " ".join(texts)[:500]

            # 找最后一条助手文本回答
            elif t == "assistant" and not assistant_answer:
                msg = entry.get("message", {})
                content = msg.get("content", [])
                if isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "text":
                            txt = item.get("text", "").strip()
                            if txt:
                                assistant_answer = txt[:800]
                                break
                elif isinstance(content, str) and content.strip():
                    assistant_answer = content.strip()[:800]

            if user_query and assistant_answer:
                break
        except Exception:
            continue

    return user_query, assistant_answer


if __name__ == "__main__":
    # 1. 从 stdin 读取 Hook 输入
    hook_input = {}
    raw_stdin = ""
    if not sys.stdin.isatty():
        raw_stdin = sys.stdin.read()
        if raw_stdin:
            try:
                hook_input = json.loads(raw_stdin)
            except Exception:
                pass

    # 2. 获取项目路径和名称
    cwd = hook_input.get("cwd", "") or hook_input.get("project_path", "") or os.getcwd()
    project_name = Path(cwd).name if cwd else "unknown"

    # 3. 排除项目
    if project_name.lower() in SKIP_PROJECTS:
        print(f"已跳过: {project_name} 在排除列表中")
        sys.exit(0)

    # 4. 获取 transcript 路径
    transcript_path = hook_input.get("transcript_path", "")
    if not transcript_path:
        # 回退：根据 cwd 手动定位会话文件
        # Claude Code 项目目录命名规则：路径中的 / \ : _ 全部替换为 -
        project_dir = cwd.replace("/", "-").replace("\\", "-").replace(":", "-").replace("_", "-")
        sessions_dir = Path.home() / ".claude" / "projects" / project_dir
        session_id = hook_input.get("session_id", "")
        if session_id:
            candidate = sessions_dir / f"{session_id}.jsonl"
            if candidate.exists():
                transcript_path = str(candidate)
        if not transcript_path:
            # 找最新的 jsonl 文件
            jsonl_files = sorted(sessions_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True)
            if jsonl_files:
                transcript_path = str(jsonl_files[0])

    # 5. 提取用户问题和助手回答（等待文件刷盘）
    import time
    time.sleep(2)
    user_query, assistant_answer = extract_from_transcript(transcript_path)

    # 6. 构建邮件
    if user_query:
        subject = f"[{project_name}] {user_query[:50]}"
    else:
        default_subject = sys.argv[1] if len(sys.argv) > 1 else "Claude Code 任务完成"
        subject = f"[{project_name}] {default_subject}"

    body_parts = [f"项目: {project_name}"]
    if user_query:
        body_parts.append(f"\n用户问题:\n{user_query}")
    if assistant_answer:
        body_parts.append(f"\n助手回答:\n{assistant_answer}")

    send(subject, "\n".join(body_parts))
    print(f"邮件已发送: {subject}")
```

**必须修改脚本顶部的 3 个配置项**：`SMTP_SERVER`、`USER`、`PASSWORD`

### 第 4 步：获取 Python 完整路径

```bash
# macOS / Linux
which python3

# Windows (PowerShell)
where.exe python
```

### 第 5 步：配置全局 Hook

打开 `~/.claude/settings.json`，合并以下 `hooks` 字段：

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "<PYTHON完整路径> <脚本完整路径>/notify_email.py",
            "shell": "powershell",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

> **关键：Windows 上必须设置 `"shell": "powershell"`，不能省略，不能用 `"bash"`！**
> 省略时 Claude Code 会尝试使用 Git Bash，但会把 `Git\bin` 目录当成可执行文件导致 ENOENT 错误。

**各平台完整示例：**

Windows（当前电脑实际配置）：
```json
"command": "C:\\zss\\important-software\\anaconda3\\python.exe C:\\Users\\15085\\.claude\\scripts\\notify_email.py",
"shell": "powershell"
```

macOS：
```json
"command": "/usr/bin/python3 /Users/你的用户名/.claude/scripts/notify_email.py",
"shell": "bash"
```

Linux：
```json
"command": "/usr/bin/python3 /home/你的用户名/.claude/scripts/notify_email.py",
"shell": "bash"
```

> macOS/Linux 上 bash 正常工作，无需改为 powershell。

### 第 6 步：（可选）添加项目级 Hook 双重保障

在每个项目根目录创建 `.claude/settings.json`，内容同上。这样即使全局配置加载失败，项目级配置仍可生效。

```bash
# 批量为所有项目添加（Windows PowerShell）
$projects = @("C:\path\to\project1", "C:\path\to\project2")
$hookJson = '{"hooks":{"Stop":[{"matcher":"","hooks":[{"type":"command","command":"C:\zss\important-software\anaconda3\python.exe C:\Users\15085\.claude\scripts\notify_email.py","shell":"powershell","timeout":30}]}]}}'

foreach ($dir in $projects) {
    New-Item -ItemType Directory -Force -Path "$dir\.claude" | Out-Null
    Set-Content -Path "$dir\.claude\settings.json" -Value $hookJson
    Write-Host "已创建: $dir\.claude\settings.json"
}
```

### 第 7 步：测试

```bash
# 手动运行脚本测试
cd 你的项目目录
python ~/.claude/scripts/notify_email.py
```

检查邮箱是否收到通知邮件。

---

## 工作原理

```
用户提问 → Claude Code 执行任务 → 任务完成触发 Stop Hook
                                         ↓
                                  PowerShell 执行 notify_email.py
                                         ↓
                          读取 stdin JSON (cwd, session_id, transcript_path)
                                         ↓
                          定位 ~/.claude/projects/<项目目录>/<session_id>.jsonl
                                         ↓
                          等待 2 秒（文件刷盘）
                                         ↓
                          从 JSONL 末尾反向遍历：
                          - 找最后一条 type=user（非 tool_result）→ 用户问题
                          - 找最后一条 type=assistant（含 text）→ 助手回答
                                         ↓
                              发送邮件通知
```

### JSONL 文件结构

Claude Code 的会话记录存储在 `~/.claude/projects/<项目目录名>/` 下，每个会话一个 `.jsonl` 文件，每行一个 JSON 对象：

```jsonl
{"type":"user","message":{"role":"user","content":"帮我写个函数"}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"好的，这是代码..."},{"type":"tool_use","name":"Write","input":{...}}]}}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"文件已写入"}]}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"已完成！"}]}}
```

**提取逻辑**：从末尾往前，找第一个 `type=user` 且 content 不含 `tool_result` 的条目（用户问题），找第一个 `type=assistant` 且 content 含 `type=text` 的条目（助手回答）。

### 项目目录名转换规则

Claude Code 将工作目录路径转换为项目目录名的规则：**`/ \ : _` 全部替换为 `-`**

| 工作目录 | 项目目录名 |
|----------|-----------|
| `C:\zss\repo\github\my_project` | `C--zss-repo-github-my-project` |
| `/home/user/projects/my_app` | `-home-user-projects-my-app` |

### Hook stdin JSON 字段

Stop Hook 触发时，Claude Code 通过 stdin 传入以下 JSON：

```json
{
  "session_id": "uuid-string",
  "transcript_path": "/path/to/session.jsonl",
  "cwd": "/current/project/path",
  "project_id": "project-hash",
  "project_path": "/your/project",
  "hook_event_name": "Stop"
}
```

脚本优先使用 `transcript_path` 和 `cwd`，如果 stdin 为空则回退到 `os.getcwd()` 推算。

---

## 自定义配置

### 修改收件人

默认发件人和收件人相同。发给其他邮箱：

```python
s.sendmail(USER, ["target@example.com"], msg.as_string())
```

### 排除项目

```python
SKIP_PROJECTS = {"noval", "private-project", "secret-repo"}
```

### 使用其他邮箱

| 邮箱 | SMTP_SERVER | SMTP_PORT | 说明 |
|------|-------------|-----------|------|
| 163 | `smtp.163.com` | `465` | 需要授权码 |
| QQ | `smtp.qq.com` | `465` | 需要授权码 |
| Gmail | `smtp.gmail.com` | `465` | 需要应用专用密码 |
| Outlook | `smtp.office365.com` | `587` | 需要应用密码 |

### 暂停邮件通知

- 删除 `settings.json` 中的 `Stop` Hook 配置
- 把项目名加入 `SKIP_PROJECTS`
- 设置 `"disableAllHooks": true`

---

## 当前电脑完整配置参考

### 文件清单

```
~/.claude/scripts/
├── notify_email.py          # 邮件通知脚本（核心）
├── last_email.txt           # 上次发送的邮件内容（调试用）
└── hook_debug.json          # Hook 调试日志

~/.claude/settings.json      # 全局 Hook 配置

各项目/.claude/settings.json  # 项目级 Hook 配置（双重保障）
```

### settings.json（全局）

路径：`C:\Users\15085\.claude\settings.json`

Hook 相关部分：

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "C:\\zss\\important-software\\anaconda3\\python.exe C:\\Users\\15085\\.claude\\scripts\\notify_email.py",
            "shell": "powershell",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 项目级 settings.json 模板

路径：`<项目根目录>/.claude/settings.json`

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "C:\\zss\\important-software\\anaconda3\\python.exe C:\\Users\\15085\\.claude\\scripts\\notify_email.py",
            "shell": "powershell",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

---

## 常见问题

**Q: 报错 SMTPAuthenticationError (550, User has no permission)?**
A: 必须使用客户端授权码，不能使用登录密码。163 邮箱 → 设置 → POP3/SMTP/IMAP → 生成授权码。

**Q: Hook 报错 ENOENT: no such file or directory, uv_spawn?**
A: Windows 上必须设置 `"shell": "powershell"`，不能用 `"bash"` 也不能省略。这是 Claude Code 在 Windows + Git Bash 环境下的已知问题。

**Q: 收到邮件但用户问题不对/不是最新的?**
A: 脚本已加 `time.sleep(2)` 等待文件刷盘。如果仍有问题，可增大等待时间。

**Q: 另一个 VS Code 窗口的 Hook 不生效?**
A: 需要重启该窗口的 Claude Code，使其加载最新的 settings.json。也可在项目目录下创建 `.claude/settings.json` 作为双重保障。

**Q: 如何卸载?**
A: 删除 `settings.json` 中的 `hooks.Stop` 配置 + 删除 `~/.claude/scripts/notify_email.py` 文件。
