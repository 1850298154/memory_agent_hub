# Claude Code 邮件通知 — 完整配置指南

## 功能效果

每当 Claude Code 完成任务或弹出选择题，自动发送邮件通知：

**任务完成时（Stop 事件）：**
```
标题: [项目名] 帮我写一个hello world函数
正文:
  项目: KAG

  用户问题:
  帮我写一个hello world函数

  助手回答:
  print("Hello, World!")
```

**弹出选择题时（PreToolUse + AskUserQuestion）：**
```
标题: [项目名] 需要你做选择 - 你的幸运数字是几？
正文:
  项目: KAG

  Claude 需要你做一个选择：

  【猜数字】你的幸运数字是几？
    1. 7 — 七上八下
    2. 8 — 发发发
    3. 9 — 长长久久
```

- 自动提取**最后的用户问题**和**最后的助手回答**
- **弹出选择题时即时通知**，无需等到任务结束
- 支持**排除指定项目**（如隐私项目不发邮件）
- **跨项目通用**：全局配置即可，所有项目自动生效
- **语音播报**：任务完成或需要做决策时语音提醒（跨平台，支持 Mac + Windows）
- 配置与代码分离：**敏感信息放 .env 文件**，不硬编码在脚本中
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

### 坑 6：邮件标题中文导致 UnicodeEncodeError

**现象**：PreToolUse Hook 触发了但邮件没发出去，报错 `UnicodeEncodeError: 'utf-8' codec can't encode character '\udcad'`。

**原因**：PowerShell 传递 stdin JSON 时，部分字符会被编码为 UTF-8 代理字符（surrogate），Python 的 `Header()` 无法处理这些非法代理字符。

**解决**：在 `send()` 函数中用 `sanitize()` 清除代理字符，邮件标题用 `Header(subject, "utf-8")` 编码。

### 坑 7：Elicitation 不是有效的 Hook 事件名

**现象**：配置了 `"Elicitation"` Hook 但从未触发。

**原因**：Claude Code 没有 `Elicitation` 这个 Hook 事件。弹出选择题应该用 `PreToolUse` 事件 + `AskUserQuestion` matcher。

**解决**：使用 `"PreToolUse": [{"matcher": "AskUserQuestion", ...}]` 配置。

### 坑 8：Windows PowerShell 传 stdin 中文乱码

**现象**：邮件标题和正文中的中文显示为 `鎴戝垰鐢熸垚浜嗕竴涓?` 之类的乱码。

**原因**：PowerShell 传递 stdin 时使用系统默认编码（中文 Windows 为 GBK），而 Python 的 `sys.stdin.read()` 也按系统编码解码，导致 UTF-8 中文被当作 GBK 解读。

**解决**：用 `sys.stdin.buffer.read()` 读取原始字节，再强制 `decode("utf-8")` 解码。

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
# macOS / Linux
mkdir -p ~/.claude/scripts

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\scripts"
```

### 第 3 步：创建配置文件和脚本

1. 将 `notify_email.py` 复制到 `~/.claude/scripts/notify_email.py`
2. 将 `.env.example` 复制为 `~/.claude/scripts/.env`，填写邮箱配置：

```bash
# .env 内容（必填）
SMTP_SERVER=smtp.163.com
SMTP_PORT=465
EMAIL_USER=你的邮箱@163.com
EMAIL_PASSWORD=你的授权码

# 语音播报开关（可选，默认开启）
VOICE_ENABLED=true
```

> 敏感信息只存在于 `.env` 文件中，脚本不会硬编码密码。

### 第 4 步：安装语音播报依赖（可选）

语音播报需要 `pyttsx3`，不安装则仅邮件通知：

```bash
pip install pyttsx3 python-dotenv
```

> Mac 自带 `say` 命令作为回退，Windows 上 pyttsx3 使用系统 SAPI 语音引擎。

```bash
# macOS / Linux
which python3

# Windows (PowerShell)
where.exe python
```

### 第 5 步：获取 Python 完整路径

```bash
# macOS / Linux
which python3

# Windows (PowerShell)
where.exe python
```

### 第 6 步：配置全局 Hook

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
            "shell": "<powershell 或 bash>",
            "timeout": 30
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "AskUserQuestion",
        "hooks": [
          {
            "type": "command",
            "command": "<PYTHON完整路径> <脚本完整路径>/notify_email.py",
            "shell": "<powershell 或 bash>",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

> **两个 Hook 的作用：**
> - **Stop**：Claude Code 完成任务时触发，通知你任务已完成
> - **PreToolUse + AskUserQuestion**：Claude Code 弹出选择题时触发，通知你需要回来做选择

> **关键：Windows 上必须设置 `"shell": "powershell"`，不能省略，不能用 `"bash"`！**
> 省略时 Claude Code 会尝试使用 Git Bash，但会把 `Git\bin` 目录当成可执行文件导致 ENOENT 错误。

**各平台完整示例：**

Windows：
```json
"command": "C:\\Python311\\python.exe C:\\Users\\你的用户名\\.claude\\scripts\\notify_email.py",
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

### 第 7 步：测试

```bash
# 方法 1：手动运行脚本测试（不依赖 Hook）
python ~/.claude/scripts/notify_email.py

# 方法 2：用 claude -p 测试完整 Hook 流程
cd 你的项目目录
claude -p "用AskUserQuestion弹出选择题让我猜数字"
```

检查邮箱是否收到通知邮件。

---

## 工作原理

### 事件 1：任务完成（Stop Hook）

```
用户提问 → Claude Code 执行任务 → 任务完成触发 Stop Hook
                                         ↓
                                  执行 notify_email.py
                                         ↓
                          读取 stdin JSON (cwd, session_id, transcript_path)
                                         ↓
                          定位 ~/.claude/projects/<项目目录>/<session_id>.jsonl
                                         ↓
                          从 JSONL 第一条获取 cwd → 项目名
                                         ↓
                          等待 2 秒（文件刷盘）
                                         ↓
                          从 JSONL 末尾反向遍历：
                          - 找最后一条 type=user（非 tool_result）→ 用户问题
                          - 找最后一条 type=assistant（含 text）→ 助手回答
                                         ↓
                              发送邮件通知
```

### 事件 2：弹出选择题（PreToolUse + AskUserQuestion）

```
Claude 调用 AskUserQuestion → PreToolUse Hook 触发
                                      ↓
                              执行 notify_email.py
                                      ↓
                    读取 stdin JSON (tool_name=AskUserQuestion, tool_input={questions, options})
                                      ↓
                    从 tool_input 提取问题和选项
                                      ↓
                    发送邮件：标题 [项目名] 需要你做选择 - 问题
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

PreToolUse Hook 触发时，额外包含：

```json
{
  "session_id": "uuid-string",
  "transcript_path": "/path/to/session.jsonl",
  "cwd": "/current/project/path",
  "hook_event_name": "PreToolUse",
  "tool_name": "AskUserQuestion",
  "tool_input": {
    "questions": [
      {
        "question": "你的幸运数字是几？",
        "header": "猜数字",
        "options": [
          {"label": "7", "description": "七上八下"},
          {"label": "8", "description": "发发发"}
        ],
        "multiSelect": false
      }
    ]
  },
  "tool_use_id": "call_xxxxx"
}
```

脚本根据 `hook_event_name` 区分事件类型，分别处理。

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

- 删除 `settings.json` 中的 `hooks` 配置
- 把项目名加入 `SKIP_PROJECTS`
- 设置 `"disableAllHooks": true`

---

## 文件清单

```
~/.claude/scripts/
├── notify_email.py          # 邮件通知 + 语音播报脚本（核心）
├── .env                     # 邮箱配置和语音开关（敏感信息，不要提交到 Git）

~/.claude/settings.json      # 全局 Hook 配置（必须配置）
```

---

## settings.json 完整示例

### Windows

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "C:\\Python311\\python.exe C:\\Users\\你的用户名\\.claude\\scripts\\notify_email.py",
            "shell": "powershell",
            "timeout": 30
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "AskUserQuestion",
        "hooks": [
          {
            "type": "command",
            "command": "C:\\Python311\\python.exe C:\\Users\\你的用户名\\.claude\\scripts\\notify_email.py",
            "shell": "powershell",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### macOS / Linux

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 /home/你的用户名/.claude/scripts/notify_email.py",
            "shell": "bash",
            "timeout": 30
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "AskUserQuestion",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 /home/你的用户名/.claude/scripts/notify_email.py",
            "shell": "bash",
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

**Q: 邮件中文显示乱码?**
A: 脚本已使用 `sys.stdin.buffer.read()` + `decode("utf-8")` 修复 Windows PowerShell 的编码问题。确保脚本版本包含此修复。

**Q: 弹出选择题时没有收到邮件?**
A: 确认 `settings.json` 中有 `PreToolUse` Hook 且 matcher 为 `"AskUserQuestion"`（不是 `"Elicitation"`）。修改配置后需要**启动新的 Claude Code 会话**才能生效（`--resume` 旧会话不会加载新配置）。

**Q: 另一个 VS Code 窗口的 Hook 不生效?**
A: 需要重启该窗口的 Claude Code，使其加载最新的 settings.json。

**Q: 如何卸载?**
A: 删除 `settings.json` 中的 `hooks` 配置 + 删除 `~/.claude/scripts/notify_email.py` 文件。

**Q: 语音播报不生效?**
A: 1) 确认已安装 `pyttsx3`（`pip install pyttsx3`）；2) 检查 `.env` 中 `VOICE_ENABLED=true`；3) Mac 无需 pyttsx3，自带 `say` 命令回退。

**Q: 关闭语音播报?**
A: 在 `.env` 中设置 `VOICE_ENABLED=false`，或删除该行（默认开启）。
