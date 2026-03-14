"""
Claude Code API - 多轮流式调用封装

实现将 Claude Code 作为 API 使用，支持：
- 多轮对话保持同一会话
- 流式输出
- 自动管理 session
- 自动执行模式（跳过权限确认）

作者: Claude Code
日期: 2026-03-15
"""

import subprocess
import json
import uuid
import os
import sys
import shutil
from pathlib import Path
from typing import Optional, Generator, Dict, Any, List


def find_claude_command() -> str:
    """
    查找 claude 命令的完整路径

    Returns:
        claude 命令的完整路径
    """
    # 尝试直接查找
    claude_path = shutil.which("claude")
    if claude_path:
        return claude_path

    # Windows 常见路径
    if sys.platform == "win32":
        possible_paths = [
            os.path.expanduser("~/.npm-global/claude.cmd"),
            os.path.expanduser("~/AppData/Roaming/npm/claude.cmd"),
            os.path.join(os.environ.get("APPDATA", ""), "npm/claude.cmd"),
            "C:/Users/{}/AppData/Roaming/npm/claude.cmd".format(os.environ.get("USERNAME", "")),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path

    # 默认返回 claude，让系统尝试
    return "claude"


def find_git_bash() -> Optional[str]:
    """
    查找 git-bash 路径（Windows 需要）

    Returns:
        bash.exe 的完整路径，找不到返回 None
    """
    if sys.platform != "win32":
        return None

    # 检查环境变量中是否已设置
    env_path = os.environ.get("CLAUDE_CODE_GIT_BASH_PATH")
    if env_path and os.path.exists(env_path):
        return env_path

    # 尝试从 PATH 中查找 git 位置
    git_path = shutil.which("git")
    if git_path:
        # git 可能在:
        # - Git/mingw64/bin/git.exe (mingw64 安装)
        # - Git/bin/git.exe
        # - Git/cmd/git.exe
        git_path = os.path.normpath(git_path)
        # 向上两级或一级获取 Git 根目录
        parent_dir = os.path.dirname(git_path)
        if os.path.basename(parent_dir) in ["bin", "cmd", "mingw64"]:
            git_root = os.path.dirname(parent_dir)
            if os.path.basename(parent_dir) == "mingw64":
                git_root = os.path.dirname(git_root)

            possible_bash = [
                os.path.join(git_root, "usr\\bin\\bash.exe"),
                os.path.join(git_root, "bin\\bash.exe"),
            ]
            for bash_path in possible_bash:
                if os.path.exists(bash_path):
                    return bash_path

    # 直接从 PATH 中查找 bash
    bash_path = shutil.which("bash")
    if bash_path and os.path.exists(bash_path):
        return os.path.normpath(bash_path)

    # 默认路径
    possible_paths = [
        "C:\\Program Files\\Git\\usr\\bin\\bash.exe",
        "C:\\Program Files\\Git\\bin\\bash.exe",
        "C:\\Program Files (x86)\\Git\\usr\\bin\\bash.exe",
        "C:\\Program Files (x86)\\Git\\bin\\bash.exe",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None


# Claude 命令路径
CLAUDE_CMD = find_claude_command()
# Git Bash 路径（Windows）
GIT_BASH_PATH = find_git_bash()


class ClaudeCodeAPI:
    """
    Claude Code API 封装类

    将 Claude Code CLI 作为 API 调用，支持多轮流式对话
    """

    # Claude Code 配置路径
    CLAUDE_HOME = Path.home() / ".claude"
    SESSIONS_DIR = CLAUDE_HOME / "sessions"
    PROJECTS_DIR = CLAUDE_HOME / "projects"
    HISTORY_FILE = CLAUDE_HOME / "history.jsonl"

    def __init__(
        self,
        session_id: Optional[str] = None,
        cwd: Optional[str] = None,
        skip_permissions: bool = False,
        allowed_tools: Optional[list] = None
    ):
        """
        初始化 Claude Code API

        Args:
            session_id: 会话 ID，不提供则自动生成
            cwd: 工作目录，默认当前目录
            skip_permissions: 是否跳过权限确认（自动执行模式）
            allowed_tools: 允许的工具列表，如 ["Bash", "Edit", "Write"]
        """
        self.session_id = session_id or str(uuid.uuid4())
        self.cwd = cwd or os.getcwd()
        self.skip_permissions = skip_permissions
        self.allowed_tools = allowed_tools or []

        # 打印配置信息
        self._print_config()

    def _print_config(self):
        """打印配置和路径信息"""
        print("=" * 60)
        print("Claude Code API 配置信息")
        print("=" * 60)
        print(f"Session ID: {self.session_id}")
        print(f"工作目录: {self.cwd}")
        print(f"Claude 命令: {CLAUDE_CMD}")
        if GIT_BASH_PATH:
            print(f"Git Bash: {GIT_BASH_PATH}")
        print(f"自动执行模式: {'启用 (跳过权限确认)' if self.skip_permissions else '禁用'}")
        if self.allowed_tools:
            print(f"允许的工具: {', '.join(self.allowed_tools)}")
        print("-" * 60)
        print("Claude Code 路径配置:")
        print(f"  Claude Home:    {self.CLAUDE_HOME}")
        print(f"  Sessions 目录:  {self.SESSIONS_DIR}")
        print(f"  Projects 目录:  {self.PROJECTS_DIR}")
        print(f"  历史文件:       {self.HISTORY_FILE}")
        print("-" * 60)

        # 计算 project session 文件路径
        project_hash = self._get_project_hash()
        session_file = self.PROJECTS_DIR / project_hash / f"{self.session_id}.jsonl"
        print(f"当前会话文件: {session_file}")
        print("=" * 60)
        print()

    def _get_project_hash(self) -> str:
        """
        获取项目路径的哈希值（Claude Code 内部使用的目录名格式）

        Returns:
            项目路径哈希字符串
        """
        # Claude Code 使用路径转换：D:\zyt\git_ln\... -> D--zyt-git-ln-...
        cwd_abs = os.path.abspath(self.cwd)
        # 替换特殊字符
        hash_name = cwd_abs.replace(":", "").replace("\\", "-").replace("/", "-")
        return hash_name

    def _get_env(self) -> dict:
        """
        获取 subprocess 环境变量

        Returns:
            环境变量字典
        """
        env = os.environ.copy()

        # Windows 需要设置 Git Bash 路径
        if GIT_BASH_PATH:
            env["CLAUDE_CODE_GIT_BASH_PATH"] = GIT_BASH_PATH

        return env

    def ask(
        self,
        prompt: str,
        stream: bool = True,
        timeout: int = 300,
        skip_permissions: Optional[bool] = None
    ) -> Generator[Dict[str, Any], None, None]:
        """
        发送问题并获取流式响应

        Args:
            prompt: 用户问题
            stream: 是否流式输出
            timeout: 超时时间（秒）
            skip_permissions: 是否跳过权限确认，None 则使用实例设置

        Yields:
            流式返回的事件字典
        """
        # 使用实例设置或参数覆盖
        skip = skip_permissions if skip_permissions is not None else self.skip_permissions

        cmd = [
            CLAUDE_CMD,
            "-p", prompt,
            "--session-id", self.session_id,
            "--output-format", "stream-json"
        ]

        # 添加自动执行模式参数
        if skip:
            cmd.append("--dangerously-skip-permissions")

        # 添加允许的工具
        if self.allowed_tools:
            cmd.extend(["--allowed-tools", ",".join(self.allowed_tools)])

        print(f"\n[用户] {prompt}")
        print(f"[Claude] ", end="", flush=True)

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=self.cwd,
            bufsize=1,
            env=self._get_env()
        )

        try:
            for line in process.stdout:
                line = line.strip()
                if not line:
                    continue

                try:
                    event = json.loads(line)
                    yield event

                    # 处理不同类型的事件
                    self._handle_event(event)

                except json.JSONDecodeError:
                    # 非JSON行，直接输出
                    print(line, end="", flush=True)

        finally:
            process.wait(timeout=timeout)

    def _handle_event(self, event: Dict[str, Any]):
        """
        处理流式事件

        Args:
            event: 事件字典
        """
        event_type = event.get("type", "")

        if event_type == "content_block_delta":
            # 文本内容增量
            delta = event.get("delta", {})
            text = delta.get("text", "")
            if text:
                print(text, end="", flush=True)

        elif event_type == "message_stop":
            # 消息结束
            print()  # 换行

        elif event_type == "AskUserQuestion":
            # Claude 反问用户
            print("\n[Claude 需要更多信息]")
            questions = event.get("questions", [])
            for q in questions:
                print(f"  - {q.get('question', '')}")

    def ask_simple(self, prompt: str, timeout: int = 300, skip_permissions: Optional[bool] = None) -> str:
        """
        发送问题并获取完整响应（非流式）

        Args:
            prompt: 用户问题
            timeout: 超时时间（秒）
            skip_permissions: 是否跳过权限确认，None 则使用实例设置

        Returns:
            完整响应文本
        """
        skip = skip_permissions if skip_permissions is not None else self.skip_permissions

        cmd = [
            CLAUDE_CMD,
            "-p", prompt,
            "--session-id", self.session_id,
            "--output-format", "text"
        ]

        if skip:
            cmd.append("--dangerously-skip-permissions")

        if self.allowed_tools:
            cmd.extend(["--allowed-tools", ",".join(self.allowed_tools)])

        print(f"\n[用户] {prompt}")
        print(f"[Claude] ", end="", flush=True)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=self.cwd,
            timeout=timeout,
            env=self._get_env()
        )

        print(result.stdout)
        return result.stdout

    def interactive_session(self):
        """
        启动交互式多轮对话会话
        """
        print("\n" + "=" * 60)
        print("交互式多轮对话模式")
        print("输入 'quit' 或 'exit' 退出")
        print("输入 'new' 开始新会话")
        print("=" * 60 + "\n")

        while True:
            try:
                prompt = input("\n[用户] ").strip()

                if not prompt:
                    continue

                if prompt.lower() in ["quit", "exit"]:
                    print("退出对话")
                    break

                if prompt.lower() == "new":
                    self.session_id = str(uuid.uuid4())
                    print(f"新会话已创建: {self.session_id}")
                    continue

                # 流式调用
                for _ in self.ask(prompt):
                    pass

            except KeyboardInterrupt:
                print("\n\n对话中断")
                break
            except Exception as e:
                print(f"\n错误: {e}")

    def get_session_info(self) -> Dict[str, Any]:
        """
        获取当前会话信息

        Returns:
            会话信息字典
        """
        project_hash = self._get_project_hash()
        session_file = self.PROJECTS_DIR / project_hash / f"{self.session_id}.jsonl"

        info = {
            "session_id": self.session_id,
            "cwd": self.cwd,
            "project_hash": project_hash,
            "session_file": str(session_file),
            "session_exists": session_file.exists(),
        }

        if session_file.exists():
            stat = session_file.stat()
            info["session_file_size"] = stat.st_size
            info["session_modified"] = stat.st_mtime

            # 统计消息数量
            with open(session_file, "r", encoding="utf-8") as f:
                info["message_count"] = sum(1 for _ in f)

        return info

    def list_sessions(self) -> list:
        """
        列出当前项目的所有会话

        Returns:
            会话列表
        """
        project_hash = self._get_project_hash()
        project_dir = self.PROJECTS_DIR / project_hash

        if not project_dir.exists():
            return []

        sessions = []
        for file in project_dir.glob("*.jsonl"):
            sessions.append({
                "session_id": file.stem,
                "file": str(file),
                "size": file.stat().st_size,
                "modified": file.stat().st_mtime
            })

        return sessions


def demo():
    """演示多轮流式调用"""
    print("\n" + "=" * 60)
    print("Claude Code API 多轮流式调用演示")
    print("=" * 60)

    # 创建 API 实例
    api = ClaudeCodeAPI()

    # 显示会话信息
    info = api.get_session_info()
    print("\n会话信息:")
    for key, value in info.items():
        print(f"  {key}: {value}")

    # 演示多轮对话
    print("\n" + "-" * 60)
    print("开始多轮对话演示...")
    print("-" * 60)

    questions = [
        "简单介绍一下你自己",
        "你刚才说了什么？",
        "我们的对话 ID 是什么？"
    ]

    for q in questions:
        print(f"\n{'=' * 40}")
        for _ in api.ask(q):
            pass

    print("\n" + "=" * 60)
    print("演示完成")

    # 显示所有会话
    print("\n当前项目所有会话:")
    sessions = api.list_sessions()
    for s in sessions:
        print(f"  - {s['session_id'][:20]}... ({s['size']} bytes)")


def demo_auto_execute():
    """
    演示自动执行模式

    在此模式下，Claude Code 会自动执行工具（如 Bash, Write, Edit 等），
    而不需要用户手动确认权限。

    警告：仅在你信任的环境中使用，比如沙箱或隔离环境。
    """
    print("\n" + "=" * 60)
    print("Claude Code API 自动执行模式演示")
    print("=" * 60)
    print("\n警告: 此模式会跳过所有权限确认!")
    print("建议仅在沙箱或隔离环境中使用!")
    print("-" * 60)

    # 创建自动执行模式的 API 实例
    # skip_permissions=True 启用自动执行
    # allowed_tools 可以限制允许使用的工具
    api = ClaudeCodeAPI(
        skip_permissions=True,
        allowed_tools=["Bash", "Write", "Read", "Edit"]  # 可选：限制工具
    )

    # 示例：让 Claude 写一个 Python 文件并执行
    prompt = """
    请执行以下任务：
    1. 在当前目录创建一个 test_hello.py 文件
    2. 文件内容是打印 "Hello from Claude Code API!" 的简单 Python 脚本
    3. 运行这个脚本并显示输出
    """

    print(f"\n[用户] {prompt.strip()}")
    print("\n[Claude] 开始自动执行...\n")
    print("-" * 40)

    # 流式获取响应
    for _ in api.ask(prompt):
        pass

    print("\n" + "=" * 60)
    print("自动执行演示完成")
    print("=" * 60)


def interactive():
    """启动交互模式"""
    api = ClaudeCodeAPI()
    api.interactive_session()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Claude Code API 多轮流式调用")
    parser.add_argument("--demo", action="store_true", help="运行基础演示")
    parser.add_argument("--demo-auto", action="store_true", help="运行自动执行模式演示")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式")
    parser.add_argument("--session-id", type=str, help="指定会话 ID")
    parser.add_argument("--prompt", "-p", type=str, help="单次提问")
    parser.add_argument(
        "--dangerously-skip-permissions",
        action="store_true",
        help="跳过权限确认（自动执行模式）"
    )
    parser.add_argument(
        "--allowed-tools",
        type=str,
        help="允许的工具列表，逗号分隔，如: Bash,Edit,Write"
    )

    args = parser.parse_args()

    # 解析允许的工具
    allowed_tools = None
    if args.allowed_tools:
        allowed_tools = [t.strip() for t in args.allowed_tools.split(",")]

    if args.demo:
        demo()
    elif args.demo_auto:
        demo_auto_execute()
    elif args.interactive:
        api = ClaudeCodeAPI(
            skip_permissions=args.dangerously_skip_permissions,
            allowed_tools=allowed_tools
        )
        api.interactive_session()
    elif args.prompt:
        api = ClaudeCodeAPI(
            session_id=args.session_id,
            skip_permissions=args.dangerously_skip_permissions,
            allowed_tools=allowed_tools
        )
        for _ in api.ask(args.prompt):
            pass
    else:
        # 默认进入交互模式
        api = ClaudeCodeAPI(
            skip_permissions=args.dangerously_skip_permissions,
            allowed_tools=allowed_tools
        )
        api.interactive_session()
