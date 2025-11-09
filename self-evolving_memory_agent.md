# 终极目标

为了做 真正的 self-evolving agent， 离不开基于知识图谱+向量索引+倒排文档的持久化存储：
1. 知识图谱： 存储企业知识， 包括 实体、关系、属性等
2. 向量索引： 存储企业文档的向量表示， 用于 文档检索
3. 倒排文档： 存储企业文档的 倒排索引， 用于 文档检索

就好比人类不需要掌握所有的技能和知识，使用书籍、网络等方式记录并检索。agent也可以进行经验的沉淀与总结，并持久化，依赖外部的数据库或搜索引擎，召回之前的经验，进行反复的进化。

## obj: 使用的目标地方
get ER schema agent 
thinking plan agent
python plot tool invocation description
sql generator agent
html agent

## way: 优化每一个 agent/tool 单独使用如下方式优化：
1. evaluator -> failure data
2. data agent -> failure analysis embeddings + es
3. retriever -> recall + rerank 
4. optimizer -> evolutionary target KGraph + es + embeding
5. generator -> {system prompt, tools [invocation,return] description} generation

## from: 失败待改进反馈的来源
1. tool执行失败
2. 自动评测效果不佳
3. 用户点踩反馈

## key: 核心技术
1. stronger memory: 
   1. graph: knowledge relation
   2. vector: similar text
   3. json-ivf: chronological time + event
2. better retrieval:  multi-recall + rerank

## when: 使用场景
1. 优化 agent离线（不是在线召回）的 system prompt / tool ， 沉淀高质量、有失败依据的 SP/tool design 
2. 为用户构建每一轮ReAct高质量的 plan 
3. 自动化构建企业级高质量的 ER schema
4. 企业的知识沉淀

# 无限状态空间建模
为了让 agent 能够自主完成未知任务， 需要让 agent 能够清晰地知道自己的任务状态， 包括：
1. 我在那
2. 我还差什么
3. 我该怎么做

技术实现：
1. 任务状态追踪，自主检测任务进度
2. 知道刚才的状态是否达到预期
3. 任务分解与规划，自主制定子任务；任务执行与反馈，自主完成子任务并根据反馈调整计划

三个机制：
1. 中间状态建模能力：不仅知道起点终点，还需要知道经过哪些点
2. 多模态反馈对比机制：判断现在的在感知状态 和预期状态的差距
3. 自我修正与优化机制：任务偏移和检测机制，如果路径跑偏要能触发replanning fallback

# 高效检索召回
## （一）如何在海量文件中 “快速找到目标”？—— 三层检索加速策略
1. 数据库路由：从 “全库检索” 到 “精准分库”
2. Small2Big 策略：小探针 + 大页面，兼顾 “速度” 与 “细节”
   - 双粒度：先粗筛（小 chunk 快召回）再精提（大 chunk 补上下文），
   - 步骤 1：预处理阶段 —— 生成双粒度 chunk 并建库
   - 步骤 2：检索阶段 —— 小 chunk “探针” 快速召回候选
     1. 小 chunk 检索：用混合索引（关键词 + 语义）查询小 chunk 库，设置较大的 TopK（比如 Top50，而非基础 RAG 的 Top5）—— 因为小 chunk 体积小，即使召回 50 个，检索速度也远快于召回 50 个大 chunk；
     2. 去重关联：对召回的 50 个小 chunk 去重（避免同一大 chunk 的多个小 chunk 重复召回），通过映射表找到对应的 20-30 个大 chunk（父页）。
   - 步骤 3：筛选阶段 —— 大 chunk “上下文” 精准提取
     1. 大 chunk 筛选：对 20-30 个大 chunk，用轻量 Rerank（如 Cross-BERT）快速筛选出 Top10（基于 “问题与大 chunk 的语义相关性”）；
     2. 细节提取：从 Top10 大 chunk 中，精准定位与问题相关的细节（比如从 “定价 + 适用场景 + 退款规则” 的大 chunk 中，提取 “999 元” 这个定价信息）；
     3. 结果输出：将提取的细节与大 chunk 的 “文件名称 + 页码” 绑定，作为 RAG Content 传入 LLM。
3. 混合索引：关键词 + 语义，双保险避免 “漏检”
## （二）如何确保找到的内容 “正确无误”？—— 三重校验筛选策略
1. 数据库路由 + Small2Big：从 “定位” 上保证正确性
2. 结构优化：让数据库内容 “格式统一、信息准确”
3. 两阶段 Rerank：经济且精准的 “结果筛选”
## （三）如何在有效 RAG Content 基础上 “减少幻觉”？—— 七重约束输出策略
1. Prompt 路由：垂直问题 “专属指令”
2. Pydantic Schema：格式化输入 / 输出，锁住随机性
3. COT 思维链：强化推理，避免 “跳跃式结论”
4. 强制参考 RAG Content + 示例引导
5. faq.txt 规则库：解决模糊问题的 “歧义”
6. 对比类问题：自动拆分子任务，避免 “混为一谈”
7. 页码验证：确保答案 “可追溯、真实存在”
