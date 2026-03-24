# OpenClaw 新手必装技能清单

> 安装日期：2026-03-23
> 安装位置：`~\.agents\skills\`

---

## 已安装技能列表

### 1. skill-vetter (安全审查)

**功能概述：** 技能安全审计工具，在安装任何第三方技能前进行安全检查。

**主要功能：**
- 元数据检查：验证技能名称、版本、作者信息
- 权限分析：评估 fileRead/fileWrite/network/shell 权限风险等级
- 内容扫描：检测敏感文件引用、可疑命令、混淆代码等危险信号
- 仿冒检测：识别仿冒知名技能的"抢注"行为
- 生成安全审查报告（SAFE/WARNING/DANGER/BLOCK）

**使用场景：**
- 安装 ClawHub 或 GitHub 上的新技能前
- 定期审计已安装技能的安全性
- 审核他人分享的技能文件

**安装量：** 10K+ | **来源：** useai-pro/openclaw-skills-security

---

### 2. find-skills (发现安装)

**功能概述：** 技能发现与安装工具，帮助用户搜索和安装社区技能。

**主要功能：**
- `npx skills find [query]` - 按关键词搜索技能
- `npx skills add <package>` - 安装技能
- `npx skills check` - 检查技能更新
- `npx skills update` - 更新所有已安装技能

**使用场景：**
- 想要扩展 AI 代理能力时搜索相关技能
- 发现新技能并一键安装
- 管理和更新现有技能

**官方资源：** https://skills.sh/

---

### 3. tavily-search (联网搜索)

**功能概述：** 基于 Tavily 的 LLM 优化网络搜索工具。

**主要功能：**
- 高质量搜索结果，专为 LLM 优化
- 支持多种搜索深度：ultra-fast/fast/basic/advanced
- 支持主题过滤：general/news/finance
- 时间范围筛选：day/week/month/year
- 域名过滤：包含/排除特定域名
- 支持返回完整页面内容

**使用场景：**
- 搜索网络获取最新信息
- 查找特定主题的文章或资料
- 新闻资讯检索

**安装量：** 3.8K+ | **来源：** tavily-ai/skills

---

### 4. self-improving-agent (自我进化)

**功能概述：** 通用自我改进代理，从所有技能交互中学习并持续进化。

**主要功能：**
- **多记忆架构**：语义记忆(模式/规则) + 情景记忆(具体经验) + 工作记忆(当前会话)
- **自我修正**：检测并修复技能指导中的错误
- **自我验证**：定期验证技能准确性
- **钩子集成**：在技能事件时自动触发（before_start/after_complete/on_error）
- **进化标记**：可追溯的变更记录

**使用场景：**
- 让 AI 代理从每次交互中学习
- 自动改进技能文件
- 建立长期经验积累系统

**安装量：** 16K+ | **来源：** charon-fan/agent-playbook

---

### 5. csv-data-summarizer (概要总结)

**功能概述：** CSV 数据自动分析与可视化工具。

**主要功能：**
- 自动检测数据类型并适配分析策略
- 生成统计摘要（均值、标准差、缺失值等）
- 智能创建可视化图表（时间序列、相关性热图、分布图等）
- 提供可操作的数据洞察

**支持数据类型：**
- 销售/电商数据
- 客户数据
- 财务数据
- 运营数据
- 调查问卷数据

**安装量：** 1.1K+ | **来源：** coffeefuelbump/csv-data-summarizer-claude-skill

---

### 6. agent-browser (浏览器自动化)

**功能概述：** 基于 Chrome/Chromium 的浏览器自动化 CLI 工具。

**主要功能：**
- 页面导航与快照
- 表单填写与点击交互
- 截图与 PDF 生成
- 认证状态管理（支持多种登录方式）
- 网络请求监控与拦截
- 多标签页/多会话管理
- iOS 模拟器支持

**使用场景：**
- 自动化网页操作
- Web 应用测试
- 数据抓取
- 网站截图
- 表单自动填写

**安装量：** 121.5K+ | **来源：** vercel-labs/agent-browser

---

### 7. pdf (PDF处理)

**功能概述：** 全面的 PDF 文件处理工具包。

**主要功能：**
- **读取提取**：提取文本、表格、元数据
- **合并拆分**：合并多个 PDF、拆分页面
- **创建生成**：使用 reportlab 创建新 PDF
- **页面操作**：旋转、裁剪、添加水印
- **安全功能**：密码保护、加密解密
- **OCR 支持**：扫描件文字识别
- **表单填写**：填充 PDF 表单

**使用场景：**
- PDF 文档处理与转换
- 报告生成
- 文档合并与整理
- 表单自动化

**安装量：** 46.7K+ | **来源：** anthropics/skills

---

### 8. humanizer-zh (去AI化)

**功能概述：** 中文 AI 写作痕迹检测与人性化处理工具。

**主要功能：**
检测并修复以下 AI 写作模式：
- 过度强调意义与象征
- 宣传性/广告式语言
- 肤浅的 "-ing" 分析句式
- 模糊归因（"专家认为..."）
- AI 高频词汇（"此外"、"至关重要"等）
- 三段式法则滥用
- 破折号/粗体过度使用
- 表情符号滥用
- 通用积极结论

**核心原则：**
1. 删除填充短语
2. 打破公式结构
3. 变化节奏
4. 信任读者
5. 删除"金句"

**安装量：** 9.6K+ | **来源：** op7418/humanizer-zh

---

### 9. proactive-agent (主动服务)

**功能概述：** 将 AI 代理从被动执行者转变为主动合作伙伴。

**核心特性：**

**主动性：**
- 预判用户需求
- 反向提示（Reverse Prompting）
- 主动检查与提醒

**持久性：**
- WAL 协议：响应前先写入关键细节
- 工作缓冲区：捕获危险区（60%+ 上下文）的所有交互
- 压缩恢复：上下文丢失后自动恢复

**自我改进：**
- 自愈能力：自动修复问题
- 不懈努力：尝试 10 种方法后才放弃
- 安全进化：ADL/VFM 协议防止漂移

**安全加固：**
- 技能安装审查
- 外部 AI 代理网络警告
- 上下文泄露防护

**安装量：** 10.2K+ | **来源：** halthelobster/proactive-agent

---

### 10. ontology (知识图谱)

**功能概述：** 类型化知识图谱系统，用于结构化代理记忆和技能间数据共享。

**核心概念：**
- 实体：具有类型、属性和关系
- 关系：实体间的有向连接
- 约束：类型验证确保数据一致性

**支持类型：**
- **人员组织**：Person, Organization
- **工作任务**：Project, Task, Goal
- **时间地点**：Event, Location
- **信息文档**：Document, Message, Thread, Note
- **资源凭证**：Account, Device, Credential
- **元数据**：Action, Policy

**使用场景：**
- "记住..." - 创建/更新实体
- "我对 X 了解什么？" - 查询图谱
- "把 X 和 Y 关联起来" - 创建关系
- "显示 Z 项目的所有任务" - 图遍历
- 多步骤规划建模为图变换

**安装量：** 1.8K+ | **来源：** sundial-org/awesome-openclaw-skills

---

## 快速参考

| 技能 | 触发词/场景 | 安装命令 |
|------|------------|---------|
| skill-vetter | 安装新技能前审查 | `npx skills add useai-pro/openclaw-skills-security@skill-vetter -g` |
| find-skills | 搜索/安装技能 | `npx skills find <query>` |
| tavily-search | 联网搜索 | `tvly search "query" --json` |
| self-improving-agent | 自动触发/自我进化 | 自动运行 |
| csv-data-summarizer | 分析 CSV 文件 | 自动检测 CSV 文件 |
| agent-browser | 浏览器操作 | `agent-browser open <url>` |
| pdf | PDF 处理 | 自动检测 .pdf 文件 |
| humanizer-zh | 去除 AI 写作痕迹 | 编辑文本时自动应用 |
| proactive-agent | 主动服务/记忆管理 | 自动运行 |
| ontology | 知识图谱/实体管理 | `python3 scripts/ontology.py <command>` |

---

## 相关资源

- [skills.sh](https://skills.sh/) - 官方技能市场
- [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 社区技能精选
- [OpenClaw China](https://github.com/openclaw-cn) - 中文社区
