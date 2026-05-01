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

# ========== 邮箱配置 ==========
SMTP_SERVER = "smtp.163.com"
SMTP_PORT = 465
USER = "13021208988@163.com"
PASSWORD = "DCajBgdZ8vpbwsyE"
PASSWORD = "HK4rL369py9DvVfQ"

# ========== 排除项目 ==========
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

            # 找最后一条用户纯文本问题
            if t == "user" and not user_query:
                msg = entry.get("message", {})
                content = msg.get("content", "")
                # content 是字符串 → 直接就是用户输入
                if isinstance(content, str) and content.strip():
                    user_query = content.strip()[:500]
                # content 是列表 → 提取 text 部分，跳过 tool_result
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

    # 调试日志（保存原始 stdin）
    debug_path = Path.home() / ".claude" / "scripts" / "hook_debug.json"
    try:
        import time as _time
        debug_path.write_text(json.dumps({
            "timestamp": _time.strftime("%Y-%m-%d %H:%M:%S"),
            "stdin_received": bool(raw_stdin),
            "stdin_length": len(raw_stdin),
            "raw_stdin_preview": raw_stdin[:500] if raw_stdin else "",
            "hook_input_keys": list(hook_input.keys()),
            "cwd": cwd,
            "project_name": project_name,
            "transcript_path_from_hook": hook_input.get("transcript_path", ""),
            "session_id_from_hook": hook_input.get("session_id", ""),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    # 3. 排除项目
    if project_name.lower() in SKIP_PROJECTS:
        print(f"已跳过: {project_name} 在排除列表中")
        sys.exit(0)

    # 4. 获取 transcript 路径
    transcript_path = hook_input.get("transcript_path", "")
    if not transcript_path:
        # 回退：根据 cwd 手动定位
        project_dir = cwd.replace("/", "-").replace("\\", "-").replace(":", "-").replace("_", "-")
        sessions_dir = Path.home() / ".claude" / "projects" / project_dir
        session_id = hook_input.get("session_id", "")
        if session_id:
            candidate = sessions_dir / f"{session_id}.jsonl"
            if candidate.exists():
                transcript_path = str(candidate)
        if not transcript_path:
            # 找最新的 jsonl
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

    # 同时保存到本地文件，方便调试
    log_path = Path.home() / ".claude" / "scripts" / "last_email.txt"
    try:
        log_path.write_text(f"标题: {subject}\n\n{chr(10).join(body_parts)}", encoding="utf-8")
    except Exception:
        pass

    print(f"邮件已发送: {subject}")
