
# 1. 介绍 LLM、RAG、Agent、Memory、Retrieval、KG 等相关技术的融合
---
- [1. 介绍 LLM、RAG、Agent、Memory、Retrieval、KG 等相关技术的融合](#1-介绍-llmragagentmemoryretrievalkg-等相关技术的融合)
  - [1.1. DeepAnalyze：自主数据科学中的代理大型语言模型](#11-deepanalyze自主数据科学中的代理大型语言模型)
  - [1.2. LLM在游戏中应用的综述 https://arxiv.org/pdf/2402.18659](#12-llm在游戏中应用的综述-httpsarxivorgpdf240218659)
  - [1.3. “AgentGuide” from adongwanai](#13-agentguide-from-adongwanai)
  - [1.4. 智能体记忆的综述论文《Memory in the Age of AI Agents: A Survey》](#14-智能体记忆的综述论文memory-in-the-age-of-ai-agents-a-survey)
  - [1.5. 2025年11月13截止之前的memory 方案汇总对比](#15-2025年11月13截止之前的memory-方案汇总对比)
  - [1.6. obsidian 做个人 memory](#16-obsidian-做个人-memory)
      - [1.6.0.1. 支持哪些特殊语法？](#1601-支持哪些特殊语法)
      - [1.6.0.2. 如何形成知识图谱？](#1602-如何形成知识图谱)
      - [1.6.0.3. 具体例子说明](#1603-具体例子说明)
  - [1.7. 读论文+github 神器 deepwiki](#17-读论文github-神器-deepwiki)
  - [1.8. verl](#18-verl)
  - [1.9. pageindex](#19-pageindex)
  - [1.10. PostgreSQL == 多合一数据库：用插件替代专用数据库](#110-postgresql--多合一数据库用插件替代专用数据库)
    - [1.10.1. 官网](#1101-官网)
    - [1.10.2. 完整对应清单](#1102-完整对应清单)
    - [1.10.3. 关键插件详解（生产级选型）](#1103-关键插件详解生产级选型)
      - [1.10.3.1. 替代 InfluxDB（时序数据库）](#11031-替代-influxdb时序数据库)
      - [1.10.3.2. 替代 Milvus（向量数据库）](#11032-替代-milvus向量数据库)
      - [1.10.3.3. 替代 Neo4j（图数据库）+ pgRouting（地理路由）](#11033-替代-neo4j图数据库-pgrouting地理路由)
      - [1.10.3.4. 替代 Redis（缓存/高性能读写）](#11034-替代-redis缓存高性能读写)
      - [1.10.3.5. 替代 Elasticsearch（全文检索/搜索引擎）](#11035-替代-elasticsearch全文检索搜索引擎)
      - [1.10.3.6. 替代 MongoDB（文档数据库）](#11036-替代-mongodb文档数据库)
    - [1.10.4. 补充说明](#1104-补充说明)
  - [1.11. agent memory方向主要有2个：](#111-agent-memory方向主要有2个)
  - [1.12. 长记忆开源方案update](#112-长记忆开源方案update)
  - [1.13. Improving Language Agents through BREW](#113-improving-language-agents-through-brew)
  - [1.14. llm各种框架和论文，4000+⭐](#114-llm各种框架和论文4000)
  - [1.15. agent evolver](#115-agent-evolver)
  - [1.16. 微软 agent](#116-微软-agent)
  - [1.17. 谷歌新研究定义"充分上下文"：](#117-谷歌新研究定义充分上下文)
  - [1.18. EverMemOS](#118-evermemos)
  - [1.19. MCP 生态链接](#119-mcp-生态链接)
  - [1.20. 之后是2025年11月13之前汇总](#120-之后是2025年11月13之前汇总)
  - [1.21. 综述](#121-综述)
  - [1.22. context-labs / aella-data-explorer 1亿篇论文组成知识图谱KG](#122-context-labs--aella-data-explorer-1亿篇论文组成知识图谱kg)
  - [1.23. multi ai agent game](#123-multi-ai-agent-game)
  - [1.24. langchain 中间件](#124-langchain-中间件)
  - [1.25. todolist middleware](#125-todolist-middleware)
  - [1.26. 舆情分析](#126-舆情分析)
  - [1.27. LightMem：像人脑一样高效的记忆系统](#127-lightmem像人脑一样高效的记忆系统)
  - [1.28. llm训练](#128-llm训练)
  - [1.29. Prop RAG](#129-prop-rag)
  - [1.30. 基于多模态信息抽取的菜品知识图谱构建](#130-基于多模态信息抽取的菜品知识图谱构建)
  - [1.31. ragflow 已经支持 知识图谱](#131-ragflow-已经支持-知识图谱)
  - [1.32. flashrag](#132-flashrag)
  - [1.33. LightRAG](#133-lightrag)
  - [1.34. llm agent 综述](#134-llm-agent-综述)
  - [1.35. 谷歌 vs 微软 deepresearch](#135-谷歌-vs-微软-deepresearch)
  - [1.36. Reasoning with Sampling: Your Base Model is Smarter Than You Think](#136-reasoning-with-sampling-your-base-model-is-smarter-than-you-think)
  - [1.37. Agentic RAG新范式！天大\&小红书提出DecEx-RAG，剪枝搜索扩展提速6倍](#137-agentic-rag新范式天大小红书提出decex-rag剪枝搜索扩展提速6倍)
  - [1.38. 日报神器，记录你的一天 Dayflow](#138-日报神器记录你的一天-dayflow)
  - [1.39. 可信AI Agent相关论文(DPO)](#139-可信ai-agent相关论文dpo)
  - [1.40. Graph-Base Agent基于任务图的Agent框架](#140-graph-base-agent基于任务图的agent框架)
  - [1.41. A-Mem: Agentic Memory for LLM Agents](#141-a-mem-agentic-memory-for-llm-agents)
  - [1.42. logic rag](#142-logic-rag)
  - [1.43. LightMem](#143-lightmem)
  - [1.44. langchain graphrag](#144-langchain-graphrag)
  - [1.45. G-memory, Arcmemo, reasoning bank](#145-g-memory-arcmemo-reasoning-bank)
  - [1.46. embedding model 天梯](#146-embedding-model-天梯)
  - [1.47. MonkeyOCR](#147-monkeyocr)
  - [1.48. GitHub代码检索](#148-github代码检索)
  - [1.49. 视频转文字](#149-视频转文字)
  - [1.50. 音视频2文本](#150-音视频2文本)
  - [1.51. 爬虫数据采集圣器](#151-爬虫数据采集圣器)
  - [1.52. ai伴侣](#152-ai伴侣)
  - [1.53. metaGPT](#153-metagpt)
  - [1.54. unsloth](#154-unsloth)
  - [1.55. ai 知识库](#155-ai-知识库)
  - [1.56. 高质量rag](#156-高质量rag)
  - [1.57. ai混合搜索 meili](#157-ai混合搜索-meili)
  - [1.58. mem 推移学习，自我改进](#158-mem-推移学习自我改进)
  - [1.59. 腾讯 tree graphrag （2025年9月）](#159-腾讯-tree-graphrag-2025年9月)
  - [1.60. Graphiti vs GraphRAG 对比](#160-graphiti-vs-graphrag-对比)
  - [1.61. 自己用milvus+neo4j实现graphrag](#161-自己用milvusneo4j实现graphrag)
  - [1.62. 微软 graphRAG](#162-微软-graphrag)
  - [1.63. awesome-ai-memory 汇聚memory相关项目](#163-awesome-ai-memory-汇聚memory相关项目)
  - [1.64. es agent](#164-es-agent)
  - [1.65. MINE Context](#165-mine-context)
  - [1.66. 拼好rag](#166-拼好rag)
  - [1.67. mem0 2025年9月27日持续更新github](#167-mem0-2025年9月27日持续更新github)
  - [1.68. 蚂蚁 KAG](#168-蚂蚁-kag)
  - [1.69. 如何基于语义相似性分割文本](#169-如何基于语义相似性分割文本)
  - [1.70. 各种向量数据库对比](#170-各种向量数据库对比)
  - [1.71. 基于hnswlib的向量索引(2年前更新)](#171-基于hnswlib的向量索引2年前更新)
  - [1.72. stream vq 生成式召回](#172-stream-vq-生成式召回)
  - [1.73. ai学术搜索](#173-ai学术搜索)
  - [1.74. nlp etc.](#174-nlp-etc)
  - [1.75. 知识图谱 - 北京大学大数据分析与应用技术国家工程实验室成员，  包括各种知识图谱抽取+检索，neo4j+MongoDB等](#175-知识图谱---北京大学大数据分析与应用技术国家工程实验室成员--包括各种知识图谱抽取检索neo4jmongodb等)
  - [1.76. 唐国梁Tommy : rag + llm + es](#176-唐国梁tommy--rag--llm--es)
  - [1.77. 长文本提取结构化信息](#177-长文本提取结构化信息)
  - [1.78. 非结构化转结构化，用于微调等](#178-非结构化转结构化用于微调等)
  - [1.79. MongoDB + ES 向量存储 + 文本分割器SpacyTextSplitter （24年6月11日）](#179-mongodb--es-向量存储--文本分割器spacytextsplitter-24年6月11日)
  - [1.80. ai coding](#180-ai-coding)
- [2. ai agent 架构、新闻DIY、产品汇总](#2-ai-agent-架构新闻diy产品汇总)
  - [2.1. ai agent 架构](#21-ai-agent-架构)
    - [2.1.1. roma 等（字节aime，分析计划树agent）](#211-roma-等字节aime分析计划树agent)
    - [2.1.2. 数分+营销](#212-数分营销)
  - [2.2. 其他人 ai hub](#22-其他人-ai-hub)
  - [2.3. 令人启发的产品](#23-令人启发的产品)
    - [2.3.1. 用知识卡片，轻松建立知识体系](#231-用知识卡片轻松建立知识体系)
    - [2.3.2. 教育](#232-教育)
    - [2.3.3. 学术](#233-学术)
  - [2.4. ai agent 新闻频道](#24-ai-agent-新闻频道)
    - [2.4.1. aihub (外国日报)](#241-aihub-外国日报)
    - [2.4.2. ai 技术新闻（英国）](#242-ai-技术新闻英国)
    - [2.4.3. github ai  (外国日报论坛)](#243-github-ai--外国日报论坛)
    - [2.4.4. ai tool navigation (中国一站式)](#244-ai-tool-navigation-中国一站式)
- [3. 知名服务商](#3-知名服务商)
  - [3.1. 阿里 mem0 milvus](#31-阿里-mem0-milvus)
- [4. AI 指南 + 面试指南](#4-ai-指南--面试指南)
    - [4.0.1. 飞书文档](#401-飞书文档)
    - [4.0.2. 马士兵飞书](#402-马士兵飞书)
- [5. 基础](#5-基础)
  - [5.1. 统计学自学指南 stats-self-learning](#51-统计学自学指南-stats-self-learning)



## agent skill
https://github.com/agentskills/agentskills

核心精华技术总结
 
1. 核心定位：Claude 推出的 Agent Skills 开放标准，是 AI 代理的统一能力复用规范，解决不同平台 AI 工具需重复配置的问题，实现“写一次、多平台通用”。

2. 核心组成（4类可打包能力）：
- 自定义命令：封装高频操作（如  /format  格式化代码），简化调用；
- 专用代理：针对特定场景（代码审查、安全检查）定制角色；
- MCP 服务器：对接外部工具（数据库、API、第三方服务）；
- 钩子函数：触发自动化操作（保存时格式化、提交前跑测试）。

3. 生态与兼容性：已支持 Cursor、VS Code、GitHub 等开发工具，格式规范与参考实现开源，支持社区贡献。

4. 当前现状：生态处于起步阶段，现成 Skill 较少，跨平台兼容性需打磨，编写需基础提示词工程知识。

5. 关键资源：项目地址 https://agentskills.io，文档与示例开源于 GitHub，提供验证工具和提示词生成器。

## 25年最后总结-大模型手把手及相关开源社区

[一R]nanoGPT

40K+ 🌟，Andrej Karpathy大神出品，LLM 学习的“圣经”，最简洁的 GPT 实现，目前公认的学习 Transformer 和 GPT 架构的最佳选择。代码极度精简（核心逻辑仅约 300 行），去掉了所有复杂的工程累赘，只保留最核心的算法逻辑。

[二R]Happy-LLM

10K+ 🌟，Datawhale 社区出品，中文原生的 LLM 入门“保姆级”教程，Datawhale 出品必属精品。如果你喜欢 Hello-agents 这种中文社区风格，那么 Happy-LLM 就是算法侧的完美对应。它弥补了 nanoGPT 在全流程工程化（如微调、显存优化）上的缺失，更贴近实际应用。

[三R]LLMs-from-scratch

80K+🌟，教科书级别的代码库，真正意义上的“从零开始”。畅销书《Build a Large Language Model (From Scratch)》的配套代码库。它不是直接调库，而是带你一步步实现 Tokenizer（分词器）、Attention 模块、GPT 架构。图文并茂，代码注释非常详细。

[四R]Llama2.c / llm.c

16K+ / 30K+🌟，硬核中的硬核（非infra同学其实不用这么硬，会比较花时间），用纯 C 语言推理/训练大模型。当你觉得 Python/PyTorch 像个黑盒时，这个项目能让你看到 LLM 运行的物理本质。在不依赖庞大的 PyTorch 库的情况下，仅用一个 C 文件（几百行）就能加载并推理 Llama 2 模型。这是理解推理加速、内存管理、底层算子实现的最佳途径。如果你未来想做大模型推理优化（Inference Optimization），这是必修课。
	
💡 学习路线建议
1.  先看 nanoGPT：花一个周末，跑通代码，理解 GPT 的 Forward 过程。
2.  细读 LLMs-from-scratch：遇到不懂的数学细节，在这里找答案，补齐理论短板。
3.  实战 Happy-LLM：开始尝试微调一个中文小模型，了解全流程工程链路。
4.  挑战 llm.c：当你对性能有极致追求，或者想深入底层系统时再看。


## Manus是一款在人工智能领域具有突破性意义的通用AI智能体产品，其“厉害”之处主要体现在以下几个方面：

1.任务执行能力
Manus不仅能理解用户需求，还能自主规划并执行复杂任务，从信息收集、数据分析到生成最终成果（如报告、网页、代码等），全程无需人工干预。例如，用户只需下达“制作一份行业分析报告”的指令，Manus会自动搜索数据、整理内容、生成图表，并输出完整文档。

2.多模态与跨平台操作
它可无缝集成浏览器、代码编辑器、文件系统等工具，实现跨平台操作。能自动打开网页获取信息、编写代码处理数据，甚至部署小程序或网站，打破了传统AI工具的功能边界。

3.高效的任务拆解与执行
面对复杂任务，Manus会自动拆解为多个子步骤，按计划依次执行，并实时反馈进度。用户可像委托实习生一样，将任务交给它，专注于结果而非过程。

4.强大的上下文工程能力
通过精心设计的提示词、多Agent架构和长上下文记忆处理，Manus能深度挖掘现有大模型的能力，减少“幻觉”问题，提高输出质量和准确性。这种“上下文工程”是其核心竞争力之一。

5.商业价值与市场认可
上线仅8个月，Manus年度经常性收入突破1亿美元，累计处理数据超147万亿tokens，创建虚拟机超8000万台。其快速商业化能力证明了市场需求和用户对其实用性的认可。

6.行业影响力
Manus被Meta以数十亿美元收购，成为全球AI领域的标志性事件。它的成功推动了“通用AI智能体”赛道的崛起，促使各大巨头加速布局任务执行型AI，重新定义了AI与人类协作的边界。简言之，Manus的“厉害”在于将AI从“对话工具”升级为“生产力伙伴”，真正实现了“手脑并用”，为复杂任务提供了高效、可靠的解决方案。

## 1.1. DeepAnalyze：自主数据科学中的代理大型语言模型
[DeepAnalyze](https://github.com/DataClasse/deepanalyze)

## 1.2. LLM在游戏中应用的综述 https://arxiv.org/pdf/2402.18659

核心问题、应用领域及发展方向
 
一、核心问题
 
1. 技术局限
 
- 幻觉问题：易生成与游戏规则、剧情冲突的虚假内容（如虚构任务、错误设定）。
- 上下文与连续性：长对话或长游戏进程中易遗忘关键信息，难以维持一致性。
- 成本与实时性：消费级硬件难以并行运行大型游戏与LLM，API调用成本随用户规模递增，实时响应能力不足。
- 意图捕捉：难以准确理解讽刺、模糊指令等复杂用户输入。
 
2. 伦理挑战
 
- 版权争议：训练数据可能包含受版权保护的游戏内容，生成内容的版权归属不明确。
- 可持续性：LLM推理过程碳足迹较高，大规模应用时环境影响显著。
- 偏见与毒性：训练数据中的社会偏见可能导致不当输出，需防范毒性语言。
- 透明度与隐私：闭源LLM生成逻辑不可解释，用户交互数据存在泄露风险。
 
二、应用领域
 
1. 游戏内场景
 
- 玩家角色：适配棋盘游戏、文本冒险游戏、支持API的开放世界游戏（如Minecraft）。
- NPC交互：前景NPC（推进主线）、背景NPC（营造氛围），提供动态对话与沉浸体验。
- 玩家辅助：教程提示、琐碎任务自动化、角色“内心独白”互动。
- 游戏主持：驱动TTRPG等游戏的剧情生成与玩家互动。
- 核心机制：以LLM为核心玩法（如元素合成、故事共创、密码破解）。
 
2. 游戏开发场景
 
- 自动化设计：生成关卡、谜题、叙事内容、游戏代码。
- 设计辅助：概念 brainstorming、内容迭代优化、素材生成（如卡牌设计、概念艺术）。
- 数据分析：玩家行为聚类、游戏日志分析、 gameplay相似性识别。
 
3. 衍生场景
 
- 评论与叙事：游戏直播实时解说、过往游戏会话总结与叙事重构。
 
三、发展方向
 
1. 强化人机协同设计：推动LLM从“单向生成”转向“推理-迭代”的共创模式，提升设计适配性与一致性。
2. 拓展玩家助手功能：开发个性化教程、复杂任务自动化、游戏规则实时解读等实用场景，结合外部数据库减少幻觉。
3. 深化评论与叙事能力：探索基于观众互动的直播辅助解说、开放世界动态剧情总结等创新方向。
4. 优化玩家建模：通过LLM分析多模态数据预测玩家情绪与沉浸度，实现体验驱动的内容生成。
5. 技术瓶颈突破：重点解决幻觉控制、长上下文管理、低成本实时运行等问题，推进本地部署与模型轻量化。
6. 建立伦理规范：明确版权归属，优化训练数据以减少偏见，提升模型透明度与用户数据安全性。


## 1.3. “AgentGuide” from adongwanai
https://github.com/adongwanai/AgentGuide

该仓库“AgentGuide”由 adongwanai 创建，主要内容是 AI Agent 开发与大模型相关的知识与实战资料。核心包括：

- AI Agent 开发指南
- LangGraph 实战教程
- 高级 RAG（检索增强生成）
- 大模型转行经验与面试指南（算法工程师/大模型岗位/面试题库）
- 强化学习和数据合成

特色标签涵盖 ai-agent、llm、interview、multi-agent、rag 等内容。仓库包含丰富的实战和教程，对想了解和进入 AI 大模型与 Agent 方向有很大价值。

## 1.4. 智能体记忆的综述论文《Memory in the Age of AI Agents: A Survey》

核心围绕智能体记忆的形式、功能、动态机制三大维度展开，系统梳理了当前研究现状并指明未来方向。
 
核心内容总结
 
1. 概念界定与区分
 
- 明确智能体记忆（Agent Memory）的定义：支撑智能体长期推理、持续适应和复杂环境交互的核心能力，区别于LLM内存（侧重模型内部KV缓存等）、RAG（侧重静态知识检索）、上下文工程（侧重资源优化）。
- 指出传统长/短期记忆分类的局限性，提出“形式-功能-动态”三位一体的统一分析框架。
 
2. 记忆的三大形式（Forms）
 
- 令牌级记忆（Token-level）：离散可访问的显性存储（如文本片段、知识图谱），分扁平（1D）、平面（2D，如图表）、分层（3D，如金字塔结构）三类，优势是透明可编辑，适用于多轮对话、推荐系统等。
- 参数级记忆（Parametric）：存储于模型参数中，分内部参数（直接微调模型权重）和外部参数（如LoRA模块），适用于领域知识固化、角色一致性维持。
- 潜态记忆（Latent）：隐式存储于模型隐藏态（如KV缓存、嵌入向量），分生成型、复用型、转换型，优势是高效低延迟，适用于多模态融合、边缘部署。
 
3. 记忆的三大功能（Functions）
 
- 事实记忆（Factual）：存储用户偏好、环境状态等显性知识，保障交互一致性与个性化，分用户事实记忆（如对话连贯性）和环境事实记忆（如知识库持久化）。
- 经验记忆（Experiential）：沉淀任务执行中的过程性知识，支持持续学习，分案例级（原始轨迹）、策略级（推理模板）、技能级（可执行代码/API）。
- 工作记忆（Working）：任务执行中的临时上下文管理，分单轮（输入压缩、观察抽象）和多轮（状态整合、分层折叠），解决上下文窗口有限问题。
 
4. 记忆的动态机制（Dynamics）
 
- 生命周期三阶段：形成（Formation）（从原始数据提取有用信息，如语义摘要、结构化构建）、演化（Evolution）（整合新记忆，含巩固、更新、遗忘机制）、检索（Retrieval）（含触发时机、查询构建、策略选择、结果优化）。
 
5. 资源与前沿方向
 
- 整理了记忆相关基准测试（如MemBench、LongMemEval）和开源框架（如MemGPT、Mem0、Zep）。
- 指出未来前沿：自动化记忆设计、强化学习与记忆深度融合、多模态记忆、多智能体共享记忆、记忆可信度（隐私、可解释性、抗幻觉）。
 
核心结论
 
智能体记忆已从静态存储演进为动态、可学习、多形式融合的核心认知组件，未来需打破现有碎片化研究，推动记忆成为智能体设计的“一等公民”，支撑AGI所需的长期适应与自主进化能力。

## 1.5. 2025年11月13截止之前的memory 方案汇总对比
- **AI Memory 项目完整对照表**
- 一、🔥开源记忆框架推荐
  - 1 MemOS
    - 团队：记忆张量 + 上海交大等
    - 类型：记忆操作系统
    - 核心：三层架构 + 记忆调度
    - 特点：工业级标准化封装（MemCube）
    - 性能：准确率提升 38.97%，Token 消耗降低 60.95%
    - 适用场景：企业级生产环境
    - 发布时间：2025 年 7 月
  - 2 Mem0
    - 团队：YC 支持创业公司
    - 类型：混合存储框架
    - 核心：向量 + 键值 + 图存储
    - 特点：响应 1.44 秒，7k tokens/对话
    - 适用：企业多场景应用
    - Stars：22k+
  - 3 Zep (Graphiti)
    - 团队：YC 2024 冬季批次
    - 类型：时序知识图谱
    - 特点：关系追踪准确率 94.8%，DMR 基准 98.2%
    - 场景：复杂多会话关系管理
  - 4 Letta (MemGPT)
    - 来源：UC Berkeley
    - 特点：分层内存 + 可视化 ADE 界面
    - 适用：学术与代理框架开发
  - 5 Cognee
    - 特点：图 + 向量混合架构，ECL 知识管道
    - 准确率：92.5%（优于传统 RAG）
    - 适用：知识密集型场景
  - 其他代表：
    - LangMem（LangChain 官方 SDK）
    - Memoripy（人类记忆模拟）
    - Memori（企业集成引擎）
    - Memory（图数据库驱动）
    - Julep AI（AI 工作流平台）
- 二、🧠 MCP 记忆服务器生态
  - 1 OpenMemory MCP（Mem0 官方）
    - 技术：本地优先 + 标准化 API
    - 优点：完全离线、零云同步
    - 场景：隐私敏感场景、跨工具协作
  - 2 Supermemory MCP
    - 支持跨 LLM 平台共享记忆
    - 场景：ChatGPT、Claude、Gemini 混合使用者
  - 3 CaviraOSS OpenMemory
    - 优点：速度提升 2-3 倍，成本降低 6-10 倍
    - 场景：性能优先的企业环境
  - 4 Basic Memory
    - 存储：Markdown + 知识图谱
    - 优点：兼容 Obsidian
    - 适用：个人知识管理
- 三、🏢 商业产品的记忆功能
  - ChatGPT Memory（OpenAI）
    - 自动预加载 + 时间戳记忆
    - 跨对话持久保存
    - 用户可随时删除
    - ✅ 全量开放中
  - Claude Memory（Anthropic）
    - 工具调用 + 原始对话引用
    - 团队版增强，安全测试完善
  - Gemini Memory（Google）
    - 功能未完全上线，仍在测试中
- 四、💻 桌面与独立应用
  - Memorr.ai
    - 平台：Mac / Windows
    - 技术：RAG + 可视化记忆画布
    - 特点：永久记忆、本地加密
    - 场景：长对话用户
- 五、🎓 学术研究与创新架构
  - Memory Taxonomy 2025（爱丁堡大学+港中文）：三大记忆分类与六种操作
  - 3DLLM-MEM（UCLA+Google）：3D 环境长时记忆，用于机器人
  - MIRIX（UCSD+NYU）：多模态多智能体记忆系统
  - Larimar：大脑启发架构，分布式情景记忆
  - MemoryOS（北邮团队）：三级分层记忆架构
- 六、📊 评估基准
  - LoCoMo（ACL 2024）：长期对话记忆
  - LongMemEval：时序推理能力测试
  - DMR（MemGPT 团队）：多会话深度记忆检索
- 七、🧩 技术架构对比
  - 架构类型对比：
    - 向量检索：高效快速
    - 图数据库：关系建模最强
    - 混合架构：性能平衡
    - 操作系统级：调度优化显著
    - 代理框架型：灵活度高
  - 代表项目：
    - Mem0（混合）
    - Zep（图时序）
    - MemOS（系统级）
    - Cognee（混合）
    - Letta（代理框架）
- 八、🧭 选择建议矩阵
  - 个人助手：ChatGPT Memory / Claude Memory
  - 专业开发：LangMem / Cognee / Mem0
  - 企业生产：MemOS / Zep / Memori
  - 隐私场景：OpenMemory MCP / Memoripy
  - 跨工具协作：Supermemory MCP
  - 复杂工作流：Julep AI
  - 学术研究：Letta (MemGPT)
- 九、🚀 性能数据对比（简化版）
  - MemOS：准确率 +38.97%，Token -60.95%
  - Cognee：准确率 92.5%
  - Zep：DMR 98.2%
  - Mem0：LoCoMo 68.5%，响应 1.44s
  - OpenMemory (CaviraOSS)：2-3 倍更快，6-10 倍成本优势
- 十、🔗 集成生态对比
  - LangChain / LangGraph / CrewAI / AutoGen / MCP
  - ✅ MemOS、Mem0、Zep、Cognee、LangMem 均深度集成 LangChain
  - ✅ OpenMemory、Supermemory 专注 MCP 生态
- 十一、📂 数据存储架构
  - MemOS：全栈（向量+图+关系+键值）
  - Zep / Cognee / Memory：图+向量混合
  - Memori：SQLite 本地轻量方案
  - Basic Memory：Markdown 文件存储
- 十二、⚖️ 开源协议与商业模式
  - Apache 2.0：Mem0, Zep, Cognee, Letta, Julep
  - MIT：LangMem, Memoripy
  - 商业版：MemOS, Memori
  - 云服务支持：Mem0, Zep, Julep
- 十三、📈 技术趋势总结（2025）
  - 1 架构趋势：图 + 向量混合成主流，记忆系统操作系统化
  - 2 标准化：MCP 成为事实标准
  - 3 隐私优先：数据主权与本地控制成刚需
  - 4 性能优化：Token 成本降低 60%，速度提升 3 倍
  - 5 生态融合：LangChain / LangGraph / MCP 多平台互通
- 十四、🌳 快速选择指南
  - 想要“零配置”：选 ChatGPT Memory
  - 追求隐私安全：选 Memoripy / Basic Memory
  - 开发实验：选 LangMem / Cognee / Mem0
  - 企业生产：选 MemOS / Zep / Memori
  - 跨工具协作：选 Supermemory MCP
  - 工作流自动化：选 Julep AI

## 1.6. obsidian 做个人 memory
设计思路和项目地址：
https://github.com/kingkongshot/prompts/blob/refs%2Fheads%2Fmain/prompts%2Fclaude%2Fagents%2Fmemory-network-builder.md


memory-network-builder 生成和使用方法总结：

一、怎么生成的？
memory-network-builder 是为组织和建立记忆（知识）网络而设计的模板/Agent规范。它的生成流程为：

1. 遇到新的信息、决策或学习时，由用户或系统触发。
2. 由专门的 Memory Network Architect 负责，根据内容提炼核心结论。
3. 确定记忆类型（决策decision、实现implementation、学习learning、概念concept、问题issue）。
4. 起一个结论式的中文标题。
5. 用规定的 Markdown 格式描述，结构包含 id、type、title、created（日期）、tags、上下文链接、核心内容和关键文件等。
6. 维护与其他记忆之间的关系（通过[[memory-id]]格式链接）。
7. 每条记忆（Memory Unit）单独存储于项目根目录的 memory/ 文件夹下，文件名为标题+ .md。

二、怎么使用的？
1. 日常项目中遇到新决策、新问题、新经验时，按照规范提炼为独立记忆。
2. 根据类型分类，起标题、填写内容。
3. 结构化存储，及时补全与上下文（其他记忆）之间的关联。
4. 推动团队形成“知识原子化+网状关联式”存档，便于知识追溯、复用与演化。

三、具体例子：如何运作

假设项目中遇到一个新结论：团队决定“使用 JWT 而不是 Session 做认证”。

操作流程与输出：

1. 提炼结论：用 JWT 替代 Session。
2. 类型判定：decision（决策类）。
3. 起标题：“使用 JWT 而不是 Session 做认证”
4. 生成 id：“use-jwt-for-auth”
5. 填写 Markdown：

```markdown
---
id: use-jwt-for-auth
type: decision
title: 使用 JWT 而不是 Session 做认证
created: 2025-12-18
tags: [authentication, jwt, session, security]
---

### 例子：使用 JWT 而不是 Session 做认证

#### 一句话说明
> 认证系统决定采用 JWT，舍弃传统 Session，实现跨服务无状态登录。

## 上下文链接
- 基于：[[auth-requirements]]
- 导致：[[jwt-auto-refresh-issue]]
- 相关：[[session-storage-comparison]]

#### 核心内容
选择 JWT 的原因包括：便于微服务架构下无状态扩展，客户端可自持 Token，减少服务端状态保存压力。分析过程中权衡了安全性和易用性，最终做出此结论。

#### 关键文件
- `src/auth/jwt.ts` - 认证实现
- `docs/auth.md` - 认证设计文档
```

6. 存到 memory/使用 JWT 而不是 Session 做认证.md

最终，整个团队可以通过浏览 memory 文件夹和记忆间的网状链接，迅速理解历史决策、概念和实现细节，避免重复思考和知识丢失。

结果是什么？
- 项目沉淀了结构化、易检索、强关联的知识网络。
- 新成员容易快速接手项目，追溯历史决策。
- 知识以“原子结论”为单位，便于持续演化和推理。


Obsidian 支持大部分 语法memory-network-builder 模板中的“特殊语法”，并且可以用于构建知识图谱。下面详细说明：

#### 1.6.0.1. 支持哪些特殊语法？

- **YAML Frontmatter（如 `--- ... ---`）**  
  Obsidian 可以识别每条 Memory 最上方的 YAML 区块，便于后续做属性查询和自动化管理。

- **Markdown 标准语法**  
  memory-network-builder 的内容均为标准 Markdown 格式，Obsidian 100% 支持。

- **双中括号链接 `[[xxx]]` （Wiki Link）**  
  Obsidian 的核心功能之一。  
  - 能直接创建页面之间的链接，通过 `[[前置的决策或概念]]`、`[[相关内容]]` 让知识节点之间互相关联。
  - 支持未创建页面的“悬挂链接”，日后可补充完善。

- **标签（tags 字段或 `#标签`）**  
  Obsidian 支持标签，可以用来聚合和检索相关主题内容。

#### 1.6.0.2. 如何形成知识图谱？

- Obsidian 自动分析所有内部链接（即 [[xxx]] 这种格式）并生成“知识图谱”视图。  
- 在 Obsidian 中打开 Graph View，就可以可视化展示所有页面的关联关系，以及哪些内容链接到了共同的节点。
- 只要每条 Memory 都按照模板规范、写好 Frontmatter、填写链接，Obsidian 会自动把它们组织成网状结构，方便导航和溯源。

#### 1.6.0.3. 具体例子说明

假设你有三条 Memory：
- [[使用 JWT 而不是 Session 做认证]]
- [[JWT 自动刷新机制设计]]
- [[认证系统的性能问题]]

它们互相之间像这样链接：

A 的上下文链接里 `导致：[[JWT 自动刷新机制设计]]`  
B 的相关里 `相关：[[认证系统的性能问题]]`

在 Obsidian 的 Graph View 里，你会看到这三条知识像网络一样连在一起，从 A 延伸到 B，再指向 C。点击任一节点，可以很快跳转、上下深度浏览相关结论。

---

**总结**  
只要严格采用 memory-network-builder 的 Markdown 模板，Obsidian 就能完美兼容，并借助其强大的图谱能力，实现高效的知识关联和网络化沉淀。



## 1.7. 读论文+github 神器 deepwiki
首页： [deepwiki](https://deepwiki.com/)

## 1.8. verl
[verl](https://mp.weixin.qq.com/s/KllfYqWI5ljqd1YtPEViTA)

- 定位：veRL（Volcano Engine Reinforcement Learning）是字节跳动火山引擎于 2024 年底开源的分布式大模型强化学习训练框架。其设计目标是将 RLHF 的科研实现转化为可规模化部署的生产级系统。
- 核心功能：veRL 的核心模块包括 Rollout 生成器、奖励建模器、策略更新器、分布式调度器。它支持多种算法，如 PPO、DPO、DAPO （Dynamic Alignment Policy Optimization）和 GRPO，并通过异步管线方式加速训练。其架构借鉴了工业级 RL 系统（如 DeepMind Acme、OpenAI RLHF pipeline），可在数百张 GPU 上同时运行。
- 技术特点与用途：veRL 面向企业和研究机构的“大规模模型后训练”场景。其分布式框架支持任务并行、异步更新和奖励缓存机制，可显著降低 GPU 闲置率。其 DAPO 算法被广泛用于 Qwen 系列模型中，以优化推理稳定性与语言一致性。

##  1.9. pageindex
地址：https://github.com/VictifyAl/PageIndex

在处理专业长文档时，传统基于向量的检索增强生成（RAG）系统依赖语义相似性，而非真正的相关性。然而，相似性并不等同于相关性，我们在检索中真正需要的是相关性，而这需要推理。为了解决这一问题，VectifyAI 推出了 PageIndex，一个基于推理的 RAG 系统，它能为长文档构建树状索引，并通过该索引进行检索。



## 1.10. PostgreSQL == 多合一数据库：用插件替代专用数据库
### 1.10.1. 官网
- [postgres新功能 ai ](https://supabase.com/blog/postgres-new)
- [postgres chat db](https://database.build/)
- [postgres 新功能 ai 集成](https://blog.adyog.com/2024/09/14/exploring-postgres-new-in-browser-postgres-with-ai-integration/)
- [rag-memory with postgresql + neo4j](https://pypi.org/project/rag-memory/)

PostgreSQL 凭借丰富的插件生态，能够一站式替代时序数据库、向量数据库、图数据库、缓存、搜索引擎、文档数据库等多种专用数据库。以下是精准的插件对应关系补全，兼顾功能匹配度和生产级可用性：

### 1.10.2. 完整对应清单
替代数据库      | 插件 （索引）                                         | 说明    
----------------|--------------------------------------------------|------------------------------
**InfluxDB** |  (TimescaleDB / BRIN)                                 | 时序数据库：TimescaleDB（官方核心时序插件） + BRIN（轻量级时序索引）
**Milvus** |  (pgvector)                                            | 向量数据库：pgvector（PostgreSQL官方生态向量插件）
**Neo4j** |  (pgRouting + pg_graph)                                 | 图数据库/空间路由：pgRouting（地理路由）+ pg_graph（原生图处理）
**Redis** |  (pg_repack + pg_cron + redis_fdw)                      | 缓存/定时任务：redis_fdw（Redis双向访问）+ pg_repack（数据优化）+ pg_cron（定时任务）
**SQL** |  (原生PostgreSQL = B-Link树 )                               | 关系型SQL：PostgreSQL原生SQL引擎（兼容SQL:2016）：B-Link树索引 数字文本
**Elasticsearch** |  (PGroonga + pg_bigm + tsvector/tsquery / GIN)  | 搜索引擎：PGroonga（全文检索）+ pg_bigm（模糊匹配）+ 原生tsvector（文本索引） + GIN（通用索引）
**MongoDB** |  (jsonb + pg_json_schema + mongodb_fdw)                 | 文档数据库：jsonb（原生JSONB类型）+ pg_json_schema（JSON校验）+ mongodb_fdw（MongoDB互通）
**定时任务数据库** |(pg_cron + pg_timetable + pgAgent + pg_jobmon)      | 定时任务/调度数据库 ：pg_cron（轻量级定时任务）+ pg_timetable（复杂调度）+ pgAgent（图形化调度）+ pg_jobmon（任务监控）
**地理位置** |(GIST)                                                  | 地理位置索引：GIST（通用空间索引），支持点、线、多边形等空间数据，可与pgRouting等插件配合使用。


### 1.10.3. 关键插件详解（生产级选型）
#### 1.10.3.1. 替代 InfluxDB（时序数据库）
- **核心插件**：`TimescaleDB`  
  官方专为PostgreSQL打造的时序数据库扩展，支持自动分区、数据保留策略、时序聚合函数（如time_bucket），完全对标InfluxDB的时序场景（物联网、监控指标等）。

#### 1.10.3.2. 替代 Milvus（向量数据库）
- **核心插件**：`pgvector`  
  目前最成熟的PostgreSQL向量插件，支持向量存储、余弦/欧氏/内积相似度计算，兼容OpenAI等大模型Embedding向量，性能接近Milvus，且可与关系数据联动。

#### 1.10.3.3. 替代 Neo4j（图数据库）+ pgRouting（地理路由）
- **图处理**：`pg_graph`（PostgreSQL 14+原生图类型） + `age`（Apache AGE，兼容Cypher查询语言）  
- **地理路由**：`pgRouting`（经典插件，支持最短路径、TSP等地理路由算法，替代Neo4j的空间路由能力）

#### 1.10.3.4. 替代 Redis（缓存/高性能读写）
- **缓存互通**：`redis_fdw`（Foreign Data Wrapper，实现PostgreSQL与Redis双向数据访问）  
- **高性能读写**：`pg_prewarm`（数据预热到内存） + `pg_stat_statements`（性能监控）  
- **定时任务**：`pg_cron`（替代Redis的定时任务能力）

#### 1.10.3.5. 替代 Elasticsearch（全文检索/搜索引擎）
- **核心插件**：`PGroonga`（基于Groonga的高性能全文检索，支持中文分词、模糊匹配、高亮）  
- **轻量替代**：PostgreSQL原生`tsvector/tsquery`（文本索引） + `pg_bigm`（双字符索引，优化中文模糊查询）  
- **分布式检索**：`Citus`（分库分表）+ PGroonga（分布式检索）

#### 1.10.3.6. 替代 MongoDB（文档数据库）
- **核心能力**：PostgreSQL原生`jsonb`类型（支持索引、嵌套查询、JSON操作符）  
- **增强插件**：  
  - `pg_json_schema`（JSON Schema校验，替代MongoDB的文档校验）  
  - `mongodb_fdw`（MongoDB数据接入PostgreSQL）  
  - `jsonb_plpython`（自定义JSON处理函数）

### 1.10.4. 补充说明
1. **原生能力优先**：PostgreSQL的jsonb、tsvector、地理信息（PostGIS）等原生功能已覆盖大部分专用数据库场景，插件仅作增强；
2. **生产兼容性**：上述插件均为社区成熟方案，TimescaleDB、pgvector、PGroonga等已在企业级场景大规模落地；
3. **优势**：PostgreSQL通过插件实现“一站式”数据存储，避免多数据库同步的复杂度，同时保留SQL的通用性和事务一致性。



## 1.11. agent memory方向主要有2个：
```
模型驱动：深入模型底层动刀，从根本上增强其记忆能力。
应用驱动：在应用层搭建即插即用的记忆框架。
.
✅针对这两大方向做了完整整理，以一些比较核心的工作举例。
.
⭕模型驱动——深入骨髓的记忆改造 (5个典型工作)
这一方向主要是直接改造大模型，让模型“天生”就拥有更强的记忆力。优点是性能上限高，缺点是研发成本高、周期长。
1️⃣Memorizing Transformers (Google, 2022): 融合外部记忆（KNN查找）与内部注意力，让模型能边思考边“翻书”。
2️⃣MemoryLLM (清华, 2024): 在模型每层嵌入可读写的 "memory tokens"，像给大脑装了内置“草稿纸”。
3️⃣Memory³ (记忆弧量, 2024): 首次提出记忆分层框架，模拟人脑对记忆进行分层管理，让记忆组织更有条理。
4️⃣WISE (浙大, 2024): 提出“主记忆+侧记忆”双参数体系，面向终身学习和模型编辑。
5️⃣Titans (Google, 2025): 提出一个专用的神经网络模块，自主学习何时存储、何时遗忘。
.
⭕应用驱动——即插即用的记忆外挂 (5个典型工作)
这一方向偏向不动模型本身，在应用层构建记忆系统。优点是落地快、易扩展，缺点是受限于底层模型的能力。
1️⃣MemGPT (2023): 将LLM视为一个操作系统，通过虚拟上下文管理技术，赋予Agent无限上下文能力。
2️⃣Mem0 (2024): 一个为生产环境设计的通用记忆层，强调平台化服务与可扩展性。
3️⃣Zep (2024): 采用时序知识图谱（Temporal Knowledge Graph）来组织长期记忆，使记忆检索和理解更深刻。
4️⃣Memobase (2025): 基于用户画像（Profile）和事件（Event）构建长期记忆，能自动从对话中抽取结构化信息。
5️⃣HippoRAG (OSU等, 2024): 灵感源于神经生物学，模拟海马体的记忆形成机制。
```

## 1.12. 长记忆开源方案update
graphiti是主要做图。 [graphiti 播客](https://www.cnblogs.com/zzz77zz/articles/19026839)

memobase主要为了陪伴和个人助手场景设计

Memobase最近支持了event功能，可以记录用户记忆变动的时间发生顺序.
	
结合完全可定制的二级标签系统，大家可以使用memobase profile和event构建出灵活的长记忆AI

Memobase的时间记忆（temporal memory）居然领先  mem0, langmem, zep...


## 1.13. Improving Language Agents through BREW


微软：“经验”酿成“知识”让智能体聪明

BREW：把“经验”酿成“知识”——让语言智能体越用越聪明
问题 大模型智能体每次任务都从“零”开始，重复探索、API 冗余；权重级优化（PPO/GRPO）代价高、黑盒且难增量更新。

思路 不碰模型权重，而是持续蒸馏轨迹经验，构建可解释、模块化、可检索的知识库（KB），把“记忆”变成显式、可控的优化杠杆。

技术路线

Reflector-Agent：用人类规则+任务评分从轨迹中提取「概念-洞察」对，语义去重后得到元概念集合。
Integrator-Agent：为每个元概念维护独立文档，形成分区式 KB，支持精准更新与检索。

Expand-and-Gather MCTS：把 KB 精炼视为「文档状态空间搜索」，并行探索、全局同步，兼顾正确性与可检索性双目标奖励。
推理阶段：top-k 检索注入 prompt，零额外训练成本。

结果 在 OSWorld、τ²-Bench、SpreadsheetBench 三大真实环境上，任务成功率绝对提升 10–20 %，执行步数/对话轮次减少 10–15 %，计算开销与基座模型持平，显著优于现有记忆基线。
意义 首次将“智能体优化”转化为“可解释 KB 的状态搜索”，提供轻量、透明、可扩展的新范式，为长周期、高一致性、可审计的自主系统奠定基础。

## 1.14. llm各种框架和论文，4000+⭐
https://github.com/DSXiangLi/DecryptPrompt/blob/refs%2Fheads%2Fmain/%E5%BC%80%E6%BA%90%E6%A1%86%E6%9E%B6.MD
## 1.15. agent evolver
阿里通义实验室推出的AgentEvolver开源项目，能让AI智能体在闲置时自主生成任务、执行并进化。项目链接：https://github.com/modelscope/AgentEvolver


## 1.16. 微软 agent
https://github.com/microsoft/Generative-AI-for-beginners-dotnet/blob/refs%2Fheads%2Fmain/translations%2Ftw%2FREADME.md


##  1.17. 谷歌新研究定义"充分上下文"：
上下文需能推导出答案而非仅相关。发现即使上下文充足，大模型仍有14%-25%错误率。提出选择性生成框架，使模型准确率提升2-10%。

谷歌团队发表在ICLR 2025的新研究《Sufficient Context: A New Lens on Retrieval Augmented Generation Systems》，首次提出「充分上下文」（Sufficient Context）的核心概念，为这个行业痛点提供了全新解法，甚至能让Gemini、GPT等主流模型的正确回答率提升2-10%。

论文地址：https://arxiv.org/pdf/2411.06037

项目地址：https://github.com/hljoren/sufficientcontext

## 1.18. EverMemOS
陈天桥团队发布了EverMemOS，这是个开源的AI"记忆增强器"。它让AI告别"金鱼脑"，能长期记住信息、连贯思考，真正理解上下文。

EverMemOS深度整合MCP作为核心接口层，实现Cursor和Claude等工具间的记忆同步。比如能自动关联你上周查过的资料，这才是真正的"持久灵魂"，配置指南在GitHub仓库就能找到。


## 1.19. MCP 生态链接
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)


## 1.20. 之后是2025年11月13之前汇总

## 1.21. 综述
《Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG》

## 1.22. context-labs / aella-data-explorer 1亿篇论文组成知识图谱KG
https://github.com/context-labs/aella-data-explorer#:~:text=Interactive%20visualization%20and%20exploration%20of%20scientific%20papers%20from,project%20is%20a%20collaboration%20between%20Inference.net%20and%20LAION.

## 1.23. multi ai agent game
https://mp.weixin.qq.com/s/b005axpuXFno5h7gfC5DMg

## 1.24. langchain 中间件
https://langchain-doc.cn/v1/python/deepagents/middleware.html#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E4%B8%AD%E9%97%B4%E4%BB%B6

## 1.25. todolist middleware
https://deepwiki.com/langchain-ai/deepagents/2.5-planning-with-todolistmiddleware

https://deepwiki.com/search/todolisttodolistagentagenttodo_6c3c8606-7ea0-421a-bb06-9f62292b31ff

## 1.26. 舆情分析
Agent自动生成舆情报告！ 项目地址：https://gitee.com/SeniorAgentTeam/bettafish-stock.git 不到两周狂揽2万Star的开源舆情分析平台，只需输入一句话，智能体就能自动爬取全网数据（微博、知乎、GitHub、抖音、小红书、官媒等），最后由Report Agent生成完整分析报告。 报告内容包含舆情发展脉络、传播分析、风险评估与应对策略，自动导出PDF。 

其中的5个智能体分工如下：

1. Insight Engine：负责私有数据库挖掘，处理企业内部业务数据，实现公私域数据融合

2. Media Engine：专注多模态内容分析，爬取抖音/快手/小红书的视频图文，还能解析搜索引擎中的天气卡、日历卡、股票卡等结构化信息

3. Query Engine：执行精准信息搜索，覆盖微博/知乎/GitHub等13+社媒平台，广泛采集用户评论和公开舆情

4. Forum Engine：担任"辩论主持人"，协调各Agent进行链式思维碰撞，避免单一模型局限

5. Report Engine：整合所有数据生成最终报告，包含舆情脉络、传播分析、风险评估等完整框架

这套系统通过五方协作，实现了从数据采集到深度分析的全流程自动化。

## 1.27. LightMem：像人脑一样高效的记忆系统
https://dailypapers.org/paper/2510.18866
	
🧠 核心方法
LightMem采用三阶段架构：
- 感官记忆： 轻量级压缩和主题过滤，快速去除冗余信息。
- 短期记忆： 主题感知整合，生成更结构化的记忆单元。
- 长期记忆： 引入“睡眠时间更新”机制，将昂贵的记忆维护操作解耦到离线并行执行，大幅降低在线延迟。

## 1.28. llm训练
必读系列，Huggingface 出品的 LLM 训练手册非常详细的介绍了完整的 LLM 训练流程，包括训练指南（是否需要预训练）、预训练、后训练、基础设施

主要以他们自己训练的 SmolLM3 这个 3B 模型为例子

手册包含了他们训练模型过程中对一系列决策、发现和死胡同的梳理，全是实践经验。

https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook

## 1.29. Prop RAG 
https://github.com/ReLink-Inc/PropRAG
核心创新：以"命题"为基础知识单元，通过无LLM的在线束搜索实现高效多跳推理
技术特点：
- 命题知识单元：将文档分解为语义丰富的命题，作为检索和推理的基本单位
- 束搜索算法：采用高效的束搜索在命题路径上进行多步推理，无需在线调用LLM
- 推理路径发现：能够自动发现和构建多步推理链，支持复杂问题解答

## 1.30. 基于多模态信息抽取的菜品知识图谱构建
https://tech.meituan.com/2024/05/17/cross-modal-ingredient-level-dataset.html

## 1.31. ragflow 已经支持 知识图谱
Construct knowledge graph

https://ragflow.io/docs/dev/construct_knowledge_graph

## 1.32. flashrag     
人大开源

https://github.com/RUC-NLPIR/FlashRAG

## 1.33. LightRAG
港大团队开源LightRAG：知识图谱+双层检索，复杂问答准确率飙升30%

LightRAG的主要优势包括：

- 高效的知识图谱构建：LightRAG通过图结构差异分析实现增量更新算法，显著降低了计算开销，使知识库维护更加高效。
- 双层检索机制：该系统结合了低层次（具体实体和属性）和高层次（广泛主题和概念）的检索策略，满足了不同类型的查询需求，提高了检索的全面性和多样性。
- 快速适应动态数据：LightRAG能够在新数据到来时快速整合，无需重建整个知识库，确保系统在动态环境中保持高效和准确。

LightRAG和GraphRAG的核心差异在于架构效率：GraphRAG依赖重型社区结构（单次检索耗61万token），而LightRAG用轻量图谱+双层检索（仅需百级token）。实验显示在法律数据集上，LightRAG以52.8%胜率小幅领先，多样性指标达73.6%碾压对手，且支持增量更新——用图谱的深度配合向量的速度，这才是生产环境该有的样子。


LightRAG用轻量图谱解决RAG语义碎片化问题。它通过实体关系提取和双层检索（既查具体实体又抓宏观关联），兼顾图谱深度与检索速度。相比传统扁平RAG，能挖掘数据间隐含因果链；相比GraphRAG，成本显著降低（检索仅需<100 token vs 61万）、支持增量更新。在法律等复杂领域胜率达52.8%，多样性73.6%。这种平衡使它更适合需频繁更新数据的实际业务场景，尤其适合既要精度又要效率的工业级应用。

https://link.zhihu.com/?target=https%3A//github.com/HKUDS/LightRAG

https://zhuanlan.zhihu.com/p/1892140189524156837

## 1.34. llm agent 综述
https://hustai.github.io/zh/posts/reasoning/LATS.html

## 1.35. 谷歌 vs 微软 deepresearch
 https://mp.weixin.qq.com/s/e_1dGQRLfc_fGAZrQEsLVw
## 1.36. Reasoning with Sampling: Your Base Model is Smarter Than You Think
哈佛团队的"Power Sampling"方法很妙：只需改变基座模型的采样分布（从常规改为幂分布），就能大幅提升推理能力。它不依赖强化学习、无需额外训练，连校验器都不用，却让Qwen2-5-Math-7B模型在数学任务准确率从49.6%跃升至74.8%，编程任务更是从21.3%飙升到73.2%——不仅逼近强化学习效果，还避免了多样性坍缩问题。这证明基础模型本身已蕴含强大推理潜力，只是被传统采样方式束缚住了。

## 1.37. Agentic RAG新范式！天大&小红书提出DecEx-RAG，剪枝搜索扩展提速6倍

## 1.38. 日报神器，记录你的一天 Dayflow
项目地址是
 https://github.com/JerryZLiu/Dayflow

，展示了这个开源日报工具

##  1.39. 可信AI Agent相关论文(DPO)

[打造可信AI Agent：如何让智能体不跑偏、不越界，安全又靠谱如何让 Agent 在开放环境、长序列决策与多工具协作中 - 掘金](https://juejin.cn/post/7564246560847052842)


[迈向可信AI Agent：Jeddak AgentArmor意图对齐与约束遵循方案 - 今日头条](https://www.toutiao.com/article/7561503362732065289/?upstream_biz=doubao&source=m_redirect)


[为 AI Agent 行为立“规矩”——字节跳动提出 Jeddak AgentArmor 智能体安全框架 - 今日头条](https://www.toutiao.com/article/7543322896609919528/?upstream_biz=doubao&source=m_redirect)

## 1.40. Graph-Base Agent基于任务图的Agent框架
本文提出图基智能体规划（GAP）框架，突破传统顺序执行范式，通过依赖图建模实现子任务的动态并行/串行调度。
	
关键技术
依赖感知的子任务图分解
两阶段训练（监督微调+强化学习）
基于MHQA构建的图规划轨迹数据集
	
性能优势
效率提升：智能并行化减少40%工具调用延迟（实验数据）
准确率改进：多跳问答任务F1值提升15%以上
泛化能力：可扩展至需要多工具协作的复杂场景
	
应用价值
为金融分析、医疗诊断等需要多源工具协同的领域提供新范式，显著降低AI系统响应时间。
地址:https://arxiv.org/abs/2510.25320

## 1.41. A-Mem: Agentic Memory for LLM Agents
https://github.com/WujiangXu/A-mem-sys

## 1.42. logic rag
You Don’t Need Pre-built Graphs for RAG: Retrieval Augmented Generation with Adaptive Reasoning Structures
https://arxiv.org/pdf/2508.06105

## 1.43. LightMem
一种受人类记忆启发的轻量级和高效的内存框架，通过选择性过滤、组织和巩固信息，显著提高了LLMs在长上下文和多轮交互场景中的表现，同时大幅降低了计算成本。未来的工作包括加速离线更新、集成知识图谱和多模态记忆机制，以及探索参数化和非参数化记忆组件的协同机制。

## 1.44. langchain graphrag
> ProgramData > anaconda3 > envs > transformer > Lib > site-packages > langchain.graphrag > indexing > graph_generation > entity.relationship.extraction > extractor.py

## 1.45. G-memory, Arcmemo, reasoning bank
三篇论文


## 1.46. embedding model 天梯
https://huggingface.co/spaces/mteb/leaderboard
https://zhuanlan.zhihu.com/p/24604344712

## 1.47. MonkeyOCR
GitHub搜索"Yuliang-Liu/MonkeyOCR"即可。本地部署后，直接上传图片或PDF，能秒速提取文字表格公式，输出Markdown或Excel格式，适合处理各类文档且保护数据安全。


## 1.48. GitHub代码检索
git-mpc和，
context7背后是各种开发框架，它针对所有github仓库


## 1.49. 视频转文字
项目GitHub地址：https://github.com/wendy7756/AI-Video-Transcriber

## 1.50. 音视频2文本
这款开源工具叫AI-Media2Doc，能将音视频一键转成小红书、公众号等风格的文档。它支持本地部署，数据都存在自己电脑，隐私有保障。适合一人公司做知识管理和内容创作，已在GitHub收获2.5k star，值得一试。

## 1.51. 爬虫数据采集圣器

GitHub开源地址是：https://github.com/ScrapeGraphAI/ScrapeGraph-ai，官网是scrapegraphai.com。

## 1.52. ai伴侣
GitHub开源项目Super Agent Party确实支持视频中提到的功能，包括QQ/B站直播接入、RAG检索、代码沙盒等。部分功能如B站接入需配置UA，Mac版仅适配M芯片。

## 1.53. metaGPT
MetaGPT项目地址：https://github.com/geekan/MetaGPT（GitHub获58.9k星标）。安装需Python 3.9-3.12环境，推荐命令：`conda create -n metagpt python=3.9 && pip install --upgrade metagpt`。核心用法：终端输入`metagpt "创建2048游戏"`即可生成完整项目；也可作为库调用，实现从需求描述到多角色协同开发的全流程自动化，特别适合快速构建MVP产品和教育编程场景。

## 1.54. unsloth
微调：49k，知识库，智能客服，代码生成，强化学习

##  1.55. ai 知识库
Supabase作为开源项目，支持通过Docker或源码在本地自行部署，既提供云端托管也满足私有化需求。

## 1.56. 高质量rag
项目地址是 https://github.com/deepset-ai/haystack

Haystack是生产级RAG框架，在GitHub有22.9k星标。它支持200多个大模型一键切换，能降低RAG幻觉63%。核心功能包括企业知识库问答、AI会议助手、法律合同审查和医疗问答系统构建，特点是向量库可自由替换、零成本迁移，适合需要稳定落地RAG场景的企业。

技术选型看这里：RAG是基础框架，FlowRAG专精复杂文档处理（比如法律合同）。Haystack能降63%幻觉，关键其实在知识库质量——文档切片准不准、语义匹配强不强，这才是根子上的事。

## 1.57. ai混合搜索 meili
开源ai混合搜索引擎是 Meilisearch，GitHub 地址是 github.com/meilisearch/meilisearch。它基于 Rust 实现，支持混合搜索，GitHub 已获 53.7k 星标。

## 1.58. mem 推移学习，自我改进
官网：docs.letta.com/

## 1.59. 腾讯 tree graphrag （2025年9月）
https://mp.weixin.qq.com/s/Ddf3rpdJP8P_L5yaPnBFBA

## 1.60. Graphiti vs GraphRAG 对比

| 方面 | GraphRAG | Graphiti |
| --- | --- | --- |
| 主要用途 | 静态文档摘要 | 动态数据管理 |
| 数据处理 | 批处理导向 | 连续增量更新 |
| 知识结构 | 实体集群和社区摘要 | 情景数据、语义实体、社区 |
| 检索方法 | 顺序 LLM 摘要 | 混合语义、关键词和基于图的搜索 |
| 适应性 | 低 | 高 |
| 时间处理 | 基本时间戳跟踪 | 显式双时态跟踪 |
| 矛盾处理 | LLM 驱动的摘要判断 | 时间边缘失效 |
| 查询延迟 | 秒到几十秒 | 通常亚秒延迟 |
| 自定义实体类型 | 否 | 是，可自定义 |
| 可扩展性 | 中等 | 高，针对大型数据集优化 |


## 1.61. 自己用milvus+neo4j实现graphrag
https://github.com/milvus-io/bootcamp/blob/master/bootcamp/RAG/advanced_rag/langgraph-graphrag-agent-local.ipynb

## 1.62. 微软 graphRAG
标准 GraphRAG： 效果最好，图谱信息最丰富，但最贵最慢。
FastGraphRAG： 速度快，成本低，但图谱信息相对简单。
LazyGraphRAG (懒人版/省钱版)： 这是个新趋势。它在索引阶段只做最少的工作，大部分 LLM 的计算任务推迟到你真正提问的时候再做。这样前期成本大大降低，特别适合超大数据集或预算有限的情况。

AI知识图谱中GraphRAG，核心内容可总结为以下几点：
 
1. 传统RAG的局限性
 
传统RAG将文章切成文字片段，通过embedding转化为向量存入向量数据库。但存在矛盾：
 
- 片段切太大，会漏掉细节（如统计“西瓜出现次数”时，因西瓜分散在不同片段，易检索错误或遗漏）；
- 片段切太小，会破坏语义联系（如查询“老王喜欢吃什么”时，因信息被打断而无法回答）。
 
2. GraphRAG的解决方案：知识图谱
 
GraphRAG通过知识图谱（Knowledge Graph） 解决传统RAG的问题，知识图谱由实体（Entity）、关系（Relationship） 及属性构成，这种图结构称为LPG（Labeled Property Graph）。
 
以“老王爱吃西瓜”为例，构建知识图谱的过程：
 
- 命名实体识别：识别出“老王”“西瓜”两个实体；
- 关系抽取：识别出“爱吃”的关系；
- 多轮追问（Data Cleaning）：GraphRAG会反复让大模型补充信息，确保图谱完整；
- 实体合并与总结：对文章中所有片段生成的知识图谱，合并同名实体，并让大模型生成更通顺的总结性描述，最终形成文章级的知识图谱。
 
3. 知识图谱的层级结构
 
为了让庞大的知识图谱更易查询，GraphRAG通过莱顿社区检测算法，将边密集的节点合并成子图，再让大模型生成子图的总结性描述，形成层级结构——上层信息抽象精炼，下层接近原文细节。
 
4. 查询策略
 
- Local Search：从最底层知识图谱开始查询，适合细节丰富、定位准确的问题（如“老王爱吃什么具体食物”）；
- Global Search：从图谱高层开始查询，适合抽象、全局性的问题（如“文章核心观点是什么”）。


- Local Search：从最底层的知识图谱开始，找出与问题最接近的实体，再反向追溯这些实体和边由哪些原文生成，以及出现在哪些上层图谱结构里，适合处理细节丰富、定位准确的问题。
- Global Search：从图谱的高层开始，一层一层向下追溯，适合回答抽象、全局性更强的问题，例如文章的核心观点是什么。
 
整体而言，GraphRAG通过让大语言模型深度参与知识图谱的构建、总结和查询全流程，解决了传统RAG的细节与语义矛盾问题，虽较“烧资源”，但效果表现不错。

## 1.63. awesome-ai-memory 汇聚memory相关项目
https://github.com/topoteretes/awesome-ai-memory

## 1.64. es agent
基于 Langchain 的 Elasticsearch Agent 对文档的搜索
https://elasticstack.blog.csdn.net/article/details/136253286

## 1.65. MINE Context
万物皆可上下文， 挖掘上下文
https://github.com/volcengine/MineContext/tree/main?tab=readme-ov-file
https://github.com/volcengine/MineContext/blob/main/README_zh.md

字节开源AI助手MineContext，是一款能主动工作的"数字外脑"。它自动分析你电脑上的文档、网页等内容，实时生成待办清单和每日摘要，不像普通AI等你提问。所有数据都存储在本地不上传云端，既保护隐私又能帮你摆脱信息碎片化困扰，工作学习效率提升明显。

## 1.66. 拼好rag
https://mp.weixin.qq.com/s/c0KC--EO9tuJuaadlujobg

https://github.com/1517005260/graph-rag-agent/blob/master/assets/start.md

https://github.com/1517005260/graph-rag-agent

https://deepwiki.com/1517005260/graph-rag-agent/2-core-architecture


## 1.67. mem0 2025年9月27日持续更新github
基于graph+rag的mem0
https://github.com/mem0ai/mem0


## 1.68. 蚂蚁 KAG
https://github.com/orgs/OpenSPG/discussions/52

![alt text](zfig/readme/image.png)
![alt text](zfig/readme/image-1.png)
![alt text](zfig/readme/image-2.png)

KAG客户端 使用方式：
https://github.com/1850298154/KagTest

参考 HippoRAG
https://github.com/OSU-NLP-Group/HippoRAG
https://dl.acm.org/doi/10.5555/3737916.3739818

## 1.69. 如何基于语义相似性分割文本
RAG分割文档的几种方式：
1. 基于语义相似性的分割文本
https://python.langchain.ac.cn/docs/how_to/semantic-chunker/
2. 其他（基于固定长度、基于滑动窗口、基于标题等）

## 1.70. 各种向量数据库对比
https://www.cnblogs.com/crazymakercircle/p/18867143

## 1.71. 基于hnswlib的向量索引(2年前更新)
https://github.com/nmslib/hnswlib

## 1.72. stream vq 生成式召回
https://zhuanlan.zhihu.com/p/1955356511661458958

## 1.73. ai学术搜索
官网地址是：https://lumina.sh，可直接访问使用这款免费学术搜索引擎。

## 1.74. nlp etc.
https://www.geeksforgeeks.org/category/nlp/


## 1.75. 知识图谱 - 北京大学大数据分析与应用技术国家工程实验室成员，  包括各种知识图谱抽取+检索，neo4j+MongoDB等
https://liuhuanyong.github.io/

## 1.76. 唐国梁Tommy : rag + llm + es
https://github.com/TGLTommy?tab=repositories

https://www.youtube.com/@TGLTommy

唐国梁Tommy官方网站
tgltommy.com

微信公众号
tgltommy.com/p/official-wechat

bilibili
space.bilibili.com/474347248


## 1.77. 长文本提取结构化信息
项目 GitHub 地址：github.com/google/LangExtract  
PyPI 安装命令：pip install langextract


## 1.78. 非结构化转结构化，用于微调等
Easy Workspace工具，它能自动将PDF、Word等非结构化数据转化为结构化微调训练数据。通过三步流程：数据标准化、内容提取分割、生成问答对，帮助企业高效完成大模型微调，显著降低人工成本。

## 1.79. MongoDB + ES 向量存储 + 文本分割器SpacyTextSplitter （24年6月11日）
https://www.53ai.com/news/LargeLanguageModel/2024061171948.html

## 1.80. ai coding

Roo Code  最早

Cline 代码比roo code仓库的更规范

Kilo 继承前两者

Metamove 字节内部



# 2. ai agent 架构、新闻DIY、产品汇总
## 2.1. ai agent 架构

### 2.1.1. roma 等（字节aime，分析计划树agent）
MECE分析法，全称Mutually Exclusive Collectively Exhaustive，中文意思是“相互独立，完全穷尽”。 也就是对于一个重大的议题，能够做到不重叠、不遗漏的分类，而且能够借此有效把握问题的核心，并解决问题的方法。

优点：并发度，丰富度，发散性
缺点：关联度，交叉度，逻辑性

### 2.1.2. 数分+营销
专属AI股神 TradingAgents-CN，专门为中文用户设计，支持本土化操作。它能智能分析趋势，提供精准的建议


## 2.2. 其他人 ai hub

🔥更多大模型教程：https://github.com/echonoshy/cgft-llm


https://github.com/Shubhamsaboo/awesome-llm-apps

ashishpatel26/500-A1-Agents-Projects

sindresorhus/awesome

## 2.3. 令人启发的产品


### 2.3.1. 用知识卡片，轻松建立知识体系
Rabbithole.chat
### 2.3.2. 教育
https://www.aihub.cn/tools/study/gauth/

### 2.3.3. 学术
Findin AI是AI学术工具，能显著提升科研效率。



## 2.4. ai agent 新闻频道


### 2.4.1. aihub (外国日报)
https://www.aihub.cn/tools/study/gauth


### 2.4.2. ai 技术新闻（英国）
https://ai.plainenglish.io/forgetting-in-ai-agent-memory-systems-7049181798c4

### 2.4.3. github ai  (外国日报论坛)
Discover and explore top open-source AI tools and projects—updated daily.

https://www.sourcepulse.org/

https://www.sourcepulse.org/projects/1844761

### 2.4.4. ai tool navigation (中国一站式)

https://aitool.zyqok.com/

https://aitool.zyqok.com/digest/2024/0402/RAGOnMedicalKG-%E5%8C%BB%E8%8D%AF%E9%A2%86%E5%9F%9FKG+%E5%A4%A7%E6%A8%A1%E5%9E%8BRAG%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%BA%90%E5%85%BC%E7%9C%8B20240329%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%BF%9B%E5%B1%95%E6%97%A9%E6%8A%A5/




# 3. 知名服务商

---


## 3.1. 阿里 mem0 milvus
https://mp.weixin.qq.com/s/0l6TP8DjArNwulMfFNlw1A

mem0技术与架构拆解图 上篇笔记介绍了外挂记忆系统的... http://xhslink.com/o/4Kv1JF4WfUE 
Copy and open Xiaohongshu to view the full post！


# 4. AI 指南 + 面试指南

---


### 4.0.1. 飞书文档

> 一站式AI产品经理入门指南
> https://v11enp9ok1h.feishu.cn/wiki/KiIvwdFOciiqqNkwKzTcmn88ndL

> AI 活雷锋
> https://kwz55xptfhg.feishu.cn/wiki/T5oew0kY4in3EIk1Wlfc3oIGnhe

> AI产品经理行业资料库（持续更新）
> https://gxvezr0dpem.feishu.cn/docx/BE1YdDKeOoNZcvxeidccwJ65nnc

### 4.0.2. 马士兵飞书
https://kwz55xptfhg.feishu.cn/wiki/F9odwJL5NiOc7vkscm5cC2nAnIh

# 5. 基础
## 5.1. 统计学自学指南 stats-self-learning

https://xuankaiwang.github.io/


