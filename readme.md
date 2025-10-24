
# 介绍 LLM、RAG、Agent、Memory、Retrieval、KG 等相关技术的融合

---
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


## 自己用milvus+neo4j实现graphrag
https://github.com/milvus-io/bootcamp/blob/master/bootcamp/RAG/advanced_rag/langgraph-graphrag-agent-local.ipynb

## 微软 graphRAG
标准 GraphRAG： 效果最好，图谱信息最丰富，但最贵最慢。
FastGraphRAG： 速度快，成本低，但图谱信息相对简单。
LazyGraphRAG (懒人版/省钱版)： 这是个新趋势。它在索引阶段只做最少的工作，大部分 LLM 的计算任务推迟到你真正提问的时候再做。这样前期成本大大降低，特别适合超大数据集或预算有限的情况。

## awesome-ai-memory 汇聚memory相关项目
https://github.com/topoteretes/awesome-ai-memory

## es agent
基于 Langchain 的 Elasticsearch Agent 对文档的搜索
https://elasticstack.blog.csdn.net/article/details/136253286

## MINE Context
万物皆可上下文， 挖掘上下文
https://github.com/volcengine/MineContext/tree/main?tab=readme-ov-file
https://github.com/volcengine/MineContext/blob/main/README_zh.md


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

> https://v11enp9ok1h.feishu.cn/wiki/KiIvwdFOciiqqNkwKzTcmn88ndL

> https://kwz55xptfhg.feishu.cn/wiki/T5oew0kY4in3EIk1Wlfc3oIGnhe

> https://gxvezr0dpem.feishu.cn/docx/BE1YdDKeOoNZcvxeidccwJ65nnc

