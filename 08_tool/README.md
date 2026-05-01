# Claude Code 任务完成邮件通知 - 一键配置指南

## 功能概述

每当 Claude Code 完成任务时，自动发送邮件通知。邮件包含：项目名称 + 用户提出的问题。
支持排除指定项目（如隐私项目不发送邮件）。

---

## 一键配置步骤

### 第 1 步：创建脚本目录

```bash
mkdir -p ~/.claude/scripts
```

### 第 2 步：创建邮件通知脚本

将以下内容保存为 `~/.claude/scripts/notify_email.py`：

```python
"""Claude Code 任务完成邮件通知脚本（全局 Hook 用）"""
import smtplib, ssl, json, sys, os
from email.mime.text import MIMEText
from pathlib import Path

# ========== 邮箱配置 ==========
SMTP_SERVER = "smtp.163.com"
SMTP_PORT = 465
USER = "@163.com"
PASSWORD = ""

# ========== 排除项目 ==========
SKIP_PROJECTS = {"noval"}


def send(subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = USER
    msg["Subject"] = subject
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as s:
        s.login(USER, PASSWORD)
        s.sendmail(USER, [USER], msg.as_string())


def cwd_to_project_dir(cwd):
    return cwd.replace("/", "-").replace("\\", "-").replace(":", "-").replace("_", "-")


def get_last_user_query(sessions_dir):
    if not sessions_dir.exists():
        return ""
    jsonl_files = sorted(sessions_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True)
    if not jsonl_files:
        return ""
    try:
        with open(jsonl_files[0], "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return ""
    for line in reversed(lines):
        try:
            entry = json.loads(line)
            if entry.get("type") != "user":
                continue
            msg = entry.get("message", {})
            content = msg.get("content", "")
            if isinstance(content, str):
                text = content.strip()
            elif isinstance(content, list):
                texts = []
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        t = item.get("text", "").strip()
                        if t:
                            texts.append(t)
                text = " ".join(texts).strip()
            else:
                continue
            if text:
                return text[:300]
        except Exception:
            continue
    return ""


if __name__ == "__main__":
    cwd = os.environ.get("CLAUDE_PWD", os.environ.get("PWD", os.getcwd()))
    project_name = Path(cwd).name if cwd else "unknown"

    if project_name.lower() in SKIP_PROJECTS:
        print(f"已跳过: {project_name} 在排除列表中")
        sys.exit(0)

    project_dir = cwd_to_project_dir(cwd)
    sessions_dir = Path.home() / ".claude" / "projects" / project_dir
    query = get_last_user_query(sessions_dir)

    if query:
        subject = f"[{project_name}] {query[:50]}"
    else:
        default_subject = sys.argv[1] if len(sys.argv) > 1 else "Claude Code 任务完成"
        subject = f"[{project_name}] {default_subject}"

    body_parts = [f"项目: {project_name}"]
    if query:
        body_parts.append(f"\n用户问题: {query}")

    send(subject, "\n".join(body_parts))
    print(f"邮件已发送: {subject}")
```

### 第 3 步：获取 Python 完整路径

```bash
# macOS / Linux
which python3

# Windows (Git Bash)
which python
```

记下输出结果。

### 第 4 步：配置全局 Hook

打开 `~/.claude/settings.json`，合并以下内容：

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$PWD\" && <PYTHON路径> \"<脚本路径>/notify_email.py\" \"Claude Code 任务完成\" \"任务已执行完毕\"",
            "shell": "bash",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**各平台示例（替换 Python 路径）：**

macOS:

```json
"command": "cd \"$PWD\" && /usr/bin/python3 \"$HOME/.claude/scripts/notify_email.py\" \"Claude Code 任务完成\" \"任务已执行完毕\""
```

Windows (当前电脑实际配置):

```json
"command": "cd \"$PWD\" && /c/zss/important-software/anaconda3/python \"C:/Users/15085/.claude/scripts/notify_email.py\" \"Claude Code 任务完成\" \"任务已执行完毕\""
```

### 第 5 步：测试

```bash
cd 你的某个项目目录
python ~/.claude/scripts/notify_email.py
```

检查邮箱是否收到通知邮件。

---

## 当前电脑完整配置参考

### notify_email.py

路径: `C:/Users/15085/.claude/scripts/notify_email.py`

内容同第 2 步，已填入实际邮箱和授权码。

### settings.json

路径: `C:/Users/15085/.claude/settings.json`

当前完整内容：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "89bf938731644c33ac1e84b6ebbbb804.vsZLIMCIqDk0JJXf",
    "ANTHROPIC_MODEL": "glm-5.1",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5.1",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.1",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.1",
    "ANTHROPIC_REASONING_MODEL": "glm-5.1"
  },
  "statusLine": {
    "type": "command",
    "command": "%USERPROFILE%\\.claude\\ccline\\ccline.exe",
    "padding": 0
  },
  "skipDangerousModePermissionPrompt": true,
  "permissions": {
    "defaultMode": "bypassPermissions"
  },
  "includeCoAuthoredBy": false,
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$PWD\" && /c/zss/important-software/anaconda3/python \"C:/Users/15085/.claude/scripts/notify_email.py\" \"Claude Code 任务完成\" \"任务已执行完毕\"",
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

## 自定义配置

### 修改收件人

默认发件人和收件人相同。如需发给其他邮箱：

```python
s.sendmail(USER, ["target@example.com"], msg.as_string())
```

### 排除更多项目

```python
SKIP_PROJECTS = {"noval", "private-project", "secret-repo"}
```

### 使用其他邮箱

| 邮箱    | SMTP_SERVER            | SMTP_PORT | 说明             |
| ------- | ---------------------- | --------- | ---------------- |
| 163     | `smtp.163.com`       | `465`   | 需要授权码       |
| QQ      | `smtp.qq.com`        | `465`   | 需要授权码       |
| Gmail   | `smtp.gmail.com`     | `465`   | 需要应用专用密码 |
| Outlook | `smtp.office365.com` | `587`   | 需要应用密码     |

### 暂停邮件通知

方法一：删除 `settings.json` 中 `Stop` Hook 配置
方法二：把项目名加入 `SKIP_PROJECTS`
方法三：设置 `"disableAllHooks": true`

---

## 工作原理

```
用户提问 → Claude Code 执行任务 → 任务完成触发 Stop Hook
                                         ↓
                                  执行 notify_email.py
                                         ↓
                          读取 ~/.claude/projects/<项目>/ 会话文件
                                         ↓
                          提取最后一条用户问题
                                         ↓
                              发送邮件通知
```

用户问题提取逻辑：

1. 根据当前工作目录计算 Claude Code 项目目录名（路径中的 `/ \ : _` 全部替换为 `-`）
2. 在 `~/.claude/projects/<项目目录名>/` 下找最新的 `.jsonl` 会话文件
3. 从后往前找最后一条 `type=user` 的消息
4. 提取文本内容作为用户问题

---

## 常见问题

**Q: 报错 SMTPAuthenticationError (550, User has no permission)?**
A: 必须使用客户端授权码，不能使用登录密码。去邮箱设置 → POP3/SMTP/IMAP → 生成授权码。

**Q: 收到邮件但没有用户问题?**
A: 检查 `~/.claude/projects/` 下对应项目目录是否存在 `.jsonl` 会话文件，项目目录名转换是否正确。

**Q: Windows 下 Hook 不触发?**
A: Python 路径使用 Git Bash 格式（`/c/...`），文件路径使用正斜杠。

**Q: 如何卸载?**
A: 删除 `settings.json` 中的 `hooks.Stop` 配置和 `~/.claude/scripts/notify_email.py` 文件。
