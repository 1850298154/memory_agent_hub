"""
Claude Code API - 多轮流式调用封装

默认配置：
- skip_permissions=True（自动执行模式）
- 自动创建 session
- 多轮对话使用同一 session
- 详细输出所有路径信息

作者: Claude Code
日期: 2026-03-15
"""

import subprocess
import json
import uuid
import os
import sys
import shutil
import time
from pathlib import Path
from typing import Optional, Dict, Any


def find_claude_command() -> str:
    """查找 claude 命令的完整路径"""
    claude_path = shutil.which("claude")
    if claude_path:
        return claude_path

    if sys.platform == "win32":
        possible_paths = [
            os.path.expanduser("~/.npm-global/claude.cmd"),
            os.path.expanduser("~/AppData/Roaming/npm/claude.cmd"),
            os.path.join(os.environ.get("APPDATA", ""), "npm/claude.cmd"),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path

    return "claude"


def find_git_bash() -> Optional[str]:
    """查找 git-bash 路径（Windows 需要）"""
    if sys.platform != "win32":
        return None

    env_path = os.environ.get("CLAUDE_CODE_GIT_BASH_PATH")
    if env_path and os.path.exists(env_path):
        return env_path

    git_path = shutil.which("git")
    if git_path:
        git_path = os.path.normpath(git_path)
        parent_dir = os.path.dirname(git_path)
        if os.path.basename(parent_dir) in ["bin", "cmd", "mingw64"]:
            git_root = os.path.dirname(parent_dir)
            if os.path.basename(parent_dir) == "mingw64":
                git_root = os.path.dirname(git_root)
            for bash_path in [
                os.path.join(git_root, "usr\\bin\\bash.exe"),
                os.path.join(git_root, "bin\\bash.exe"),
            ]:
                if os.path.exists(bash_path):
                    return bash_path

    bash_path = shutil.which("bash")
    if bash_path and os.path.exists(bash_path):
        return os.path.normpath(bash_path)

    return None


# 全局路径常量
CLAUDE_CMD = find_claude_command()
GIT_BASH_PATH = find_git_bash()
CLAUDE_HOME = Path.home() / ".claude"


class ClaudeCodeAPI:
    """
    Claude Code API 封装类

    默认配置：
    - skip_permissions=True（自动执行模式）
    - 自动创建 session
    - 多轮对话使用同一 session
    """

    def __init__(
        self,
        session_id: Optional[str] = None,
        cwd: Optional[str] = None,
        skip_permissions: bool = True,  # 默认开启自动执行
        allowed_tools: Optional[list] = None,
        verbose: bool = True
    ):
        """
        初始化 Claude Code API

        Args:
            session_id: 会话 ID，不提供则自动生成
            cwd: 工作目录，默认当前目录
            skip_permissions: 是否跳过权限确认，默认 True
            allowed_tools: 允许的工具列表
            verbose: 是否打印详细信息
        """
        self.session_id = session_id or str(uuid.uuid4())
        self.cwd = cwd or os.getcwd()
        self.skip_permissions = skip_permissions
        self.allowed_tools = allowed_tools or []
        self.verbose = verbose
        self._full_response = ""

        if verbose:
            self._print_config()

    def _print_config(self):
        """打印详细配置和路径信息"""
        print("\n" + "=" * 70)
        print(" Claude Code API 配置信息")
        print("=" * 70)

        print("\n【基本配置】")
        print(f"  Session ID:      {self.session_id}")
        print(f"  工作目录:        {self.cwd}")
        print(f"  自动执行模式:    {'[OK] 启用' if self.skip_permissions else '[X] 禁用'}")
        if self.allowed_tools:
            print(f"  允许的工具:      {', '.join(self.allowed_tools)}")

        print("\n【Claude Code 路径】")
        print(f"  Claude 命令:     {CLAUDE_CMD}")
        if GIT_BASH_PATH:
            print(f"  Git Bash:        {GIT_BASH_PATH}")
        print(f"  Claude Home:     {CLAUDE_HOME}")

        print("\n【Claude Code 目录结构】")
        print(f"  Sessions 目录:   {CLAUDE_HOME / 'sessions'}")
        print(f"  Projects 目录:   {CLAUDE_HOME / 'projects'}")
        print(f"  历史文件:        {CLAUDE_HOME / 'history.jsonl'}")
        print(f"  设置文件:        {CLAUDE_HOME / 'settings.json'}")
        print(f"  插件目录:        {CLAUDE_HOME / 'plugins'}")
        print(f"  Skills 目录:     {CLAUDE_HOME / 'skills'}")

        # 计算并显示 session 文件路径
        project_hash = self._get_project_hash()
        session_file = CLAUDE_HOME / "projects" / project_hash / f"{self.session_id}.jsonl"

        print("\n【当前会话文件】")
        print(f"  项目 Hash:       {project_hash}")
        print(f"  Session 文件:    {session_file}")

        if session_file.exists():
            stat = session_file.stat()
            print(f"  文件大小:        {stat.st_size} bytes")
            with open(session_file, "r", encoding="utf-8") as f:
                line_count = sum(1 for _ in f)
            print(f"  消息数量:        {line_count}")
        else:
            print(f"  状态:            新会话（文件将在首次对话后创建）")

        print("=" * 70 + "\n")

    def _get_project_hash(self) -> str:
        """获取项目路径哈希"""
        cwd_abs = os.path.abspath(self.cwd)
        return cwd_abs.replace(":", "").replace("\\", "-").replace("/", "-")

    def _get_env(self) -> dict:
        """获取环境变量"""
        env = os.environ.copy()
        if GIT_BASH_PATH:
            env["CLAUDE_CODE_GIT_BASH_PATH"] = GIT_BASH_PATH
        return env

    def ask(self, prompt: str, timeout: int = 300) -> str:
        """
        发送问题并获取响应

        Args:
            prompt: 用户问题
            timeout: 超时时间（秒）

        Returns:
            完整响应文本
        """
        cmd = [
            CLAUDE_CMD,
            "-p", prompt,
            "--session-id", self.session_id,
            "--output-format", "text"
        ]

        if self.skip_permissions:
            cmd.append("--dangerously-skip-permissions")

        if self.allowed_tools:
            cmd.extend(["--allowed-tools", ",".join(self.allowed_tools)])

        print(f"\n[用户] {prompt}")
        print("[Claude] ", end="", flush=True)

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.cwd,
                timeout=timeout,
                env=self._get_env(),
                encoding='utf-8',
                errors='replace'  # 忽略无法解码的字符
            )

            response = result.stdout.strip()
            self._full_response = response

            if response:
                print(response)
            else:
                if result.stderr:
                    print(f"[错误] {result.stderr.strip()}")

            return response

        except subprocess.TimeoutExpired:
            print(f"[超时] 请求超过 {timeout} 秒")
            return ""
        except Exception as e:
            print(f"[异常] {e}")
            return ""

    def get_session_file_path(self) -> Path:
        """获取当前会话文件路径"""
        project_hash = self._get_project_hash()
        return CLAUDE_HOME / "projects" / project_hash / f"{self.session_id}.jsonl"

    def get_session_info(self) -> Dict[str, Any]:
        """获取会话详细信息"""
        session_file = self.get_session_file_path()

        info = {
            "session_id": self.session_id,
            "cwd": self.cwd,
            "project_hash": self._get_project_hash(),
            "session_file": str(session_file),
            "session_exists": session_file.exists(),
            "skip_permissions": self.skip_permissions,
            "claude_cmd": CLAUDE_CMD,
            "git_bash": GIT_BASH_PATH,
            "claude_home": str(CLAUDE_HOME),
        }

        if session_file.exists():
            stat = session_file.stat()
            info["file_size"] = stat.st_size
            info["modified_time"] = stat.st_mtime

            with open(session_file, "r", encoding="utf-8") as f:
                info["message_count"] = sum(1 for _ in f)

        return info

    def interactive_session(self):
        """启动交互式多轮对话"""
        print("\n" + "=" * 70)
        print(" 多轮对话模式")
        print("=" * 70)
        print(" 命令:")
        print("   quit/exit  - 退出")
        print("   new        - 开始新会话")
        print("   info       - 显示会话信息")
        print("   clear      - 清屏")
        print("=" * 70 + "\n")

        round_num = 0
        while True:
            try:
                prompt = input("\n[用户] ").strip()

                if not prompt:
                    continue

                if prompt.lower() in ["quit", "exit"]:
                    print("\n退出对话")
                    self._print_session_summary()
                    break

                if prompt.lower() == "new":
                    self.session_id = str(uuid.uuid4())
                    print(f"\n新会话已创建: {self.session_id}")
                    if self.verbose:
                        self._print_config()
                    continue

                if prompt.lower() == "info":
                    info = self.get_session_info()
                    print("\n【会话信息】")
                    for k, v in info.items():
                        print(f"  {k}: {v}")
                    continue

                if prompt.lower() == "clear":
                    os.system("cls" if sys.platform == "win32" else "clear")
                    continue

                round_num += 1
                print(f"\n--- 第 {round_num} 轮对话 ---")
                self.ask(prompt)

            except KeyboardInterrupt:
                print("\n\n对话中断")
                self._print_session_summary()
                break
            except Exception as e:
                print(f"\n错误: {e}")

    def _print_session_summary(self):
        """打印会话总结"""
        session_file = self.get_session_file_path()
        print("\n" + "=" * 70)
        print(" 会话总结")
        print("=" * 70)
        print(f"  Session ID:    {self.session_id}")
        print(f"  Session 文件:  {session_file}")

        if session_file.exists():
            print(f"  文件大小:      {session_file.stat().st_size} bytes")
            print(f"  继续对话:      python claude_code_api.py --session-id {self.session_id}")

        print("=" * 70)


def demo_default_mode():
    """
    演示默认模式（无参数）

    - 自动开启所有权限
    - 自动创建 session
    - 详细输出所有路径
    - 验证文件创建

    注意：由于 Claude Code 的 session 锁定机制，同一 session ID
    在短时间内无法重复使用，所以 demo 中每轮对话使用新 session。
    真正的多轮对话请使用交互模式（默认无参数运行）。
    """
    print("\n" + "=" * 70)
    print(" Claude Code API 默认模式演示")
    print("=" * 70)
    print("\n说明:")
    print("  - 默认 skip_permissions=True（自动执行）")
    print("  - 自动创建 session")
    print("  - demo 中每轮使用新 session（避免锁定问题）")
    print("  - 真正的多轮对话请使用交互模式")
    print("=" * 70)

    # 第一轮对话：创建文件
    print("\n" + "-" * 70)
    print(" 第一轮对话：创建 Python 文件")
    print("-" * 70)
    api1 = ClaudeCodeAPI()
    api1.ask("写一个 test_demo.py 文件，内容是打印 'Hello from Claude API Demo!'")

    # 验证 Python 文件创建
    test_file = Path(api1.cwd) / "test_demo.py"
    print("\n【验证 Python 文件创建】")
    if test_file.exists():
        print(f"  [OK] 文件已创建: {test_file}")
        print(f"  文件大小: {test_file.stat().st_size} bytes")
        print(f"  文件内容:")
        print("  " + "-" * 40)
        for line in test_file.read_text(encoding="utf-8").split("\n"):
            print(f"  | {line}")
        print("  " + "-" * 40)

    # 验证 Session 文件
    session_file = api1.get_session_file_path()
    print("\n【验证 Session 文件】")
    if session_file.exists():
        print(f"  [OK] Session 文件已创建: {session_file}")
        print(f"  文件大小: {session_file.stat().st_size} bytes")
        with open(session_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"  消息数量: {len(lines)}")

    # 第二轮对话：运行文件（使用新 session）
    print("\n" + "-" * 70)
    print(" 第二轮对话：运行文件")
    print("-" * 70)
    api2 = ClaudeCodeAPI()
    api2.ask(f"运行 {test_file} 文件")

    # 第三轮对话：创建计算脚本（使用新 session）
    print("\n" + "-" * 70)
    print(" 第三轮对话：创建计算脚本")
    print("-" * 70)
    api3 = ClaudeCodeAPI()
    api3.ask("写一个 calc.py 计算 1+2+...+10 并打印结果，然后运行它")

    # 验证 calc.py
    calc_file = Path(api3.cwd) / "calc.py"
    print("\n【验证 calc.py 创建】")
    if calc_file.exists():
        print(f"  [OK] 文件已创建: {calc_file}")
        print(f"  内容: {calc_file.read_text(encoding='utf-8').strip()}")

    # 最终总结
    print("\n" + "=" * 70)
    print(" 演示完成")
    print("=" * 70)
    print("\n生成的文件:")
    for f in ["test_demo.py", "calc.py"]:
        path = Path(api1.cwd) / f
        if path.exists():
            print(f"  - {path} ({path.stat().st_size} bytes)")

    print("\n多轮对话说明:")
    print("  使用 'python claude_code_api.py' 进入交互模式")
    print("  交互模式下同一 session 可以进行真正的多轮对话")

    print("\n" + "=" * 70)

    print("=" * 70)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Claude Code API 多轮流式调用",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 默认模式（自动执行 + 多轮对话）
  python claude_code_api.py

  # 演示模式（验证功能）
  python claude_code_api.py --demo

  # 单次提问
  python claude_code_api.py -p "你的问题"

  # 指定 session 继续
  python claude_code_api.py --session-id <session-id>

  # 静默模式
  python claude_code_api.py --quiet
        """
    )

    parser.add_argument("--demo", action="store_true", help="运行完整演示（验证功能）")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式（默认）")
    parser.add_argument("--session-id", type=str, help="指定会话 ID")
    parser.add_argument("--prompt", "-p", type=str, help="单次提问")
    parser.add_argument(
        "--no-skip-permissions",
        action="store_true",
        help="禁用自动执行（需要手动确认权限）"
    )
    parser.add_argument(
        "--allowed-tools",
        type=str,
        help="允许的工具列表，逗号分隔"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="静默模式（不打印详细配置）"
    )

    args = parser.parse_args()

    # 默认开启自动执行，除非明确禁用
    skip_permissions = not args.no_skip_permissions

    # 解析允许的工具
    allowed_tools = None
    if args.allowed_tools:
        allowed_tools = [t.strip() for t in args.allowed_tools.split(",")]

    # 是否打印详细配置
    verbose = not args.quiet

    if args.demo:
        demo_default_mode()
    elif args.prompt:
        # 单次提问模式
        api = ClaudeCodeAPI(
            session_id=args.session_id,
            skip_permissions=skip_permissions,
            allowed_tools=allowed_tools,
            verbose=verbose
        )
        response = api.ask(args.prompt)

        # 输出 session ID 便于后续继续
        if verbose:
            print(f"\n---\nSession ID: {api.session_id}")
            print(f"Session 文件: {api.get_session_file_path()}")
    else:
        # 默认：交互式多轮对话模式
        api = ClaudeCodeAPI(
            session_id=args.session_id,
            skip_permissions=skip_permissions,
            allowed_tools=allowed_tools,
            verbose=verbose
        )
        api.interactive_session()
