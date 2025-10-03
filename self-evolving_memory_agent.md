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

