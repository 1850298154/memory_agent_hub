# 终极目标
基于知识图谱+向量索引+倒排文档的 self-evolving agent

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



# 开源项目

---

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


## 基于hnswlib的向量索引(2年前更新)
https://github.com/nmslib/hnswlib

## stream vq 生成式召回
https://zhuanlan.zhihu.com/p/1955356511661458958

## ai学术搜索
官网地址是：https://lumina.sh，可直接访问使用这款免费学术搜索引擎。

## 知识图谱 - 北京大学大数据分析与应用技术国家工程实验室成员
https://liuhuanyong.github.io/

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

