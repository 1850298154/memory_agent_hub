# Claude Code API 多轮流式调用

将 Claude Code CLI 封装为 Python API，支持多轮对话、流式输出和自动执行模式。

## 目录结构

```
06_claude_api/
├── README.md              # 本文档
└── claude_code_api.py     # Python API 封装
```

## 功能特性

| 功能 | 说明 |
|------|------|
| 多轮对话 | 通过 `session-id` 保持同一会话上下文 |
| 流式输出 | 实时返回 Claude 响应 |
| 自动执行模式 | 跳过权限确认，自动执行工具 |
| 工具限制 | 可指定允许使用的工具 |
| 会话管理 | 查看/列出会话信息 |

## Claude Code 文件路径

### 核心路径

| 路径 | 说明 |
|------|------|
| `~/.claude/` | Claude Code 主目录 |
| `~/.claude/sessions/` | 活跃会话映射目录 (pid -> sessionId) |
| `~/.claude/projects/` | 项目会话数据目录 |
| `~/.claude/history.jsonl` | 命令历史记录 |
| `~/.claude/settings.json` | 用户设置 |
| `~/.claude/plugins/` | 插件目录 |
| `~/.claude/skills/` | 用户自定义 skills |

### 会话文件路径格式

```
~/.claude/projects/{project_hash}/{session_id}.jsonl
```

其中 `project_hash` 是工作目录路径的转换：
- `D:\zyt\git_ln\memory_agent_hub` → `D--zyt-git-ln-memory-agent-hub`

### 示例路径

```
Windows:
C:\Users\{username}\.claude\
├── sessions\
│   └── 21116.json                    # PID -> SessionID 映射
├── projects\
│   └── D--zyt-git-ln-memory-agent-hub\
│       └── f67c96a2-40fe-454e-b713-ee51af46eed6.jsonl  # 会话历史
├── history.jsonl
├── settings.json
├── plugins\
│   └── marketplaces\
│       └── claude-plugins-official\
└── skills\
    └── excalidraw-diagram-generator\

Git Bash 路径（Windows 自动检测）:
D:\software\git\install\Git\usr\bin\bash.exe
```

## 安装要求

- Python 3.7+
- Claude Code CLI 已安装并配置
- Windows 需要 Git Bash

```bash
# 检查 Claude Code 是否安装
claude --version

# Windows 需要设置 Git Bash 路径（自动检测或手动设置）
# 自动检测：代码会自动查找 Git 安装目录下的 bash.exe
# 手动设置：设置环境变量 CLAUDE_CODE_GIT_BASH_PATH
export CLAUDE_CODE_GIT_BASH_PATH="D:\\software\\git\\install\\Git\\usr\\bin\\bash.exe"
```

## 使用方法

### 1. 运行演示

```bash
python claude_code_api.py --demo
```

输出示例：
```
============================================================
Claude Code API 配置信息
============================================================
Session ID: 550e8400-e29b-41d4-a716-446655440000
工作目录: D:\zyt\git_ln\memory_agent_hub
------------------------------------------------------------
Claude Code 路径配置:
  Claude Home:    C:\Users\zooos\.claude
  Sessions 目录:  C:\Users\zooos\.claude\sessions
  Projects 目录:  C:\Users\zooos\.claude\projects
  历史文件:       C:\Users\zooos\.claude\history.jsonl
------------------------------------------------------------
当前会话文件: C:\Users\zooos\.claude\projects\D--zyt-git-ln-memory-agent-hub\550e8400....jsonl
============================================================
```

### 2. 交互模式

```bash
python claude_code_api.py -i
# 或
python claude_code_api.py --interactive
```

### 3. 单次提问

```bash
python claude_code_api.py -p "解释一下这个项目的结构"
```

### 4. 指定会话 ID

```bash
python claude_code_api.py --session-id "my-session-id" -p "继续上一个问题"
```

### 5. 自动执行模式（跳过权限确认）

```bash
# 方式1: 使用演示脚本
python claude_code_api.py --demo-auto

# 方式2: 命令行参数
python claude_code_api.py --dangerously-skip-permissions -p "写一个 hello.py 并执行它"

# 方式3: 限制允许的工具
python claude_code_api.py --dangerously-skip-permissions --allowed-tools "Bash,Write" -p "你的问题"
```

**警告**: 自动执行模式会跳过所有权限确认，仅在信任的环境（沙箱/隔离环境）中使用！

## Python 代码示例

### 基本使用

```python
from claude_code_api import ClaudeCodeAPI

# 创建 API 实例
api = ClaudeCodeAPI()

# 流式调用
for event in api.ask("帮我分析这个项目"):
    pass  # 事件已在内部处理并打印

# 非流式调用
response = api.ask_simple("项目的主要功能是什么？")
print(response)
```

### 多轮对话

```python
from claude_code_api import ClaudeCodeAPI

# 固定 session_id 保证多轮对话
api = ClaudeCodeAPI(session_id="my-conversation-001")

# 第一轮
for _ in api.ask("介绍一下 Python 的装饰器"):
    pass

# 第二轮 - 可以引用之前的内容
for _ in api.ask("能给个实际例子吗？"):
    pass

# 第三轮
for _ in api.ask("这个例子有什么问题？"):
    pass
```

### 获取会话信息

```python
api = ClaudeCodeAPI()

# 当前会话信息
info = api.get_session_info()
print(info)
# {
#     'session_id': 'xxx',
#     'cwd': 'D:\\zyt\\git_ln\\memory_agent_hub',
#     'project_hash': 'D--zyt-git-ln-memory-agent-hub',
#     'session_file': 'C:\\Users\\zooos\\.claude\\projects\\...',
#     'session_exists': True,
#     'session_file_size': 12345,
#     'message_count': 10
# }

# 列出所有会话
sessions = api.list_sessions()
for s in sessions:
    print(f"{s['session_id']}: {s['size']} bytes")
```

### 处理流式事件

```python
from claude_code_api import ClaudeCodeAPI

api = ClaudeCodeAPI()

for event in api.ask("写一个快速排序算法"):
    event_type = event.get("type", "")

    if event_type == "content_block_delta":
        text = event.get("delta", {}).get("text", "")
        # 自定义处理文本增量

    elif event_type == "AskUserQuestion":
        # Claude 反问用户
        questions = event.get("questions", [])
        # 处理交互请求
```

### 自动执行模式

```python
from claude_code_api import ClaudeCodeAPI

# 创建自动执行模式的 API 实例
api = ClaudeCodeAPI(
    skip_permissions=True,           # 跳过权限确认
    allowed_tools=["Bash", "Write"]  # 可选：限制允许的工具
)

# 让 Claude 写代码并执行
for _ in api.ask("""
    请执行以下任务：
    1. 创建一个 fibonacci.py 文件
    2. 写入斐波那契数列的实现
    3. 运行并测试输出
"""):
    pass
```

### CLI 直接调用自动执行

```python
import subprocess
import json

# 直接使用 claude CLI 的自动执行模式
result = subprocess.run([
    "claude", "-p",
    "写一个 hello.py 并运行它",
    "--dangerously-skip-permissions",
    "--output-format", "json"
], capture_output=True, text=True)

print(result.stdout)
```

## CLI 参数说明

```
usage: claude_code_api.py [-h] [--demo] [--demo-auto] [--interactive] [--session-id SESSION_ID]
                          [--prompt PROMPT] [--dangerously-skip-permissions] [--allowed-tools TOOLS]

Claude Code API 多轮流式调用

optional arguments:
  -h, --help            show this help message and exit
  --demo                运行基础演示
  --demo-auto           运行自动执行模式演示
  --interactive, -i     交互模式
  --session-id SESSION_ID
                        指定会话 ID
  --prompt PROMPT, -p PROMPT
                        单次提问
  --dangerously-skip-permissions
                        跳过权限确认（自动执行模式）
  --allowed-tools TOOLS
                        允许的工具列表，逗号分隔，如: Bash,Edit,Write
```

## 流式输出格式

使用 `--output-format stream-json` 时，返回的 JSON 事件类型包括：

| 事件类型 | 说明 |
|---------|------|
| `content_block_delta` | 文本增量，包含 `delta.text` |
| `content_block_start` | 内容块开始 |
| `content_block_stop` | 内容块结束 |
| `message_start` | 消息开始 |
| `message_stop` | 消息结束 |
| `AskUserQuestion` | Claude 反问用户 |

## 多轮对话原理

```
┌─────────────────────────────────────────────────────────┐
│                    Claude Code CLI                       │
├─────────────────────────────────────────────────────────┤
│  --session-id <uuid> ──► 保持同一会话上下文              │
│                                                          │
│  ~/.claude/projects/{hash}/{session_id}.jsonl            │
│     └── 存储完整对话历史                                  │
│     └── 每次调用时自动加载历史作为上下文                   │
└─────────────────────────────────────────────────────────┘

第1轮: session_id=abc, prompt="问题1"
  └── 创建 abc.jsonl，写入对话

第2轮: session_id=abc, prompt="问题2"
  └── 读取 abc.jsonl 历史
  └── 追加新对话到 abc.jsonl
  └── Claude 能引用之前的内容
```

## 注意事项

1. **会话文件增长**：长对话会导致 `.jsonl` 文件变大，定期清理 `~/.claude/projects/`

2. **并发安全**：同一 session_id 不支持并发调用，需要串行执行

3. **超时处理**：默认超时 300 秒，可通过 `timeout` 参数调整

4. **Windows 路径**：代码已处理 Windows 路径格式兼容

5. **自动执行模式风险**：
   - 仅在沙箱/隔离环境中使用
   - 建议使用 `--allowed-tools` 限制工具范围
   - 避免在包含敏感数据的环境中启用
   - Claude 可能执行删除、修改等破坏性操作

## 权限模式对比

| 模式 | CLI 参数 | 说明 |
|------|---------|------|
| 默认模式 | (无) | 每个工具调用需要用户确认 |
| 自动执行 | `--dangerously-skip-permissions` | 自动执行所有工具 |
| 工具限制 | `--allowed-tools Bash,Write` | 只允许指定工具 |
| 组合使用 | 两者结合 | 自动执行但只限于指定工具 |

## 相关资源

- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [Claude API 文档](https://docs.anthropic.com/claude-reference)
- [skillsmp.com](https://skillsmp.com) - Skills 市场
