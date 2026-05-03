"""Claude Code 任务完成邮件通知脚本（全局 Hook 用）

支持两种 Hook 事件：
1. Stop：任务完成时触发，从 transcript 提取用户问题和助手回答
2. PreToolUse + AskUserQuestion：Claude 弹出选择题时触发，提取问题和选项

通知方式：
  - 邮件通知（必选）
  - 语音播报（可选）：播报项目名 + 事件类型（完成/需要做决策）

配置步骤详见同目录 README.md
"""
import smtplib, ssl, json, sys, os, time, subprocess, platform, re
from email.mime.text import MIMEText
from email.header import Header
from pathlib import Path

# 加载 .env 配置
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

# ========== 邮箱配置（从 .env 读取）==========
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.163.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "465"))
USER = os.environ.get("EMAIL_USER", "")
PASSWORD = os.environ.get("EMAIL_PASSWORD", "")

# ========== 排除项目（可选修改）==========
SKIP_PROJECTS = {"noval"}

# ========== 语音播报开关 ==========
VOICE_ENABLED = os.environ.get("VOICE_ENABLED", "true").lower() == "true"


def sanitize(text):
    """清除 surrogate 字符，避免 UTF-8 编码报错"""
    if not isinstance(text, str):
        return str(text)
    return text.encode("utf-8", errors="replace").decode("utf-8")


def truncate_for_voice(text, max_len=80):
    """智能截断文本用于语音播报：1句直接说，2句都说，3句以上只保留首尾用省略连接"""
    if not text or not text.strip():
        return ""
    text = text.strip()
    # 清理代码块、反引号内容、多余符号
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`]+`', '', text)
    text = re.sub(r'[{}()\[\]<>|#$%^&*_~]', '', text)
    # 按中英文句号、问号、感叹号、分号、换行断句
    sentences = re.split(r'[。！？；\n.!?;]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return text[:max_len]
    if len(sentences) == 1:
        return sentences[0][:max_len]
    if len(sentences) == 2:
        return "，".join(s[:max_len] for s in sentences)
    # 3句及以上：首句 + 省略 + 尾句
    return f"{sentences[0][:max_len]}，省略，{sentences[-1][:max_len]}"


def send(subject, body):
    if not USER or not PASSWORD:
        print("邮件未发送：缺少 EMAIL_USER 或 EMAIL_PASSWORD 配置")
        return
    subject = sanitize(subject)
    body = sanitize(body)
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = USER
    msg["Subject"] = Header(subject, "utf-8")
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as s:
        s.login(USER, PASSWORD)
        s.sendmail(USER, [USER], msg.as_string())


def speak(text):
    """跨平台语音播报，用独立进程播放，不阻塞主脚本"""
    if not VOICE_ENABLED or not text.strip():
        return
    # 构造语音播放脚本，用独立进程执行，避免 Hook 超时杀掉语音
    voice_script = (
        "import pyttsx3,sys,subprocess,platform\n"
        "text = " + repr(text) + "\n"
        "try:\n"
        "    engine = pyttsx3.init()\n"
        "    voices = engine.getProperty('voices')\n"
        "    for v in voices:\n"
        "        if any(k in v.name.lower() or k in v.id.lower() for k in ['chinese','zh','huihui','yaoyao']):\n"
        "            engine.setProperty('voice', v.id)\n"
        "            break\n"
        "    engine.setProperty('rate', 180)\n"
        "    engine.say(text)\n"
        "    engine.runAndWait()\n"
        "except Exception:\n"
        "    try:\n"
        "        if platform.system() == 'Darwin':\n"
        "            subprocess.call(['say', '-v', 'Ting-Ting', text])\n"
        "    except Exception:\n"
        "        pass\n"
    )
    try:
        kwargs = {}
        if platform.system() == "Windows":
            kwargs["creationflags"] = 0x08000000  # CREATE_NO_WINDOW
        subprocess.Popen([sys.executable, "-c", voice_script], **kwargs)
    except Exception:
        pass


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


def get_project_name(cwd, transcript_path):
    """从 transcript 第一条 cwd 字段获取真实项目路径，回退到 cwd 参数"""
    real_cwd = ""
    if transcript_path:
        try:
            with open(transcript_path, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                        if "cwd" in entry and entry["cwd"]:
                            real_cwd = entry["cwd"]
                            break
                    except Exception:
                        continue
        except Exception:
            pass
    return Path(real_cwd or cwd).name if (real_cwd or cwd) else "unknown"


def handle_ask_user_question(hook_input, cwd, transcript_path):
    """处理 PreToolUse + AskUserQuestion 事件：提取选择题并发邮件 + 语音播报"""
    tool_input = hook_input.get("tool_input", {})
    questions = tool_input.get("questions", [])

    project_name = get_project_name(cwd, transcript_path)

    if project_name.lower() in SKIP_PROJECTS:
        print(f"已跳过: {project_name} 在排除列表中")
        return

    # 构建选择题文本
    question_parts = []
    first_question_text = ""
    for i, q in enumerate(questions):
        q_text = q.get("question", "")
        if i == 0:
            first_question_text = q_text
        header = q.get("header", "")
        options = q.get("options", [])
        opt_lines = []
        for j, o in enumerate(options):
            label = o.get("label", "")
            desc = o.get("description", "")
            if desc:
                opt_lines.append(f"  {j+1}. {label} — {desc}")
            else:
                opt_lines.append(f"  {j+1}. {label}")
        part = f"{'【' + header + '】' if header else ''}{q_text}\n" + "\n".join(opt_lines)
        question_parts.append(part)

    questions_str = "\n\n".join(question_parts)

    # 发邮件
    subject = f"[{project_name}] 需要你做选择 - {first_question_text[:30]}"
    body = f"项目: {project_name}\n\nClaude 需要你做一个选择：\n\n{questions_str}"

    send(subject, body)
    print(f"邮件已发送: {subject}")

    # 语音播报：项目名 → 动作 → 问题
    voice_q = truncate_for_voice(first_question_text)
    speak(f"项目名为{project_name}，需要做选择。用户的要求问题是，{voice_q}")

if __name__ == "__main__":
    # 1. 从 stdin 读取 Hook 输入（用 buffer 强制 UTF-8 解码，避免 Windows GBK 乱码）
    hook_input = {}
    raw_stdin = ""
    if not sys.stdin.isatty():
        try:
            raw_bytes = sys.stdin.buffer.read()
            raw_stdin = raw_bytes.decode("utf-8", errors="replace")
        except Exception:
            raw_stdin = sys.stdin.read()
        if raw_stdin:
            try:
                hook_input = json.loads(raw_stdin)
            except Exception:
                pass

    # 2. 获取基本参数
    cwd = hook_input.get("cwd", "") or hook_input.get("project_path", "") or os.getcwd()
    transcript_path = hook_input.get("transcript_path", "")
    hook_event = hook_input.get("hook_event_name", "")
    tool_name = hook_input.get("tool_name", "")

    # 3. 判断事件类型
    if hook_event == "PreToolUse" and tool_name == "AskUserQuestion":
        handle_ask_user_question(hook_input, cwd, transcript_path)
        sys.exit(0)

    # 4. 以下为 Stop 事件处理逻辑
    if not transcript_path:
        project_dir = cwd.replace("/", "-").replace("\\", "-").replace(":", "-").replace("_", "-")
        sessions_dir = Path.home() / ".claude" / "projects" / project_dir
        session_id = hook_input.get("session_id", "")
        if session_id:
            candidate = sessions_dir / f"{session_id}.jsonl"
            if candidate.exists():
                transcript_path = str(candidate)
        if not transcript_path:
            jsonl_files = sorted(sessions_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True)
            if jsonl_files:
                transcript_path = str(jsonl_files[0])

    project_name = get_project_name(cwd, transcript_path)

    # 5. 排除项目
    if project_name.lower() in SKIP_PROJECTS:
        print(f"已跳过: {project_name} 在排除列表中")
        sys.exit(0)

    # 6. 提取用户问题和助手回答（等待文件刷盘）
    time.sleep(2)
    user_query, assistant_answer = extract_from_transcript(transcript_path)

    # 7. 构建邮件
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

    # 8. 语音播报：项目名 → 动作 → 用户问题 → AI结果
    voice_query = truncate_for_voice(user_query)
    voice_result = truncate_for_voice(assistant_answer)
    parts = [f"项目名为{project_name}，已经完成。"]
    if voice_query:
        parts.append(f"用户的要求问题是，{voice_query}。")
    if voice_result:
        parts.append(f"AI执行的结果是，{voice_result}。")
    speak("".join(parts))
