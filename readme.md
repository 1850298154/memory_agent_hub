
# 介绍 LLM、RAG、Agent、Memory、Retrieval、KG 等相关技术的融合

---

## 综述
《Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG》

## Prop RAG 
https://github.com/ReLink-Inc/PropRAG
核心创新：以"命题"为基础知识单元，通过无LLM的在线束搜索实现高效多跳推理
技术特点：
- 命题知识单元：将文档分解为语义丰富的命题，作为检索和推理的基本单位
- 束搜索算法：采用高效的束搜索在命题路径上进行多步推理，无需在线调用LLM
- 推理路径发现：能够自动发现和构建多步推理链，支持复杂问题解答

## 基于多模态信息抽取的菜品知识图谱构建
https://tech.meituan.com/2024/05/17/cross-modal-ingredient-level-dataset.html

## ragflow 已经支持 知识图谱
Construct knowledge graph

https://ragflow.io/docs/dev/construct_knowledge_graph

## LightRAG
港大团队开源LightRAG：知识图谱+双层检索，复杂问答准确率飙升30%

LightRAG的主要优势包括：

- 高效的知识图谱构建：LightRAG通过图结构差异分析实现增量更新算法，显著降低了计算开销，使知识库维护更加高效。
- 双层检索机制：该系统结合了低层次（具体实体和属性）和高层次（广泛主题和概念）的检索策略，满足了不同类型的查询需求，提高了检索的全面性和多样性。
- 快速适应动态数据：LightRAG能够在新数据到来时快速整合，无需重建整个知识库，确保系统在动态环境中保持高效和准确。

https://link.zhihu.com/?target=https%3A//github.com/HKUDS/LightRAG

https://zhuanlan.zhihu.com/p/1892140189524156837

## llm agent 综述
https://hustai.github.io/zh/posts/reasoning/LATS.html

## 谷歌 vs 微软 deepresearch
 https://mp.weixin.qq.com/s/e_1dGQRLfc_fGAZrQEsLVw
## Reasoning with Sampling: Your Base Model is Smarter Than You Think
哈佛团队的"Power Sampling"方法很妙：只需改变基座模型的采样分布（从常规改为幂分布），就能大幅提升推理能力。它不依赖强化学习、无需额外训练，连校验器都不用，却让Qwen2-5-Math-7B模型在数学任务准确率从49.6%跃升至74.8%，编程任务更是从21.3%飙升到73.2%——不仅逼近强化学习效果，还避免了多样性坍缩问题。这证明基础模型本身已蕴含强大推理潜力，只是被传统采样方式束缚住了。

## Agentic RAG新范式！天大&小红书提出DecEx-RAG，剪枝搜索扩展提速6倍

## 日报神器，记录你的一天 Dayflow
项目地址是
 https://github.com/JerryZLiu/Dayflow

，展示了这个开源日报工具

##  可信AI Agent相关论文(DPO)
![img](https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://juejin.cn&size=32

[打造可信AI Agent：如何让智能体不跑偏、不越界，安全又靠谱如何让 Agent 在开放环境、长序列决策与多工具协作中 - 掘金](https://juejin.cn/post/7564246560847052842)

![img](https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://toutiao.com&size=32

[迈向可信AI Agent：Jeddak AgentArmor意图对齐与约束遵循方案 - 今日头条](https://www.toutiao.com/article/7561503362732065289/?upstream_biz=doubao&source=m_redirect)

![img](https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://toutiao.com&size=32

[为 AI Agent 行为立“规矩”——字节跳动提出 Jeddak AgentArmor 智能体安全框架 - 今日头条](https://www.toutiao.com/article/7543322896609919528/?upstream_biz=doubao&source=m_redirect)

## Graph-Base Agent基于任务图的Agent框架
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

## A-Mem: Agentic Memory for LLM Agents
https://github.com/WujiangXu/A-mem-sys

## logic rag
You Don’t Need Pre-built Graphs for RAG: Retrieval Augmented Generation with Adaptive Reasoning Structures
https://arxiv.org/pdf/2508.06105

## LightMem
一种受人类记忆启发的轻量级和高效的内存框架，通过选择性过滤、组织和巩固信息，显著提高了LLMs在长上下文和多轮交互场景中的表现，同时大幅降低了计算成本。未来的工作包括加速离线更新、集成知识图谱和多模态记忆机制，以及探索参数化和非参数化记忆组件的协同机制。

## langchain graphrag
> ProgramData > anaconda3 > envs > transformer > Lib > site-packages > langchain.graphrag > indexing > graph_generation > entity.relationship.extraction > e extractor.py

## G-memory, Arcmemo, reasoning bank
三篇论文


## embedding model 天梯
https://huggingface.co/spaces/mteb/leaderboard
https://zhuanlan.zhihu.com/p/24604344712

## MonkeyOCR
GitHub搜索"Yuliang-Liu/MonkeyOCR"即可。本地部署后，直接上传图片或PDF，能秒速提取文字表格公式，输出Markdown或Excel格式，适合处理各类文档且保护数据安全。


## GitHub代码检索
git-mpc和，
context7背后是各种开发框架，它针对所有github仓库


## 视频转文字
项目GitHub地址：https://github.com/wendy7756/AI-Video-Transcriber

## 音视频2文本
这款开源工具叫AI-Media2Doc，能将音视频一键转成小红书、公众号等风格的文档。它支持本地部署，数据都存在自己电脑，隐私有保障。适合一人公司做知识管理和内容创作，已在GitHub收获2.5k star，值得一试。

## 爬虫数据采集圣器

GitHub开源地址是：https://github.com/ScrapeGraphAI/ScrapeGraph-ai，官网是scrapegraphai.com。

## ai伴侣
GitHub开源项目Super Agent Party确实支持视频中提到的功能，包括QQ/B站直播接入、RAG检索、代码沙盒等。部分功能如B站接入需配置UA，Mac版仅适配M芯片。

## metaGPT
MetaGPT项目地址：https://github.com/geekan/MetaGPT（GitHub获58.9k星标）。安装需Python 3.9-3.12环境，推荐命令：`conda create -n metagpt python=3.9 && pip install --upgrade metagpt`。核心用法：终端输入`metagpt "创建2048游戏"`即可生成完整项目；也可作为库调用，实现从需求描述到多角色协同开发的全流程自动化，特别适合快速构建MVP产品和教育编程场景。

## unsloth
微调：49k，知识库，智能客服，代码生成，强化学习

##  ai 知识库
Supabase作为开源项目，支持通过Docker或源码在本地自行部署，既提供云端托管也满足私有化需求。

## 高质量rag
项目地址是 https://github.com/deepset-ai/haystack

Haystack是生产级RAG框架，在GitHub有22.9k星标。它支持200多个大模型一键切换，能降低RAG幻觉63%。核心功能包括企业知识库问答、AI会议助手、法律合同审查和医疗问答系统构建，特点是向量库可自由替换、零成本迁移，适合需要稳定落地RAG场景的企业。

技术选型看这里：RAG是基础框架，FlowRAG专精复杂文档处理（比如法律合同）。Haystack能降63%幻觉，关键其实在知识库质量——文档切片准不准、语义匹配强不强，这才是根子上的事。

## ai混合搜索 meili
开源ai混合搜索引擎是 Meilisearch，GitHub 地址是 github.com/meilisearch/meilisearch。它基于 Rust 实现，支持混合搜索，GitHub 已获 53.7k 星标。

## mem 推移学习，自我改进
官网：docs.letta.com/

## 腾讯 tree graphrag （2025年9月）
https://mp.weixin.qq.com/s/Ddf3rpdJP8P_L5yaPnBFBA

## Graphiti vs GraphRAG 对比

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


## 自己用milvus+neo4j实现graphrag
https://github.com/milvus-io/bootcamp/blob/master/bootcamp/RAG/advanced_rag/langgraph-graphrag-agent-local.ipynb

## 微软 graphRAG
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

## awesome-ai-memory 汇聚memory相关项目
https://github.com/topoteretes/awesome-ai-memory

## es agent
基于 Langchain 的 Elasticsearch Agent 对文档的搜索
https://elasticstack.blog.csdn.net/article/details/136253286

## MINE Context
万物皆可上下文， 挖掘上下文
https://github.com/volcengine/MineContext/tree/main?tab=readme-ov-file
https://github.com/volcengine/MineContext/blob/main/README_zh.md

字节开源AI助手MineContext，是一款能主动工作的"数字外脑"。它自动分析你电脑上的文档、网页等内容，实时生成待办清单和每日摘要，不像普通AI等你提问。所有数据都存储在本地不上传云端，既保护隐私又能帮你摆脱信息碎片化困扰，工作学习效率提升明显。

## 拼好rag
https://mp.weixin.qq.com/s/c0KC--EO9tuJuaadlujobg

https://github.com/1517005260/graph-rag-agent/blob/master/assets/start.md

https://github.com/1517005260/graph-rag-agent

https://deepwiki.com/1517005260/graph-rag-agent/2-core-architecture


## mem0 2025年9月27日持续更新github
基于graph+rag的mem0
https://github.com/mem0ai/mem0


## 蚂蚁 KAG
https://github.com/orgs/OpenSPG/discussions/52

![alt text](zfig/readme/image.png)
![alt text](zfig/readme/image-1.png)
![alt text](zfig/readme/image-2.png)

KAG客户端 使用方式：
https://github.com/1850298154/KagTest

参考 HippoRAG
https://github.com/OSU-NLP-Group/HippoRAG
https://dl.acm.org/doi/10.5555/3737916.3739818

## 如何基于语义相似性分割文本
RAG分割文档的几种方式：
1. 基于语义相似性的分割文本
https://python.langchain.ac.cn/docs/how_to/semantic-chunker/
2. 其他（基于固定长度、基于滑动窗口、基于标题等）

## 各种向量数据库对比
https://www.cnblogs.com/crazymakercircle/p/18867143

## 基于hnswlib的向量索引(2年前更新)
https://github.com/nmslib/hnswlib

## stream vq 生成式召回
https://zhuanlan.zhihu.com/p/1955356511661458958

## ai学术搜索
官网地址是：https://lumina.sh，可直接访问使用这款免费学术搜索引擎。

## nlp etc.
https://www.geeksforgeeks.org/category/nlp/


## 知识图谱 - 北京大学大数据分析与应用技术国家工程实验室成员，  包括各种知识图谱抽取+检索，neo4j+MongoDB等
https://liuhuanyong.github.io/

## 唐国梁Tommy : rag + llm + es
https://github.com/TGLTommy?tab=repositories

https://www.youtube.com/@TGLTommy

唐国梁Tommy官方网站
tgltommy.com

微信公众号
tgltommy.com/p/official-wechat

bilibili
space.bilibili.com/474347248


## 长文本提取结构化信息
项目 GitHub 地址：github.com/google/LangExtract  
PyPI 安装命令：pip install langextract


## 非结构化转结构化，用于微调等
Easy Workspace工具，它能自动将PDF、Word等非结构化数据转化为结构化微调训练数据。通过三步流程：数据标准化、内容提取分割、生成问答对，帮助企业高效完成大模型微调，显著降低人工成本。

## MongoDB + ES 向量存储 + 文本分割器SpacyTextSplitter （24年6月11日）
https://www.53ai.com/news/LargeLanguageModel/2024061171948.html

## ai coding

Roo Code  最早

Cline 代码比roo code仓库的更规范

Kilo 继承前两者

Metamove 字节内部



# 知名服务商

---


## 阿里 mem0 milvus
https://mp.weixin.qq.com/s/0l6TP8DjArNwulMfFNlw1A


# 面试指南

---


### 飞书文档

> 一站式AI产品经理入门指南
> https://v11enp9ok1h.feishu.cn/wiki/KiIvwdFOciiqqNkwKzTcmn88ndL

> AI 活雷锋
> https://kwz55xptfhg.feishu.cn/wiki/T5oew0kY4in3EIk1Wlfc3oIGnhe

> AI产品经理行业资料库（持续更新）
> https://gxvezr0dpem.feishu.cn/docx/BE1YdDKeOoNZcvxeidccwJ65nnc

### 马士兵飞书面经
https://kwz55xptfhg.feishu.cn/wiki/F9odwJL5NiOc7vkscm5cC2nAnIh

# 基础
## 统计学自学指南 stats-self-learning

https://xuankaiwang.github.io/


