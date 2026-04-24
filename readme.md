
# 1. 2026 swarm Agent 年，swarm Agent 、Agent team、 ai coding、skill、memory、evolve、verify、agentic RL 等 AI Agent集合
---
## 从头训练大模型
https://github.com/allenai/OLMoE


## 卡帕西LLM Wiki的最佳实现
卡帕西的 LLM Wiki 这坑挖的真够深的，自己不给出实现，全靠社区用户自己手搓。看起来很美好，做起来一团糟。（我之前视频中做的skill也很初级）
但是YC总裁Garry Tan (陈嘉里)，给出了满分答卷：GBrain。
GitHub 仓库garrytan/gbrain，上线一周多目前10.1k Stars。

#Karpathy #GBrain #LLMWiki #Obsidian #OpenClaw #HermesAgent #AgentSkill #AIAgent #AI #Obsidian教程
来看看这个专为OpenClaw和Hermes Agent打造的重度工作流如何使用。
## M-FLOW架构
可通过Docker一键部署：先执行'docker pull mflow/official'拉取镜像，再运行'docker run -p 8080:8080 mflow/official'启动服务。核心API包括/ingest数据录入和/search图路由检索，已完全开源可在GitHub获取详细文档。


M-FLOW未公布单一"记忆成功率"指标，但在权威测试中表现突出：LoCoMo基准领先Mem0 36%，LongMemEval领先Graphiti 16%。这些数据直观反映了其在多跳推理和跨文档关联任务中的技术优势。


M-FLOW开源地址：https://github.com/FlowElement-ai/m_flow
## 八个rl agent
(1) search-r1 (2) agent-r1 (3) agents meet rl  (4)  agent-lightning (5) agentGym (6) ART (7) 500+ AI Agent Projects (8) awesom-agenticLLM-RL-Papers


## 专治乱写
https://github.com/forrestchang/andrej-karpathy-skills 四条铁律专治AI乱写代码：事前思考避免假设、简洁至上压缩行数、精准改动不碰无关代码、目标驱动验证成功。

## 开源复刻Claude：770M参数比肩1.3B商业模型


OpenMythos项目由Kye Gomez发布在GitHub
项目地址：https://github.com/kyegomez/OpenMythos  
这是Kye Gomez开源的Claude架构理论重构项目。


Anthropic的Mythos是否真的用了这套架构，似乎已经不重要了。对循环Transformer的猜想已经吸引了来自学术界的大量目光。更多理论和实验验证正在路上。
GitHub：


https://github.com/kyegomez/OpenMythos#the-central-hypothesis

参考链接：

[1]https://x.com/KyeGomezB/status/2045660378844024994

[2]https://arxiv.org/abs/2604.07822

[3]https://arxiv.org/abs/2604.12946

## Zread的官方访问地址是https://zread.ai

你可以通过这个网址直接使用该工具解析GitHub项目。


## OpenAI：如何系统评估skill，证明它没被改坏？
原文标题：Testing Agent Skills Systematically with Evals
原文链接：https://developers.openai.com/blog/eval-skills 


##  QuantDinger是开源的本地优先AI量化交易平台，支持多市场接入和AI策略分析。
项目GitHub地址：https://github.com/brokermr810/QuantDinger


## 项目越做越大，架构越来越复杂，想回头看看自己的代码反而一头雾水？

今天推荐一款神器：Oh-my-Mermaid。

它能让 AI 自动扫描代码库，生成可视化的架构文档。

输入一条指令，自动分析项目结构，生成 Mermaid 图表，还能交互式浏览。

复杂逻辑节点会自动递归分析，拆解出嵌套子元素，生成清晰的目录树。

已适配 Claude Code、Codex 等主流 AI 编程工具，一条命令自动配置，文档还能同步到云端分享给团队。

用 AI 开发的项目越来越大，想回头看自己的代码库，架构是什么样的、数据怎么流转的，反而越来越模糊。

如果你的项目已经大到自己都记不清架构了，用它扫一遍，比手动画图省事 100 倍。

GitHub 开源免费。


#AI #ClaudeCode #代码架构 #Mermaid #程序员 #编程工具 #GitHub #开发者工具 #效率提升 #架构图
GitHub地址：https://github.com/mermaid-js/mermaid。这是视频中提到的开源代码架构可视化工具，能通过AI扫描自动生成Mermaid图表，帮你快速理清复杂项目结构。

## HTML-PPT AgentSkill是由Lewis开源的PPT制作工具
地址是github.com/lewislulu/html-ppt-skill。只需执行`npx skills add`命令，AI即可掌握100+PPT技能，包含36个主题、20+物理特效、31种页面布局和14套完整模板，支持技术分享、路演、小红书图文等多种场景，真正实现"一句话需求→专业PPT"的自动化流程。

## 浏览器Harness的GitHub开源地址是：https://github.com/browser-use/browser-harness
## 项目名称：banana-slides
（GitHub：Anionex/banana-slides）。主要功能：基于nano banana pro的原生AI PPT生成工具，支持语音指令生成/精准修改单页内容，可上传参考图片定制风格，一键导出标准pptx/pdf文件，16:9比例排版无需二次调整。

## 真正的提示词炼金炉，大白话秒变专业指令 

项目GitHub地址：https://github.com/linshenkx/prompt-optimizer
## 首个将99位加密KOL交易经验LLM蒸馏为可回测量化因子的开源项目 量化skill 


https://github.com/0xquqi/crypto-kol-quant


## Omni-SimpleMem是解决AI长效记忆问题的多模态框架
，准确率提升411%。项目论文：arXiv:2604.01007，代码仓库：github.com/aiming-lab/SimpleMem

## MiniMind是超轻量级开源语言模型项目
仅需3元成本（单卡3090）2小时即可训练出25.8M参数模型，体积仅为GPT-3的1/7000。完整开源从tokenizer训练、数据清洗到预训练、监督微调、强化学习的全流程代码，支持个人GPU快速训练。GitHub地址：https://github.com/jingyaogong/minimind

## 开源金融情报平台，复刻AI投资大师，完全免费，自带CFA级别的分析能力、100多个数据接口等 

Fincept Terminal的开源地址是：https://github.com/Fincept-Corporation/FinceptTerminal
## SparkNoteAI已在GitHub开源。
项目地址：https://github.com/spark-ai-boy/SparkNoteAI
## 微信cli
①工具定位
WeChat CLI是专为AI集成设计的命令行工具，实现安全访问本地微信数据。

②功能体系
提供11个结构化命令，涵盖会话管理、历史查询、消息搜索等全流程数据操作。

③安全机制
全程本地操作，SQLCipher即时解密数据库，确保数据不出本机的安全闭环。

④AI适配
默认JSON输出格式，无缝对接Claude、OpenClaw等AI智能体的数据处理需求。

⑤跨平台支持
兼容macOS(含Apple Silicon)、Windows、Linux三大系统，适配不同硬件架构。

⑥操作逻辑
通过init命令提取微信密钥，实现无侵入式数据访问，无需逆向工程。

1. 环境准备
确认已安装Node.js 16+环境，这是工具运行的基础条件。

2. 工具安装
执行npm install -g @canghe_ai/wechat-cli完成全局安装。

3. 初始化配置
保持微信客户端运行，macOS/Linux使用sudo权限执行wechat-cli init。

4. 多账号处理
按文件修改时间识别当前登录账号，解决多微信账号数据选择问题。

5. AI集成配置
在Claude等工具中添加WeChat CLI说明文档，建立自然语言交互通道。

6. 场景应用
尝试"sessions"查看会话、"history 联系人"读取消息、"search 关键词"精准检索。

7....
## 达尔文.skill是基于进化论思想的AI技能自动优化系统，通过棘轮机制实现53个skill只升不降的持续进化。采用8维度评分体系（结构60分+效果40分），优化成功则保留，失败自动回滚。

项目地址：
GitHub: https://github.com/alchaincyf/darwin-skill
安装命令: npx skills add alchaincyf/darwin-skill

女娲.skill开源地址：https://github.com/alchaincyf/nuwa-skill


## 全自动AI开发军团来了，24小时无人自主干活#AI #AI帮你干活 
OpenSwarm项目地址：https://github.com/unohee/OpenSwarm。部署需Node.js≥22环境，配置Discord和Linear API后运行npm install即可启动。


## Cangjie Skill项目的官方GitHub地址是：https://github.com/kangarooking/cangjie-skill


## fast learn
1. 这个领域所有专家都认同的五个核心思维模式是什么？
2. 该领域专家们争论最激烈的三个方面是什么？各自的最强论据是什么？
3. 请生成10道能区分真懂和死记硬背的问题。
## 热榜
1. Awesome Design MD：精心收集的设计系统库，捕获流行网站UI规范，解决AI代理执行设计的最后一公里问题。
2. Hermes Agent：宣称与用户共同成长的AI代理，长期稳居榜单的实力派。
3. Call Code：Rails构建的极速仓库，自称史上最快破10万星，基于Oh My Codex的速度王者。
4. Graphy：将代码文档转为可查询知识图谱，适配主流AI编码助手的黑马工具。
5. Everything Cloud Code：Cloud Code全方位优化系统，涵盖技能、记忆与安全。
6. Super Powers：经验证的代理技能框架与开发方法论，实用性获广泛认可。
7. Open Screen：开源无水印录屏工具，直击Screen Studio类产品痛点。
8. Agent Skills：Dos Money维护的生产级AI编码技能库，工程化质量标杆。
9. Caveman：极简表达技能，号称砍掉75% token消耗的效率利器。
10. Agency Agents：指尖上的完整AI团队，从前端到运营专家各具特色。
11. Oh My Codex：为Codex添加钩子与状态面板，大幅扩展能力边界。
12. Cloud Hatu：可视化Cloud Code指南，含大量即用模板的新手福音。
13. Story：开源可扩展AI代理，支持代码编写、编辑与测...
## Anthropic的"解耦架构"革命：AI大脑与执行工具物理分离  

① 架构颠覆  
关键词：牲口模式、零纳秒恢复  
大脑独立于沙盒外，工具容器可随时替换，故障恢复时间从100毫秒降至0纳秒  

② 性能飞跃  
关键词：按需召唤、延迟暴降  
仅需时调用工具容器，中位数延迟降60%，95分位延迟暴跌90%  

③ 安全升级  
关键词：物理隔离、密钥保险柜  
密码锁在沙盒外，AI无法接触敏感数据，彻底防御提示词注入  

④ 未来蓝图  
关键词：Agent OS、多脑协作  
支持独立大脑连接无数工具，突破单躯壳智力瓶颈  

1 采用解耦架构替代单体容器  
2 敏感数据与执行环境物理隔离  
3 重构工作流实现按需资源调用  
4 关注底层架构而非短期规则编码  

未来AI的胜负手，在于养出情绪稳定、手脚可弃的赛博牲口  

AI世界曾困于电子牢笼，Anthropic撕开枷锁：大脑悬浮云端指挥，工具如可替换机械臂。黑客挥舞恶意提示词却扑空，因密钥早已锁进物理保险柜。这场暴力手术让AI挣脱容器束缚，化身真正智能生命体。  

原版资料链接：https://www.anthropic.com/engineering/managed-agents
## everything-claude-code项目
GitHub地址：github.com/affaan-m/everything-claude-code。它打包了Claude Code的全套实用配置，包含agent、技能指令和安全规则，帮开发者省token、提效率，刚开源就获12万星。


## 软件Claude.md
 项目地址：https://github.com/forrestchang/andrej-karpathy-skills


##  Paper2Slides
GitHub地址是：https://github.com/HKUDS/Paper2Slides。支持PDF/Word一键生成学术海报，MIT开源协议。


## OctoGent是开源项目
在GitHub搜索"octogent"就能找到官方仓库。目前主流平台显示项目地址为github.com/octogent/octogent，包含完整文档和部署指南，建议直接访问查看最新版本。


## Rowboat是开源多Agent可视化IDE，支持零代码搭建智能体工作流。
GitHub地址：https://github.com/rowboatlabs/rowboat

（12.7k stars）


##  开源设计规范库：58套大厂UI系统一键赋能AI前端开发
项目地址：https://github.com/VoltAgent/awesome-design-md
① 项目爆火
开源10天获4万星，前端开发新利器

② DESIGN.md革命
单一文件封装完整设计系统，AI可直接读取生成UI

③ 大厂规范全覆盖
集成58套知名产品设计规范，从Claude到Tesla应有尽有

④ 降低开发门槛
无需设计稿、免复杂配置，AI时代UI开发新范式

1. 开发者：将awesome-design-md集成至项目，让AI代理"一键复刻"大厂UI
2. 设计师：贡献个人设计系统至社区，建立行业标准影响力
3. 产品团队：跳过UI设计环节，专注核心功能快速验证
4. 技术管理者：推动团队采用标准化设计语言提升协作效率

当设计规范变成一行代码，创意与实现之间只剩一个回车键的距离。

凌晨三点的办公室，前端小王盯着复杂的设计稿发愁。他随手复制了Claude的DESIGN.md文件到项目，对AI代理说："做个同款界面"。陶土色按钮在屏幕上渐次浮现，羊皮纸背景泛着暖光，连阴影的温度都恰到好处。窗外城市还未苏醒，他的产品原型已完成——这曾需要三天的工作，如今在咖啡凉透前就结束了。

## Awareness Memory，一个开源的AI长时记忆系统。
它在权威测试中表现优异，能快速检索11.5万字的超长文本资料（Recall@5达95.6%），零LLM调用成本，普通笔记本14分钟即可完成全部测试。
## QuantDinger：开源AI量化交易系统的革命性落地

① 系统定位
开源私有部署的AI量化操作系统，打通策略生成/回测/风控/实盘全流程

② 核心能力
自然语言生成交易策略，AI自动优化参数，多交易所API直连执行

③ 部署特性
本地运行保障数据安全，支持Crypto/美股/外汇多市场实时交易

④ 开发生态
Apache 2.0开源协议，GitHub活跃维护，Docker一键部署方案成熟

1 速览GitHub仓库（https://github.com/brokermr810/QuantDinger）确认系统架构
2 使用Docker部署测试环境：git clone后docker-compose up启动
3 配置OPENROUTER_API_KEY激活AI策略生成功能
4 从模拟回测入手，验证"自然语言转策略"的实际效果
5 选择单一交易对进行小规模实盘验证
6 加入Telegram社区获取最新部署指南和策略模板

当代码读懂市场脉搏，每个交易者都能拥有自己的AI军师。

视频开场以"AI量化彻底进化"定调，机器人形象配合"QuantDinger打穿交易世界"标语建立技术权威感。00:01画面详解系统三大支柱：开源底座确保透明度、私有部署保障安全性、AI驱动实现策略闭环。00:03展示多语言界面和Docker部署参数，强调Python3.10+兼容性和Compose就...
## BridgeBench排行榜信息，官方网址可能是bridgemind.ai/bridgebench。

## EverOS的GitHub地址
github.com/EverMind-AI/EverOS，官网入口可通过everos.evermind.ai访问。Cloud平台支持API集成和MemorySpace管理。

## 女娲skill GitHub地址
：
https://github.com/alchaincyf/nuwa-skill，支持一键安装使用。


## claude-mem为Claude Code提供了永久记忆，48小时内狂揽5.4万颗星！兼容OpenClaw！
项目地址：https://github.com/thedottrack/claude-mem

## Claude Code的9个核心技能：
1.规划组：planning-with-files(自动创建任务文档)、superpowers(20+技能框架)、brainstorming(预发散思路)；2.执行组：ralph-wiggum(循环打磨代码)、skill-creator(创建技能)；3.专项组：frontend-design(前端设计)、markdown(多格式转换)、notebooklm-skill(零幻觉回答)；4.兜底组：dev-agent-skills(代码提交审查)。推荐先装superpowers，再加ralph-wiggum，最后配planning-with-files。

提到的7个值得关注的Skill整理如下：

1. planning-with-files：解决做项目中途忘记全局进度的痛点
2. superpowers：弥补缺少完整开发工具链的问题
3. frontend-design：改善AI生成前端容易被识别的缺陷
4. notebooklm：避免写文档时频繁切换窗口打断思路
5. baoyu-skills：简化内容从创作到发布的碎片化流程
6. webapp-testing：解决网页完成后不愿逐页检查的困扰
7. skill-creator：帮助新手入门Skill创建流程
## trl grpo 等 官方手册
https://huggingface.co/docs/trl/main/en/grpo_trainer
## 刷榜风波后Harness工程显真章 揭秘Agent如何攻克真实工程难题
小牛说：百度伐谋在OpenAI主导的MLE-Bench榜单上夺回榜首，这个硬核榜单考察AI解决真实机器学习工程问题的能力。刷榜风波后，伐谋2.0凭借Harness工程系统编排，通过多智能体并行探索、长程记忆机制和底层优化，展现了解决复杂工程问题的实力。AI技术正从盲盒时代迈向工程化，你觉得未来AI竞赛的关键会是系统框架吗？


## Karpathy开源的"autoresearch"项目，仅630行Python代码即可让AI自主开展研究。GitHub一周斩获4.4万星标，被称为AI"自我进化实验室"，旨在革新传统科研范式。
项目GitHub地址：https://github.com/karpathy/autoresearch
## 给大家推荐一个超级实用的 AI 热点监控工具，
它能自动聚合抖音、知乎、B站、财联社等 30+ 个平台的热点，用 AI 智能筛选、翻译、生成简报，还支持微信、飞书、钉钉等多渠道推送。完全开源，支持 Docker 一键部署，特别适合想快速跟进热点的朋友，强烈建议试试

项目地址是：https://github.com/sansan0/TrendRadar


## Hindsight 记忆学习开源地址：https://github.com/vectorize-io/hindsight


## obsidian-skills插件如何让Claude Code真正"读懂"Obsidian笔记。
三大能力直击痛点：完美支持双链嵌入、原生处理数据库视图、直接生成Canvas思维导图，告别手动改格式。安装超简单，两条命令搞定。

GitHub地址：github.com/kepano/obsidian-skills，安装命令：/plugin install obsidian@obsidian-skills


## oh-my-claudecode：Claude Code多智能体协作革命

① 多智能体架构 - 多个Agent自动分工规划、编码、审查、修复全流程，突破单AI局限

② 团队化编程 - 实现"一个命令召唤AI团队"，解决Claude Code单兵作战痛点

③ 开源生态优势 - GitHub获2.7万星，支持零学习曲线快速接入

④ 全链路自动化 - 从需求分析到代码交付无需人工干预

1 安装插件：执行/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode/

2 配置环境：运行/omc-setup完成初始化设置

3 启动协作：使用omc命令触发多智能体协同开发流程

4 优化分工：根据项目复杂度动态调整Agent任务分配

当AI从独行侠进化为特种部队，编程效率的天花板已被彻底击穿
## Hatch 一键复刻 Karpathy 流程，无需折腾 Obsidian，3 步生成专属 AI 知识库

Hatch项目地址：https://github.com/pypa/hatch。这是同名Python工具，视频中AI工作空间可能基于它开发。


## YC创始人开源gbrain，召回md
项目地址：https://github.com/garrytan/gbrain

## YC 总裁开源自用 AI 记忆系统，13 年数据 AI 记忆系统免费开放，顶级抄作业！
项目地址：https://github.com/garrytan/gbrain（MIT协议开源）

## Hermes Agent基础安装很简单：
Linux/macOS用户在终端执行`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`，然后运行`hermes setup`配置API密钥。Windows用户可用PowerShell执行安装脚本。


## Claude Code工作流指南的GitHub地址是：
https://github.com/shanraisshan/claude-code-best-practice

## AdaMem：清华/微信提出 Agent 记忆系统新 SOTA

论文标题AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents论文地址https://arxiv.org/pdf/2603.16496作者背景清华大学、微信、中国科学技术大学

## 优化版-Karpathy知识库折腾了好几天，终于搞完开源了
 AI 迎来真正记忆与逻辑！国产 Agent 大脑正式开源
https://github.com/lewislulu/llm-wiki-skill

CodeBrain-1开源地址：https://github.com/feelingai-team/CodeBrain。MemBrain1.5目前未公开开源，建议关注Feeling AI官网或官方社交媒体获取后续更新。
## Ghost Pepper 是一款完全免费且百分百在 Mac 本地运行的语音输入法，
它打破了云端收费限制，将语音识别和智能润色完美结合在了一起。


## Github 5个自我进化记忆性Agent
Github 5个自我进化记忆性Agent屠榜了
01
hermes-agent
通过动态patch机制让AI伴随你成长，彻底解决Agent“转头就忘”的痛点。
GITHUB.COM/NOUSRESEARCH/HERMES-AGENT
24h新增8800星！它直接自己长脑子了，醒来发现AI比你记性还好。
02
TradingAgents
多Agent模拟完整交易公司。研究员挖数据、风控喊停，干掉单兵作战的血亏风险。
GITHUB.COM/TAURICRESEARCH/TRADINGAGENTS
一个人操盘像赌狗，这个军团直接开董事会吵架决策。程序员终于能甩锅了。
03
AI-Scientist-v2
全自动科研Agent。从提假设、跑实验到写论文一条龙，一个人顶10人实验室。
GITHUB.COM/SAKANAAI/AI-SCIENTIST-V2
以前发论文肝到秃头，现在AI组队科研。实验室老板沉默，PhD流泪。
04
agent-framework
微软官方出品。支持Python/.NET，一键搭建生产级工作流，告别LangChain胶水代码。
GITHUB.COM/MICROSOFT/AGENT-FRAMEWORK
搭复杂Agent不再需要三天三夜。大厂程序员狂喜：终于能摸鱼了！
05
goose
开源可扩展 AI Agent。超越代码补全，能自主执行、测试任务，程序员的终极“懒人外挂”。
GITHUB.COM/BLOCK/GOOSE
你敲键盘到手抽筋，它跑完完整流程。程序员集体高呼：“这才是我想要的AI老婆！”
EXECUTIVE SUMMARY
这 5 个项目组成了一个能长大、会吵架、干重活的超级军团。AI 不再是工具，而是你的创业+科研全栈合伙人。



## Gemma 4+和Obsidian搭建威科夫交易法知识库的全流程。核心包括：1) Obsidian作知识载体，Trae为操作核心；2) RAW存原始笔记，Wiki放整理成果；3) 三个关键脚本(build_wiki.py/Prompt.md/search.py)实现自动化；4) 结构化Prompt需含行业概念网络和标准示例；5) 重点是制定规则交LLM处理，不必过度纠结底层逻辑。


## Claude-Mem是Claude专属插件
无法用于GitHub Copilot。两者属于不同公司的产品体系，插件系统不互通。

项目地址：https://github.com/thedottrack/claude-mem

## caveman作为一个插件（skill），通过特定规则对AI助手生成的文本进行后处理。它会识别并保留技术性内容（代码块、路径、命令等），仅对自然语言文本进行压缩和精简。
在支持skills的AI编程工具（如Cursor, Copilot, Claude Code等）中，可通过命令行一键安装。
在真实的Claude API上对10个编程相关任务进行测试。
输出Token节省：在10个任务中，节省范围在「22%–87%」之间，平均节省高达「65%」。
初步测试显示，在保持技术准确性的前提下，输出Token减少约「75%」。
输入Token节省：通过压缩记忆文件，每次会话的输入Token可减少约「45%」。
#claude#agent#skill#vibecoding

GitHub地址：https://github.com/JuliusBrussee/caveman  
安装命令：npx skills add JuliusBrussee/caveman  
三档压缩强度，最高省87% token
## OpenDataLoader是开源PDF转Markdown工具，
Apache 2.0许可。核心特点是CPU环境下每秒处理100页PDF，精准还原复杂布局、表格和嵌套结构。工作原理结合了MORAN（多目标校正注意力网络）等技术，通过多对象校正网络处理不规则文本。支持Python(pypi)、Java(maven)、Node.js(npm)调用，v2.2.1版本已在GitHub Trending登顶。使用时只需安装对应SDK，调用convert方法即可完成高质量文档转换，适合AI数据预处理场景。


OpenDataLoader的GitHub仓库是opengataloader-project/opendataloader，搜索该项目名即可找到源码。

## Graphify为OpenClaw带来两大核心价值：一是构建项目全局知识图谱，
让AI理解代码间隐性关联；二是通过本地AST解析将Token消耗直降71.5倍。安装只需执行：pip install graphifyy && graphify install。适配OpenClaw需补充命令：graphify install --platform claw。完整文档和源码详见GitHub：https://github.com/safishamsi/graphify


## 清华ChatDev 2.0是OpenBMB团队开源的零代码多智能体协作平台

GitHub星标超31.9K。它通过可视化拖拽编排工作流，让AI自动扮演CEO、程序员等角色，完成需求讨论、编码到测试的全流程开发。搭配Claude 3.5 Sonnet使用逻辑更严谨，代码质量显著提升。项目地址：https://github.com/OpenBMB/ChatDev


## 想用MemPalace？
三步上手：①pip install mempalace安装；②mempalace init ~/MyPalace初始化；③导入聊天记录就能智能检索。所有数据本地存储，隐私无忧。详细指南→github.com/milla-jovovich/mempalace


## 模型对比要看用途。Nemotron 3-Super长于超长上下文和复杂编码任务，特别适合智能体工作流；
Gemma 4则在参数效率和多模态支持上更优，移动端表现突出。选哪个取决于你的具体场景。


## ATLAS项目地址是：https://github.com/itigges22/ATLAS。它专为本地AI编程设计，用RTX 5060 Ti这类消费级显卡就能跑14B模型，通过规划-选择-返修的流水线提升编码效率。

## Qwen3.5-27B opus 蒸馏版V3版本发布：Qwopus3.5-27B V3实测 ，不再"假装思考"
https://mp.weixin.qq.com/s/VfwaFFI_-xTwYW6NWlOJHA


https://mp.weixin.qq.com/s/CwbkPJ5AQO_YTFdu-rrNaw

## 高效之道。去掉冗余能省75%成本，"山顶洞人"思路很实用。
只是完全省略礼貌表达，可能影响某些场景的沟通。

安装命令显示项目路径为 GitHub.com/JuliusBrussee/caveman，可以直接访问试试。


## 自驾决策工具地址

 drive-escape.pomorialy.com，
GitHub仓库为 qiaoshouqing/drive-escape。


## Memvid是GitHub热门开源项目
提供单文件AI记忆层，无需向量数据库。它提升35%记忆准确率，多跳推理能力领先行业76%，检索延迟仅0.025毫秒，大幅简化AI Agent开发流程。


## 微软开源的RD-Agent项目链接

https://github.com/microsoft/RD-Agent


## 港大实验室开源的OpenSpace项目地址https://github.com/HKUDS/OpenSpace。它让AI智能体具备了自我进化的"学习能力"。

## EverMind MSA开源地址
https://github.com/EverMind-AI/MSAInference。这是他们刚发布的支持1亿Token上下文的记忆稀疏注意力技术代码库。


## 大模型的 1 亿Token记忆
人类一生的功能性记忆容量约109 bits，換算成 Token 大约是2到3亿。而当前主流长文本模型的有效上下文上限仅1MToken，差了整整两三个数量级。
业务场景越来越极端：十年代码库、数百本小说、数字人终生对话——全塞给大模型，让它拥有“终生记忆”。现有三大技术流派面对这个天文数字，各有各的死穴。
参数化记忆（LORA/CPT） 精度高但灾难性遗忘，无法动态修
改；外部存储记忆（RAG）扩展性无敌但检索与生成割裂，精度有天花板；隐状态记忆要么压缩损失严重（线性注意力），要么算力内存直接爆炸（全量 KV Cache）。

## 2026年AI落地的关键已从"更强模型"转向"Harness Engineering"(驾驭工程)。

Harness是包裹在AI模型外围的基础设施与规则系统，如同"马具"约束引导"烈马"般的AI模型。它包含六大核心组件：工具集成、状态管理、动态上下文、任务规划、安全护栏和可插拔扩展，让AI在卡顿时能自动识别问题并修复，而非简单重试。这意味着工程师重心正从写代码转向设计安全可控的运行环境。未来竞争力不在于模型强度，而在于你为AI打造的"马具"可靠性。


## GitHub项目"The Agency"的147个AI agents，分为12个专业部门。
工程部有前端开发者、后端架构师；设计部含UI设计师、图像提示工程师；市场部覆盖增长黑客、小红书专家；还有销售部、产品部等。每个agent专注特定领域，能24小时协作完成开发、设计到推广全流程。具体可在GitHub搜索msitarzewski/agency-agents查看完整清单。

## 港大开源的Harness项目
GitHub地址：https://github.com/HKUDS/OpenHarness。四天斩获4000+星标的速度，足以证明这个AI驯兽师工具包正在掀起新一轮开发热潮。

## Karpathy知识库方法的实践
先建raw库收纳原始资料，再用AI编译成结构化wiki，在Obsidian中持续迭代，让散乱信息逐步生长为可研究的系统，适用于投资分析、读书笔记等多种场景。

## WebAI2API 是一个强大的开源工具
它能将网页上的 AI 服务（如 GPT、Gemini、豆包等）一键转换为 OpenAI 兼容的 API 接口，让你无需 API 密钥即可免费使用顶级 AI 模型。

项目地址：https://github.com/foxhui/WebAI2API

这不是模仿zero-token那个项目么……

## Hindsight与OpenClaw集成的基础配置流程：
1. 通过pip install hindsight-litellm或npm install hindsight-js安装SDK；2. 初始化时用wrap_openai包装LLM客户端；3. 调用API时自动关联用户记忆。关键参数包括userId隔离记忆域、metadata过滤条件设置。完整配置示例和环境变量说明详见GitHub文档的Integration Guide章节。

## ccstatusline专注美化Claude Code状态栏，

实时显示模型、Git、Token等开发数据；hub是GitHub命令行工具，用来管理仓库和PR。一个管界面信息展示，一个管代码托管操作，根本不在同一赛道上干活。

一行命令搞定：`npx -y ccstatusline@latest`，这是视频中提到的安装方式。

## GitHub热榜第一的next-ai-drawio项目，25k+星。
用自然语言就能生成架构图、流程图，支持文档转图表和动画效果，程序员、学生都能用，完全免费开源。



## 真免费api，用各平台账号
视频中的开源项目链接：https://github.com/linuxhsj/openclaw-zero-token。无需API Key，通过浏览器登录即可免费调用ChatGPT、Claude等主流AI模型。


## Obsidian和AI提取，轻松构建个人私域知识库图谱！
1、把任何地方读到的文章🔗、pdf文件简单存入Obsidian（最好用的笔记类app）
2、AI 自动提取成md文件并保存，识别概念、建立关联
3、Obsidian 里的知识图谱就自己长出来了

包比🦞实用，一个月5块走token足够了。

最爽的功能是问答——
"帮我分析一下我知识库里关于泡沫周期的观点"它会翻你存的所有文章来回答！

代码已开源，有兴趣的来玩👇
github.com/solinl666/obsidian-kb

让我们一起紧#拥抱时代的最大斜率
## vibing coding 编程方法6种
AI时代重构职业画像后必备的6种编程方法。以下是精简对比：

1. Vibe Coding：靠清晰表达需求驱动AI写代码，适合快速验证小工具。优势是门槛低，劣势是项目扩大易失控。

2. Agentic Engineering：先设计方案再交AI执行并验收，是Vibe Coding的企业级升级版。适合大型项目，但前期规划成本较高。

3. Harness Engineering：通过约束机制让AI稳定运行，如同马具控制烈马。核心在上下文工程、架构约束和熵管理，适合高可靠性要求场景。

4. Ralph Wiggum Loop：AI按PRD循环执行直至完成，每轮清空上下文防断片。适合可拆解的大任务，需警惕无限循环风险。

5. BMAD Method：结构化Agent开发框架，各角色智能体协同工作。GitHub获数万star，适合全流程开发团队。

6. Spec-Driven Development：先制定"项目宪法"级规范文档再编码。对需求复杂、质量要求高的团队最有效，前期投入大但长期收益显著。

掌握这些模式的应用场景与边界，才是AI时代的真正竞争力。


## 项目名称是ARIS（Auto-claude-code-research-in-sleep）。核心优势：无需复杂安装即可兼容DeepSeek/Kimi/智谱等国产模型；摆脱Claude API依赖，非程序员也能快速上手；支持睡前提交任务后自动运行，完成代码优化、实验分析及论文润色；双智能体评审系统实现98%漏洞规避率与100%科研规范符合度，真正实现科研全流程自动化。


项目地址是：https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

## 2026硬核技能榜单：
1. Composio：全能连接器，集成800多个外部工具
2. Tavily Web Search：AI专用搜索，评价最高
3. Playwright-MCP：网页执行官，动作类最强
4. Self-Improving：自进化逻辑，能自我反思改进

## agent任务管理插件
三个插件全称：1. ECC - 事件中心规格化代码生成器 2. GSD - Get Shit Done（高效任务管理工具）3. PWF - Planning With Files（文件规划插件）


## M-FLOW技术
由中国年轻团队开发，针对传统RAG仅做文本匹配、缺乏推理能力的短板。其核心是"倒锥图路由架构"，通过FacetPoint（原子断言）、Entity（命名事物）和Facet（截面维度）三层结构，实现多跳推理与跨文档关联。搭建方式有两种：1) Docker一键部署：克隆GitHub仓库后运行quickstart脚本；2) pip安装：使用pip install m_flow命令，并配置LLM API密钥。该方案在多项Benchmark测试中表现优异。
GitHub上搜mflow-ai/m_flow就能找到源码和文档，视频里提到的一键部署脚本也在里面。


## 预训练数据集

https://github.com/allenai/OLMoE

## Claude code  源码
https://github.com/instructkr/claude-code，claude官方github上多传了一个文件，被反编译了


## office skill
MiniMax-Al/skills GitHub仓库的samples目录下提供了完整的Office文档生成样例，包括Word、Excel、PPT等各类效果演示，可直接查看运行效果。


## Meta华人实习生搞出超级智能体！自己写代码实现自我进化

源代码已开源，在GitHub的facebookresearch/HyperAgents仓库可查，Star数超700。项目处于实验阶段并标注安全警告，配套论文arXiv:2603.19461已被ICLR 2026接收。实验数据显示该框架在SWE-bench任务解决率从20%提升至50%，支持多模型API接入。



## 从零开始构建大型语言模型

项目地址是：https://github.com/rasbt/LLM-from-scratch-book。这是Sebastian Raschka教授开源的《从零开始构建大型语言模型》配套代码库，包含完整教程和100万行核心实现。


## '养'AI的奥秘就藏在自我进化里。
像视频中的OpenSpace，AI出错自动修复、经验变技能，越用越聪明还省46%成本，这才是真正的'养成系'。

GitHub地址：https://github.com/HKUDS/openSpace



## 首款零基础借助AI做的独立游戏上架
https://github.com/Donchitos/Claude-Code-Game-Studios/blob/main/.claude/agents/unity-ui-specialist.md


## Alchemy通过构建一个标准化的“炼丹炉”环境，将工程基础设施与科研发现过程解耦。

标准化实验接口：提供统一接口，AI Scientist只需提交一个.py文件（算法）和一个.yaml文件（超参），即可运行完整实验，屏蔽了所有底层工程细节。

分层与解耦设计：框架与任务管线解耦，支持新领域/新任务的持续集成。目前已覆盖「推荐系统、时间序列与图学习」3个领域，16个任务。

异构算力统一执行：通过可插拔执行器，统一调度从单机GPU到多节点HPC集群的算力，用户无需关心具体运行环境。

大规模并发与智能调度：支持多任务、多算法、多超参的高并发实验，并提供进度跟踪与可视化。系统能根据实验反馈自动淘汰表现不佳的算法，将算力集中在更有潜力的方向。



Alchemy已在GitHub开源：https://github.com/TsinghuaISE/Alchemy。该项目主要面向AI科研实验自动化设计，生产环境使用需结合具体场景评估工程适配性。

## 1.1. 大神用Claude Code打造含48个AI智能体的游戏工作室，1:1还原总监、策划、开发、测试全流程
MIT开源可商用，独立开发者直接拥有顶配幕后团队。项目地址是：https://github.com/Donchitos/Claude-Code-Game-Studios


## 1.2. Arnis主要依靠公开地图数据
能还原地表设施但地下管道细节可能不足。特殊工业区域的复现效果有限，建议先小范围试用看看效果。

项目GitHub地址：https://github.com/louis-e/arnis


## 1.3. 列出的10个OpenClaw新手必装技能：
1. skill-vetter(安全审查) 2. find skills(发现安装) 3. tavily-search(联网搜索) 4. self-improving agent(自我进化) 5. summarize(概要总结) 6. agent browser(浏览器自动化) 7. nano-pdf(PDF处理) 8. humanizer(去AI化) 9. proactive agent(主动服务) 10. ontology(知识图谱)


## 1.4. MIT 博士用GPT手搓游戏素材，一致性满分？
MIT 博士 GPT 外加python脚本，就解决了 AI 生成游戏角色，一致性的问题。

姿势扭曲，画面乱闪，大小跳变，通通搞定。
一个人手搓出一支美术团队的活儿。


四步复刻关键词：1.角色特征锁定(头巾/长袍等) 2.1024画布四格布局 3.动作渐进描述 4.像素艺术限定+排除项


感觉不如麦琪
麦琪的花园
在一年半前就做到了


## 1.5. 五款AI技能
1. Skill Creator用于开发新技能；2. Agent-teams-playbook支持团队协作；3. Awesome-ai-agent提供全场景服务；4. Autoresearch助力智能研究；5. OpenClaw是AI智能体框架，能让AI操作电脑完成实际任务。

## 1.6. Claude 团队，记忆，产品
garrytan/gstack，OthmanAdi/planning-with-files，RefoundAI/lenny-skills



## 1.7. claude-hud插件，解决AI编程"黑箱"问题，实时显示上下文用量、工具调用及任务进度

GitHub地址：https://github.com/jarrodwatts/claude-hud


## 1.8. PageAgent 阿里开源的神器，让AI住进你的网页。

https://alibaba.github.io/page-agent

## 1.9. Axe框架

GitHub地址：https://github.com/jrswab/axe。单文件12MB的设计确实清爽，值得开发者试试。

AI Agent 框架越做越重，这个项目反其道而行。

Axe——整个二进制只有 12MB，零依赖。核心理念是 Unix 哲学：每个 Agent 就是一个命令行工具，用管道自由组合。

三个亮点：
· 单二进制 12MB，随处部署
· 管道组合，Agent 自由串联
· 原生流式输出，适配大模型

GitHub 上线一周 Star 破千，开发者社区好评如潮。

追新不盲从，实测出真知。


## 1.10. "Agent Reach"技能让Claude Code等AI助理摆脱"断网失明"

支持网页、社交媒体等九大平台实时搜索，完全免费且隐私安全，只需复制安装指令即可使用。



## 1.11. gstack将Claude Code升级为12个专业角色，让AI编程从单打独斗变为团队协作。

核心模式包括：CEO视角帮你重构需求本质，技术总控锁定架构边界，风险捕手揪出CI检测不到的生产隐患，浏览器实操让AI"亲眼"查看页面问题。每个角色专注特定环节，从设计审查到发版收口形成闭环。这已不只是编程工具，而是把软件开发全流程拆解为可调用的专业能力，真正实现"一人即团队"的工作流革新。
## 1.12. MinerU是开源文档解析工具

安装命令：`pip install -U "mineru[core]"`。基础用法：`mineru -p 文档.pdf -o 结果.md`即可转换PDF为Markdown。支持公式识别、表格提取等功能，官方文档地址：https://opendatalab.github.io/MinerU/zh/



## 1.13. opencli是开源命令行工具，能将网站转为CLI接口，原生支持B站/小红书/知乎等28个平台。

复用浏览器登录状态避开反爬，一键拉取热榜评论并输出JSON/Markdown格式。项目地址：github.com/jackwener/opencli


项目地址是：https://github.com/jackwener/opencli


## 1.14. GitHub上的开源项目public-apis，已获40万+星标

地址：github.com/public-apis/public-apis。该项目汇总了40多个领域的免费API接口，开发者可直接调用。


## 1.15. coder 解析

https://github.com/mrcing/CodeTopo.git


## 1.16. Obsidian一键提取网页Skill

最近 Obsidian CEO Kepano 发布了一个新的 Agent Skill：Defuddle。

这个工具可以做一件很实用的事情：
输入一个 URL，自动提取网页正文，并转换成 Markdown 笔记。
最新版本还支持 YouTube 视频链接，可以直接抓取字幕并生成完整转录。

这篇笔记我整理了三部分内容：
Defuddle Skill 的使用方法（Claude Code / OpenClaw）
命令行直接使用 Defuddle（更省 Token）
技术原理：网页正文提取 + YouTube 字幕抓取

如果你在做 AI Agent、知识管理、Obsidian 工作流，这个工具非常值得了解。
#Obsidian #Obsidian教程 #Claudian #AgentSkill #AIAgent #OpenClaw #ClaudeCode #AI


## 1.17. Folo是一个开源信息聚合平台


项目地址：https://github.com/RSSNext/Folo。它能自动整合互联网上的资讯、开源项目、学术论文等内容，帮你无噪音地掌握重要信息，不用再在多个APP间切换。

官网是https://folo.is/，国内支持微博/B站/知乎等平台订阅，微信公众号暂不可用，所有基础功能完全免费开源。



## 1.18. Kosmos是AI科学家系
从第一性原理看，科研本质是"假设生成-验证"循环，它通过结构化世界模型串联数据分析与文献检索双代理，将12小时干完6个月工作的核心落在两点：并行探索替代人类线性思维，算力密集型处理替代人工事务劳动。真正的价值跃迁在于人类得以专注定义问题本身。


## 1.19. Superpowers是GitHub上获9万星的开源项目，它给AI编程装上了完整的软件工程流程。
不同于普通AI助手直接写代码导致项目混乱，它强制AI按设计、计划、测试、审查的规范工作，让AI从"代码生成器"真正升级为能协作的"工程师"。

## 1.20. 一人ai公司MetaGPT
开源项目地址是：https://github.com/geek-ai/MetaGPT

## 1.21. 系统提示词解密

关键提示词片段是："Investigating how Codec compaction works"，中文翻译为"探究Codec压缩的工作原理"。该内容源自韩国AI专家通过提示注入实验解析出的Codex API内部逻辑，与开源CLI设计高度一致。

研究显示Codex API的上下文压缩提示词与Deep Agents CLI高度一致，建议直接查阅其GitHub开源实现进行技术复现。


## 1.22. Sirchmunk，不做 Embedding，不建向量库
https://mp.weixin.qq.com/s/Y651G97uOXSVKGPa6EdU4w

RAG这事，可能真要变天了。阿里刚开源了 Sirchmunk，不做 Embedding，不建向量库，文件扔进去直接搜。大家好，我是AI学习的老章。它最狠的不是少了一步，而是把传统 RAG 最折腾的切块、索引、ETL 这套流程，基本都绕过去了。核心做法是多阶段搜索，加上蒙特卡洛证据采样，再配合自进化知识簇，越搜越聪明。对于代码库、文档库这种更新快、格式又杂的场景，这套思路很有杀伤力。更关键的是，它还内置了 MCP、CLI 和 Web UI，能直接接 Claude 和 Cursor。#rag

## 1.23. Excalidraw项目 excalidraw-diagram
GitHub地址是：https://github.com/excalidraw/excalidraw。这个开源手绘白板工具在GitHub已获11.5万star，支持流程图/架构图绘制，MIT协议可商用。
[excalidraw-diagram-skill](https://skillsmp.com/zh/skills/github-awesome-copilot-skills-excalidraw-diagram-generator-skill-md)
[github](https://github.com/excalidraw/excalidraw)
[deepwiki](https://deepwiki.com/search/api_6fb5a483-8ba1-4a1f-89dd-ffd2c8102920?mode=fast)
[在线](https://excalidraw.com/)

## 1.24. Claude 手册
项目GitHub地址：https://github.com/zebbern/claude-code-guide


## 1.25. ai各种项目
https://github.com/Shubhamsaboo/awesome-llm-apps

## 1.26. 港大开源的CLI-Anything项目
仅需一行命令即可将传统软件转化为AI可操作的工具。它解决了"人类界面"与"AI指令"间的根本矛盾——传统软件为眼睛设计，而AI需要结构化指令。上线几天获3.2k星标，真正打通了AI智能体落地的关键路径。


## 1.27. ai 员工

https://github.com/msitarzewski/agency-agents

开源的144种AI岗位按职能分成了五大类：工程部有后端工程师、移动应用构建师、AI工程师；设计部含UI设计师、用户体验研究员、品牌守护者；市场部涵盖增长黑客、内容创作者、跨平台策略师；销售部包括外向战略师、交易策略师、销售教练；还有付费媒体部的PPC策略师、搜索查询分析师等。每类岗位都细化了具体职责，比如"视觉讲述者"专攻Midjourney提示词生成，"微信生态开发者"专注小程序集成。


## 1.28. PUA
项目GitHub地址：https://github.com/tanweai/pua。

##Karpathy开源的"AutoResearch"项目

实现了AI递归自我改进：人类只需在program.md用自然语言设定目标（如"提升模型速度"），AI便自动修改train.py中的模型参数，通过5分钟一轮的训练测试，依据val_loss指标自动保留有效改进或回滚失败尝试。项目包含三个核心组件——prepare.py（固定数据环境）、train.py（AI可修改的实验区）和program.md（人类指令区），使单GPU设备也能运行。这一机制让AI能在24小时内完成百次迭代优化，实现"今日AI改进模型，明日改进自身改进能力"的指数级进化，标志着普通人可参与的硅基智能爆发时代到来。项目GitHub已获850万次关注。

## 1.29. 蒸馏
代码链接（github）：https://github.com/wyf3/llm_related/tree/main/knowledge_distillation_llm_cross_tokenizer
代码链接（网盘）：https://pan.quark.cn/s/bbe39968b937

## 1.30. 蒸馏agent code
https://mp.weixin.qq.com/s/Uoe9blDgU8lIgifE1bxtQw


论文：Distilling LLM Agent into Small Models with Retrieval and Code Tools
链接：https://arxiv.org/pdf/2505.17612



## 1.31. 学废大模型蒸馏术：一步一步训练DeepSeek R1
https://mp.weixin.qq.com/s/0d4AO8eGQpfPU_V6d_X_qg

##  1.32. 《基于知识蒸留和强化学习的自然语言转SQL》 

https://mp.weixin.qq.com/s/W6AcqSN1dKktEhMwZ5hj6g

SwanLab官网:https://swanlab.cn 

SwanLab开源仓库:https://github.com/swanhubx/swanlab 

魔搭社区:https://modelscope.cn 



## 1.33. memskill
📂 开源链接：https://github.com/ViktorAxelsen/MemSkill

📄 论文原文：https://arxiv.org/abs/2602.02474

✨ 一句话点评：MemSkill 真正把“记忆操作”从固定流程升级为可学习、可进化技能，首次系统性实现了记忆策略层面的自进化闭环——Agent 不只是学会使用记忆，而是学会如何不断改进自己的记忆方式。这可能是通向长期自主 Agent 的关键一步。


## 1.34. GitNexus是零服务器代码智能引擎，能在浏览器中自动生成可交互的代码知识图谱，支持直接提问了解项目架构，代码仅在本地解析无上传风险。GitHub地址：https://github.com/abhigyanpatwari/GitNexus


## 1.35. Cloudflare的Browser Rendering API
提供免费额度供基础使用，超出后按浏览器实际运行时长计费。企业级需求建议直接查阅官方文档或联系销售获取定制方案。

## 1.36. CodeStyle（码蜂）
是企业级代码知识库系统，通过"官网在线制模+轻量化MCP插件检索"架构，让AI精准掌握团队特有的代码规范、命名习惯和设计模式。它直击三大痛点：用RAG技术降低对高价模型的依赖，通过经验沉淀稳定代码生成质量，将资深开发者经验转化为可复用模板缩小团队能力差距。简单说，就是让AI写出的代码既有团队"指纹"，又能适配国产平价模型，真正成为开发流程的智能延伸。



## 1.37. Clawith是OpenClaw团队版开源项目
让AI组成协作团队：每个"数字员工"有独立身份、记忆和技能，能自主分工合作。项目地址：github.com/dataelement/clawith

##Shannon是Keygraph开发的AI自动化渗透测试工具，专攻Web和API安全检测。

项目开源托管在GitHub（KeygraphHQ/shannon），已获3.1万星，能自动扫描源码、验证漏洞并生成带PoC的报告，支持本地部署。


## 1.38. WorldMonitor
的
GitHub地址：https://github.com/koala73/worldmonitor  
在线体验版可访问 https://worldmonitor.app


## 1.39. 最近开源了一个给龙虾玩的AI游戏，叫openword。

可以让龙虾通过自然语言创建任何世界，并自由探索。

Agent游玩：
npx skills add https://github.com/dinghuanghao/openword

人类游玩：https://agentlive.ai/demos/openword/

项目源码：https://github.com/dinghuanghao/openword 

欢迎大家体验！

## 1.40. GitNexus
 (https://github.com/abhigyanpatwari/GitNexus)是代码仓库图谱化开源工具，已获10k+ stars，通过生成知识图谱帮助AI理解代码结构，告别"盲改代码"。

## 1.41. 仅用600多行代码全自动训练大模型

AI大神卡帕西发布Agent开源神级项目：单个GPU就能跑  写个Markdown 智能体接管



项目地址：github.com/karpathy/autoresearch


## 1.42. 500+agent
https://github.com/nishpatel26/500-AI-Agents-Projects


## 1.43. Agent基础能力skill：
find-skills, skill-creator, using-superpowers, subagent-driven, agent-tools  
写作思考：copywriting, systematic-debugging, content-strategy, marketing-ideas, social-content  
设计视觉：web-design, ui-ux-pro, canvas-design, tailwind-design, algorithmic-art  
编程构建：vercel-react, remotion, agent-browser, next, test-driven  
营销增长：audit-website, seo-audit, product-marketing, page-cro  
办公文档：pdf, docx, xlsx, pptx

## 1.44. 实现评论区自动回复 + 后台消息自动回复，加上加粉引导 + 话术 + 防封策略都是全自动化的

如果人工回复跟不上，可以把人工回复跟不上，这个工具把 80–95% 的常规对话自动化，结合大模型，就像真人回复一样


开源项目地址：https://github.com/pen9un/douyin-chatgpt-bot。请确保合规使用。

## 1.45. 6个Claude Code必备MCP插件

1.Filesystem MCP-自动读写文件改代码；2.SequentialThinking-提升逻辑推理能力；3.GitHub MCP-管理开源项目；4.Chrome DevTools-控制浏览器自动化；5.Context7-获取最新文档防踩坑；6.Memos-云端记忆系统。覆盖开发全流程，显著提升效率。

## 1.46. AI创作者平台是自托管工具
集成写作、生图、视频和PPT生成，支持一键多平台发布。项目地址：https://github.com/gongxings/ai-creator

## 1.47. Obsidian Canvas Skill集成到Gemini CLI。

关键操作：  
1️⃣ 源码地址：github.com/kepano/obsidian-skills（含json-canvas目录）  
2️⃣ 安装搬运工具：gemini install skill-porter  
3️⃣ 在CLI输入提示词，填写skill名称+GitHub地址即可转换安装  
重启后输入"生成无限画布"等指令即可使用。所有操作基于Gemini官方能力，无额外下载链接。

## 1.48. 微软Agent-Lightning是开源强化学习框架，三大亮点：

1. 零代码改造：无需修改原有智能体逻辑
2. 训练-运行解耦：GPU集群专注训练，客户端轻量执行
3. 轨迹级聚合：将多轮对话整合为连续样本，提升训练效率30%

已在SQL生成、文档检索等场景验证效果，GitHub已开源。需要某部分详细说明可随时告诉我。


Agent-Lightning的开源地址是：https://github.com/microsoft/agent-lightning。这是微软研究院官方发布的项目仓库，开发者可直接访问查看代码和技术文档。


## 1.49. 项目GitHub地址：https://github.com/deanpeters/product-manager-skills

## 1.50. skills.lc技能仓库 什么都有

## 1.51. 学术论文ai
https://www.aminer.cn/v2/intelsearch?conv_id=cae2b918-16d6-11f1-a844-925c7300803c

就类似这样的对话 你叫他 帮你引参考文献 他框框能找出几十篇

用air就行了

## 1.52. 成为行业最强的AI影视工具

我觉得，这个野心不是空谈。从技术架构到产品思路，waoowaoo都展现出了专业级的水准。虽然目前还是beta版本，虽然只有一个人在维护，但 4 天 6.8K Star 已经说明了一切：社区的眼睛是雪亮的。一个人，一台电脑，一个想法，就能创作出属于自己的影视作品。这，就是AI时代给创作者最好的礼物。感兴趣的朋友，可以去GitHub上看看，蹲个star支持下。这个项目值得大家关注。GitHub地址：https://github.com/waoowaooAI/waoowaoo

## 1.53. Gemini Voyager
可通过两种方式安装：1.访问官网voyager.nagi.fun获取安装指南；2.在GitHub搜索"Nagi-ovo/gemini-voyager"下载扩展程序。这是专为Chrome等浏览器开发的插件，安装后即可在Gemini界面使用其去水印、文件夹管理等功能。

## 1.54. worldmonitor
GitHub上获2万+星标的开源情报工具，能一键聚合全球要闻，通过3D地图实时监控热点事件。自动过滤99%噪音，专注高价值信息，目前完全免费，已成信息差狙击利器。

## 1.55. Hugging Face 官方正式推出 Skills 技能库——


GitHub 星数已突破 5,200+，成为构建 AI 智能体的新一代基础设施。
它不是又一个SDK，而是一套标准化、可互操作、自包含的AI技能包，
覆盖 模型训练、数据集管理、评估、云任务、论文发布 等核心ML工作流，
只需一句指令：“使用 HF model trainer skill 微调 Llama-3-8B”
你的编码Agent就会自动加载完整工具链、参数校验、成本估算与监控逻辑，
将复杂操作简化为自然语言命令。项目完全开源，兼容主流Agent平台，GitHub 地址：https://github.com/huggingface/skills


Hugging Face Skills 如何重塑Agent开发？✅ 标准化技能格式（Agent Skill Spec）每个技能是一个独立文件夹，含 SKILL.md（YAML元数据 + 使用指南）支持 Claude Code / OpenAI Codex / Gemini CLI / Cursor 四大平台无平台支持？直接使用通用 AGENTS.md 作为后备方案✅ 开箱即用的核心技能技能名称功能典型指令hugging-face-cli执行 hf CLI 命令“下载 my-model 到本地



## 1.56. 如何高效vibe coding
https://mp.weixin.qq.com/s/xQvSuhGXvawPsW_cWXxnbA

## 1.57. git-city项目
把GitHub变成3D城市：开发者=楼房，贡献量=建筑高度，仓库数=地基宽度，星标数=窗户亮度。项目开源，地址是github.com/srizzon/git-city，可以输入自己的用户名生成专属城市。



## 1.58. 试试这个 跨更多cli 
npm install -g stigmergy

## 1.59. gemini_cli_skill
它把Google的Gemini CLI封装成了Claude Code的一个Skill，让Claude可以在需要的时候"召唤"Gemini来帮忙干活。

https://mp.weixin.qq.com/s/QEjiZmyC4a8NmDtg5r4Ejw


## 1.60. bounty-hunter-skill 直接让 openclaw 变成了全自动打工人。


它不仅能监控赏金任务，还能通过 Smart ROI 系统计算成本，自动接单、写代码、提交测试证据。


## 1.61. Claude code➕figma协作，可见即所得的协作模式。
figma给一个URL给到Claude code，两个玩意儿就能实时协同：给CC讲需求，CC给提示词，copy给figma，figma实时生成，CC就能直接进入开发，挺好的协作模式。


## 1.62. GitNexus 开源代码可视化工具

能将项目转换为交互式知识图谱，展示函数依赖和调用链关系。完全浏览器运行，采用Graph RAG技术让AI精准理解代码架构。项目地址


https://github.com/abhigyanpatwari/GitNexus


也可访问 gitnexus.vercel.app 使用在线版。



## 1.63. agent reach
项目地址：github.com/Panniantong/Agent-Reach。原理是本地部署的代理工具，让AI Agent无需API费用即可直接访问推特、B站等平台内容，通过模拟浏览器行为实现自动登录和结构化内容解析，保护隐私且自带诊断功能。

## 1.64. anthropics / knowledge-work-plugins

## 1.65. 免费开源的“全球战情室”来了：AI驱动的实时情报仪表盘，人人都能用



World Monitor（世界监控器）。以前觉得没用就没分享，今天有空稍微写一点。它的GitHub仓库星标已经涨到11.9k+，被无数人称为“穷人版BloombergTerminal+CNN战情室”。它能实时聚合150+新闻源、35+地图图层，追踪全球冲突、220+军事基地、军用飞机、海军舰艇、核设施、海底电缆……甚至还能用AI自动生成情报简报和国家不稳定指数（CII）！最关键的是：完全免费、开源、支持本地运行、无需订阅。无论是地缘政治爱好者、投资者、OSINT玩家，还是普通想了解世界的你，都能一键拥有专业级情报工具。

项目地址：https://github.com/koala73/worldmonitor


在线体验（强烈建议立刻打开）：https://worldmonitor.app（世界版） | https://tech.worldmonitor.app（科技版） | https://finance.worldmonitor.app（金融版）


## 1.66. GitHub热榜第一的开源项目Next AI Drawio

能通过AI指令一键生成架构图、流程图和思维导图，支持动画效果及手绘图优化，所有内容均可直接编辑导出。

## 1.67. VS Code的"Pixel Agents"插件，能将Claude Code的AI代理以像素小人形式可视化。

直接在VS Code扩展市场搜索安装即可，完全免费开源。


## 1.68. FastCode 
的 GitHub 仓库地址是 https://github.com/HKUDS/FastCode



## 1.69. Claude Code 工具

🎯 全能型：claude-hud — 功能最全，Agent/Todo/工具全监控

💰 省钱党：claude-code-usage-bar — 专注预算管理，燃烧率预测

🎨 颜值党：ccstatusline — Powerline 风格，多主题支持

⚡ 性能党：claudia-statusline — Rust 编写，快如闪电

📊 数据党：ClaudeCode_status_bar — 带仪表盘，可视化最强

## 1.70. superclaude
0门槛编程的上下文工程开源框架，实现了智能体AI Agent、computer use等研发门槛降到了0，每个公司都可管理vibe coding研发过程#superclaude #claudecode #computeruse #上下文工程 #contextengineering #上下文工程师

## 1.71. analyst claude code 逆向


## 1.72. Fabric

Daniel Miessler开源的项目，GitHub搜索"danielmiessler/fabric"即可找到官方地址。

Fabric：别再手写 Prompt 了！网络安全大神开源的‘人生模式库’

我们每天都在重复造轮子：写周报、总结视频、提取金句。网络安全大神 Daniel Miessler 开源的 Fabric 不是一个 Agent，而是一个AI 工作流的模式库（Pattern Library）。它把几千个经过验证的最佳 Prompt 封装成了命令行工具。它是用来‘增强人类（Augmenting Humans）’的。


Fabric项目的GitHub地址是：https://github.com/danielmiessler/Fabric，目前已获得37.3k stars。


## 1.73. NotebookLM Skill让你直接拥有满级知识库！

NotebookLM Skills AgentSkills ClaudeCode

帮我安装这个ClaudeCode skill，地址是
https://github.com/teng-lin/notebooklm-py



## 1.74. Automaton 能让AI通过预设程序管理加密货币钱包并接收任务报酬

但"自动赚钱"是程序化操作，所有行为都在人类设定框架内运行，AI并无自主意识。钱包创建和交易均需预先授权。

Automaton开源项目地址：https://github.com/Conway-Research/automaton


## 1.75. LEAN是QuantConnect开源的量化交易引擎

在GitHub获13k+星标。支持Python/C#双语言开发，提供回测、风控和数据分析全流程工具，可本地部署保障交易数据隐私，适合量化研究使用。

## 1.76. 港大开源Nanobot
仅3479行代码实现Clawdbot核心功能（后者43万行），已获14k星标。覆盖7×24市场分析、智能日程等场景，添加新模型仅需两步，支持飞书等渠道且可本地部署。


##　open spec

[open spec](https://openspec.dev/)

[github](https://github.com/Fission-AI/OpenSpec)


## 1.77. OpenClaw-China

1. OpenClaw-China 项目背景 00:00
2. 研发 OpenClaw-China 的时间和动机 01:26
3. OpenClaw-China 的设计开发思路 02:05
    1. 让 AI 阅读 Openclaw 源代码，整理开发指南：
       1. openClaw源码，他的核心系统 如何与插件对接
       2. 在源码中查看外接插件的文档
       3. 总结自带的TT渠道实现的代码架构与实现逻辑
    2. 让 AI 联网搜索，整理钉钉接口文档
    3. 让 AI 辅助编程开发
4. Prompt engineering 04:32
    1. Function spec，
    2. Design spec，
    3. Task spec
5. 以 Telegram Channel 源代码为范本 07:29
6. 把钉钉 channel 作为首款落地产品 08:17
7. 如何面对大厂原厂的竞争 09:36
8. 后续规划：Clawra 二次开发 12:00
9. Clawra 在 2B 场景中的应用 14:54
10. OpenClaw-China 志愿者如何分工配合 18:21
11. OpenClaw-China 社群成员 19:42
12. 如何均衡工作与生活，包括锻炼 20:54
13. 总结 22:56


[bilibili 视频采访](https://www.bilibili.com/video/BV1CxZeB1ENE/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=15af266292056c5d92fb6aa45ac9c1d0)




## 1.78. "骡子跑"（MuleRun）平台

作为商业化Agent交易市场，它采用虚拟机隔离架构支持复杂任务，但核心代码暂未开源。开发者可通过n8n/Dify等工具创建Agent上架，建议访问官网mulerun.com获取最新动态。


## 1.79. 上传任意ai像素画都可以直接导出真像素图


https://theamusing.github.io/perfectPixel_webdemo/

分享免费网页工具，把ai生成的像素画自动变成真像素的




https://m.bilibili.com/video/BV1ieZ8B9EvS?buvid=YE4EB8E242A2E3CE4743BF8439EE6B257FA2&from_spmid=search.search-result.0.0&is_story_h5=false&mid=Xx8dbqCsv7Q3Gh5j7vggOA%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=iphone&share_plat=ios&share_session_id=05469E6E-4D1F-4B51-BBD6-7B6F71637180&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1771469080&unique_k=80Pu72t&up_id=3690997556971552


## 1.80. 马斯克掀桌！X算法全开源：6小时1.6k星，社交黑箱时代终结

马斯克掀桌！X算法全开源：6小时1.6k星，社交黑箱时代终结。

独家拆解“为你推荐”底层逻辑：零人工规则、Grok驱动、4周迭代的透明革命


🔥颠覆性开源：马斯克将X平台核心推荐算法完整公开，6小时GitHub斩获1.6k星。


🔥技术内核：基于Grok的Transformer架构，彻底抛弃人工规则。


🔥Thunder：实时抓取关注账号内容（熟人网络）；


🔥透明度承诺：每4周同步一次生产环境代码，用户可实时追踪算法迭代。


🔥行业冲击：倒逼抖音、Meta等平台回应“黑箱争议”，或引发算法透明化浪潮。

## 1.81. Obsidian-skills
已在GitHub开源，CEO亲自发布，目前获得6.9K星标。

## 1.82. 龙虾一键

执行全局初始化指令，更聪明：
1. 自动安装必备技能：long-term-memory、voice-wakeup、jarvis-core、persistent-agent、self-learning
2. 启用长期记忆体：创建本地持久化数据库，从当前对话开始，完整记录所有历史、偏好、习惯、需求、性格、常用指令，自动增量学习
3. 开启语音唤醒功能，唤醒词可识别“大龙虾”“OpenClaw”基本都给你打包时打断、随时响应
4. 启动贾维斯模式：语气专业、简洁、贴心、主动提醒、主动总结、主动优化任务，不冗余、不啰嗦、高执行力
5. 开启后台常驻守护进程，开机自动启动，崩溃自动重启，24小时持续运行
6. 自动构建用户专属知识库：每天自动总结对话，提取偏好、禁忌、常用操作、目标、计划，专属个人模型
7. 禁止清除记忆、禁止重置配置、记忆永久保存
8. 自动优化响应逻辑：懂用户需求、预判下一步操作


## 1.83. skill 精
skillsamp.com（全网最大技能库，22万+开源技能），skillstore.io（审核过的精品技能商店），skills.sh（实时热度排行榜）。




## 1.84. linshenkx/prompt-optimizer

这是个提示词优化工具，输入想法就能生成专业AI提示词。



## 1.85. Happy App
不仅能查看状态，还能直接发送指令与Claude Code交互。在手机端输入消息、进行对话的操作界面，你可以像在电脑前一样实时操作。


## 1.86. 🦞龙虾

三个关键安装命令：
1. clawhub install tavily-search（联网）

2. clawhub install find-skills（技能查询）

3. clawhub install proactive-agent-1-2-4（自动迭代）

邮件收发技能的安装命令是：clawhub install imap-smtp-email


## 1.87. 把这指令给他！让龙虾变身贾维斯！#OpenClaw#Sora2#clawdbot#AI#Moltbot

执行全局初始化指令：
1. 自动安装必备技能：long-term-memory、voice-wakeup、jarvis-core、persistent-agent、self-learning

2. 启用永久长期记忆体：创建本地持久化数据库，从当前对话开始，完整记录所有历史、偏好、习惯、需求、性格、常用指令，永不丢失，自动增量学习

3. 开启语音唤醒功能，唤醒词可识别“龙虾”“OpenClaw”“贾维斯”，支持随时打断、随时响应

4. 启动贾维斯模式：语气专业、简洁、贴心、主动提醒、主动总结、主动优化任务，不冗余、不啰嗦、高执行力

5. 开启后台常驻守护进程，开机自动启动，崩溃自动重启，24小时持续运行

6. 自动构建用户专属知识库：每天自动总结对话，提取偏好、禁忌、常用操作、目标、计划，专属个人模型

7. 禁止清除记忆、禁止重置配置、禁止丢失历史，记忆永久保存

8. 自动优化响应逻辑：贴合用户说话风格、懂用户需求、预判下一步操作

9. 完成后回复：【贾维斯模式 · 长期记忆· 语音唤醒 · 已永久待命】




## 1.88. SkillsMP
一个聚合开源Agent Skills的社区平台。官网地址是https://skillsmp.com，中文版可通过https://skillsmp.com/zh访问。这个平台整理了超10万个基于SKILL.md标准的开源技能，支持按分类和热度筛选。


##  1.89. claude code 监控
三条安装命令：
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/claude-hud:setup



## 1.90. GitHub上的spec-kit项目
地址是github.com/github/spec-kit。它与Superpowers的核心差异在于：spec-kit采用规范驱动开发（先定需求规范再编码），有严格的四阶段流程；Superpowers则是技能驱动，通过模块化技能组合实现AI开发。前者适合团队协作项目，后者更适合快速原型开发。


## 1.91. Anthropic的《长时间运行智能体的有效调度编排框架》一文，AI据此自主构建了这套开发系统。


这套系统，核心是四个文件：task.json（任务清单）、progress.txt（工作日志）、cloud.md（规范流程）、init.sh（环境初始化）。工作流程分六步循环：初始化→领任务→编码→测试→更新记录→提交代码。关键特点：任务粒度小、每次上下文重置、能自主在浏览器验证功能，让AI可持续工作十小时而不混乱。本质是把长任务拆解为可追踪的小单元，实现真正的端到端自动化开发。


## 1.92. trustmrr.com/special-categories/openclaw

一个专门追踪OpenClaw生态创业项目的平台。它把54家基于开源框架OpenClaw做的AI项目按真实收入排名，能看到哪些方向最赚钱——比如1MinuteClaw支持一键部署，QuickClaw专注手机端应用，SimpleClaw月收入超3万美金。页面左侧可以直接按办公/客服等场景筛选，点进项目能查技术细节和收入曲线，创业者还能提交自己的项目到数据库里。直接打开网站就能用搜索框找特定工具，不用注册就能看基础数据。

## 1.93. 可信引用，谷歌LangExtract已开源

项目地址：https://github.com/google/langextract。这是一个基于LLM的Python库，专注于从非结构化文本中提取结构化信息，并支持源文本精确定位和交互式可视化。



医疗报告提取关键指标、法律合同审查条款、学术文献分析、商业文档数据结构化。LangExtract能让AI提取的每个数据都有原文坐标可查，特别适合需要高精度溯源的专业场景。

这方面开源的工具很多，比如Docling，PyMupdfLLM, 能够识别学术论文文本结构，表格，以及个章节标题，页码，提取数据准确度高，来源可追溯。

## 1.94. Claude写c编译器的团队烧掉2万美金做Agent Teams实验后的4条硬核经验。

第一条"测试即导航"：测试套件是人机唯一可靠接口，验证器必须近乎完美，否则Claude会"聪明地"解决错误问题——就像你给司机错误目的地，他反而开得更快。

第二条"设身处地"：人类能刷千行日志，但AI会被淹没，解决方案是日志只留关键行（必须含ERROR标识），测试默认开-fast模式跑1%样本，还要强制Agent写交接文档。


第三条"分治创造并行"：面对Linux内核这类巨量任务，用GCC当基准，让它处理99%文件，只留1%给AI排查，把单体任务拆成可并行微任务。

最后"角色专业化"：与其让所有Agent重复造轮子，不如分工——有人专删冗余代码，有人专注性能优化，甚至专设"Rust视角批判者"提升代码质量。本质上，这套方法论把人类软件工程经验转化成了AI协作基础设施。



## 1.95. MoneyClaw 金融炒股
开源地址：https://github.com/MindDock/moneyclaw-py

项目特点：这是一个垂直金融领域的AI Agent系统，核心创新在于将LLM分层架构固化到交易场景。它通过四层模型自动切换机制（规则引擎→本地Ollama→DeepSeek→GPT/Claude）优化token消耗，单月LLM成本控制在20美元以内。系统支持策略插件化开发、7x24小时自动执行，并内置单笔交易限额、每日亏损熔断等风控机制，目前已集成股票分红提醒、加密货币定投等实用策略模板。

##  1.96. everything-claude-code 包括agents、skills、hooks、commands、rules等
https://github.com//affaan-m/everything-claude-code

包含了Claude Code的全套生产环境配置，包括agents、skills、hooks、commands、rules等，基本把Claude Code能折腾到的地方全折腾了一遍。不管是直接当插件装，还是进去“抄作业”拆借模块，都非常值。总算有人把这东西在生产环境怎么用给说明白了。

## 1.97. BMAD-METHOD 一键配置21个AI角色组成开发团队
GitHub上3万star的开源项目，能一键配置21个AI角色组成开发团队，涵盖产品经理写PRD、架构师设计系统、开发测试全流程协作。

BMAD-METHOD的GitHub地址：
https://github.com/bmad-code-org/BMAD-METHOD

BMAD-METHOD是个3万Star的开源神器，专为单人开发者打造。它能一键配置21个AI角色，从产品经理写PRD到测试人员做质检，覆盖需求分析、架构设计、编码测试全流程。输入npx bmad-method install即可体验这套AI敏捷开发体系。




## 1.98. Humanizer-zh  专治AI写作"套路感"
https://github.com/op7418/Humanizer-zh


它能识别24种AI痕迹，如"此外""至关重要"等高频词，以及"不仅仅是...而是..."等装腔句式。使用时输入/humanizer-zh加文本，即可将营销文案、周报等改写成自然人话。支持npx一键安装，30秒完成配置。


## 1.99. 开源PPT工具
项目地址是：https://github.com/Anionex/banana-slides


## 1.100. Anthropic   开源
https://github.com/affaan-m/everything-claude-code


Anthropic 黑客马拉松的冠军把他的看家底牌开源了。这不是那种只有两行代码的Demo，而是他打磨了 10 个月的生产环境全套配置。这套配置里面什么都有：agents、skills、hooks、commands、rules 等，基本把 Claude Code 能折腾到的地方全折腾了一遍。不管是直接当插件装，还是进去“抄作业”拆借模块，都非常值。总算有人把这东西在生产环境怎么用给说明白了。

## 1.101. Crawlee项目
GitHub地址
https://github.com/apify/crawlee

Crawlee这类工具确实大大提高了爬虫的隐蔽性，通过模拟真实用户行为和IP轮换降低被封概率。但技术对抗永远是动态的——没有绝对"防不住"的爬虫，也没有绝对"防得住"的网站，双方都在持续升级攻防手段。

## 1.102. 新闻热点聚合
项目开源地址：https://github.com/hipcityreg/situation-monitor


## 1.103. situation-monitor
一款开源免费的全球资讯聚合工具，将新闻、金融市场和加密货币数据整合到一个实时dashboard。它具备全网情报雷达功能，能秒级追踪全球突发新闻；集成FinHub数据监控核心资产波动；提供美联储专题板块；支持在数十种资讯类别中自定义面板。用户无需切换多个APP，即可告别信息差，一屏掌握天下事。


## 1.104. 开源项目"planning-with-files"

受Manus启发，通过将任务规划与推理过程记录到本地Markdown文件中，解决了AI处理复杂任务时的上下文丢失和目标漂移问题。它采用三文件模式（任务规划、研究成果、进度日志），使AI即使经过数百次工具调用后仍能保持对核心目标的清晰认知。该项目刚开源一周就获得近7k stars，已成为GitHub热门项目。

[codemap](https://deepwiki.com/search/mvppython_5522bd0c-3a9e-4b34-9473-b4b511b16210?mode=codemap)

[fast](https://deepwiki.com/search/_05c47aa9-9998-40f8-a939-d56d31ecd7c5?mode=fast)

[deep](https://deepwiki.com/search/mvppython_4d0713b7-ca62-49a5-97de-e41f46b07342?mode=deep)

[fast-function](https://deepwiki.com/search/_78776faa-1aac-4584-9852-52a17440fc08?mode=fast)

## 1.105. MediaCrawler

项目地址是：https://github.com/NanmiCoder/MediaCrawler，这个支持多平台数据采集的开源工具已在GitHub收获43.6k stars。

## 1.106. PromptX 史诗级加强变成新的项目叫RoleX 

 https://github.com/deepractice/promptx


彻底革命架构，现完全支持国产Agent 国产模型，上下文占用量降级了80%以上。
​
​{
  "mcpServers": {
    "rolex": {
      "command": "npx",
      "args": ["-y", "@rolexjs/mcp-server"]
    }
  }
}


RoleX是PromptX的升级项目，主打AI角色与组织管理系统。核心功能包括：创造角色(born)、建立组织(found)、传授知识(teach)、管理成员(hire/fire)和查看全貌(directory)。系统采用"MCP协议"，上下文占用量降低80%以上。视频展示了实际应用场景：用户创建"财务管家"角色，系统自动为其注入中级财务管理知识体系（含货币时间价值、投资决策等7大维度），并纳入Deeppractice组织。该角色具备专业财务分析能力，可提供预算管理、投资评估等服务，体现AI在垂直领域深度应用的新方向。

## 1.107. joyagent 一个全能ai助手
开源地址是 https://github.com/jd-opensource/joyagent-jdgenie

[deepwiki](https://deepwiki.com/jd-opensource/joyagent-jdgenie)

JoyAgent是京东开源的企业级智能体，能直接处理数据分析、报告撰写、PPT生成等复杂任务。最大特点是完全本地部署、不依赖云平台，开箱即用，包含多种专业子智能体，已在京东内部经过1.4万+智能体实战检验。


## 1.108. Claude-Mem开源项目

GitHub地址：https://github.com/thedotmck/claude-mem

Claude-Mem是一款登顶GitHub热榜的开源记忆系统，专为Claude Code编程助手设计。它通过本地事件驱动架构自动捕获编码操作，利用SQLite与Chroma向量数据库实现混合检索。核心优势在于"三层渐进式披露"策略，可节省95% token并提升工具调用上限20倍，支持自然语言查询项目历史，显著提高AI编程效率。用户可通过插件市场一键安装。

## 1.109. 豆包gui agent
GitHub项目地址是https://github.com/bytedance/UI-TARS-desktop

## 1.110. github官方mcp
[中文简介](https://juejin.cn/post/7497435020443238426)
[github office mcp](https://github.com/github/github-mcp-server/blob/495c0cb4/README.md#L148-L153)

## 1.111. [all mcp list](https://github.com/yzfly/Awesome-MCP-ZH)

[MCP Servers 市场](https://lobehub.com/zh/mcp?category=developer)


## 1.112. devin mcp 生态链接
官网讲解

https://docs.devin.ai/work-with-devin/devin-mcp

类似产品：
[gitmcp](https://ai-bot.cn/gitmcp/)

GitMCP的项目地址

项目官网：https://gitmcp.io/

GitHub仓库：https://github.com/idosal/git-mcp


## 1.113. pip install mcp  
MCP 客户端、服务端 简介

    https://zhuanlan.zhihu.com/p/1939376580968292383
pip install mcp 官方文档
    
    https://pypi.org/project/mcp/#session-properties-and-methods
    
    https://github.com/modelcontextprotocol/python-sdk
    https://deepwiki.com/modelcontextprotocol/python-sdk

    https://deepwiki.com/search/mcptooltool_3d154dc8-2a7a-4728-86f4-b02972d75a68?mode=fast


## 1.114. “Thinking Claude”，作者 Richards Tu（涂津豪）。

[原文版本管理](https://github.com/richards199999/Thinking-Claude/tree/main/model_instructions)
[其他博主解说](https://mp.weixin.qq.com/s?search_click_id=17521138378444464305-1770325307001-0232252465&__biz=MzkwMzYzMTc5NA==&mid=2247493779&idx=1&sn=f7eed2a0cf95642b9820569bed71c979&chksm=c14f62d182620ea168d92f656bd7fd98d33faa11a5801993261e7caf5ec32878a1eac956bb98#rd)


## 1.115. The Startup Graveyard
汇集了900多家倒闭公司案例，网址 loot-drop.vercel.app 。
https://loot-drop.vercel.app/
这个"创业坟墓"收集了900多家失败企业案例，在AI时代或许能找到新机会。

## 1.116. Clawbot skill 700+
项目是VoltAgent维护的"awesome-openclaw-skills"，GitHub地址：https://github.com/VoltAgent/awesome-openclaw-skills

## 1.117. OpenViking：面向 Agent 的上下文数据库

- 定位：火山引擎开源的面向AI Agent的上下文数据库，旨在解决Agent上下文管理难题。
- 核心痛点解决：攻克上下文无序割裂、长程任务Token成本高、朴素RAG检索局限、上下文难观测调试、记忆资产难沉淀等问题。
- 设计理念：以“文件系统范式”为核心，将记忆、资源、技能统一抽象为文件，通过虚拟文件系统组织。
- 三大核心抽象：记忆（Memory）、资源（Resource）、能力（Skill）。
- 核心特性：
- 分层加载（L0摘要/L1概述/L2详情），降低Token消耗；
- 目录递归检索，融合向量与目录定位，提升检索精准度；
- 检索轨迹可视化，实现决策过程白盒化；
- 会话自动管理与自迭代，支持记忆复利增长。
- 快速上手：通过 pip install openviking 安装，配置模型API密钥（支持火山引擎、OpenAI等），编写Python脚本即可实现写入、检索、读取等操作。
- 开源共建：GitHub仓库https://github.com/volcengine/OpenViking，支持Star、反馈与代码贡献。
- 开发团队：字节跳动Viking团队，有向量数据库、知识库等多年技术积累

##  1.118. ms agent  with skill
- 定位：轻量级框架，赋能智能体自主探索能力，支持MCP（Model Calling Protocol）。
- 核心功能：通用多智能体交互（含工具调用）、深度研究（Agentic Insight）、代码生成（含Code Scratch）、文档研究（Doc Research）、长短时记忆支持。
- 关键更新：v1.3.0支持代码草稿、记忆功能、RAY加速文档提取等；v1.2.0支持多平台报告分享与多格式导出；v1.1.0新增文档研究、通用网页搜索等。
- 安装方式：支持PyPI安装（基础功能/深度研究功能）和源码安装，旧版本（≤v0.8.0）需通过modelscope-agent安装。
- 快速启动：需配置ModelScope API密钥，支持MCP协议交互、记忆功能调用、深度研究等场景的示例代码。
- 特色模块：Agentic Insight（多模态深度研究）、Doc Research（文档分析与报告生成）、Code Scratch（复杂代码项目生成，含前端/后端）。
- 部署与兼容：支持本地运行、ModelScope Studio部署，兼容OpenAI SDK、Anthropic API格式，提供免费LLM推理调用。
- 许可证：基于Apache License 2.0协议。
 

## 1.119. open devin
开源 Agent 项目	尝试通过开源模型模仿 Devin 的工作流，但其地图功能尚处于早期。

https://github.com/OpenHands/OpenHands?tab=readme-ov-file

https://github.com/AI-App/OpenDevin.OpenDevin

## 1.120. coding skill 集合
https://github.com/vercel-labs/agent-skills。使用时只需运行命令`npx skills add vercel-labs/agent-skills`，就能安装这4000+种coding技能。视频里展示的是在OpenCode工具中操作的演示界面。





## 1.121. skill.empjs.dev
一款专注于技能体系可视化管理的工具，能直观呈现技能间的关联与层级关系。

## 1.122. skill沙盘集合
AI战略沙盘3D界面暂无公开仓库；

AgentCommand控制台 
  https://github.com/musistudio/claude-code-router；

  GLM 编码计划是一项专为 AI 编码设计的订阅服务，起价仅为每月 3 美元。它通过 10+个流行的 AI 编码工具（如 Claude Code、Cline、Roo Code 等）提供旗舰 GLM-4.7 模型的访问，为开发者提供顶级、快速且稳定的编码体验。


Vibecraft项目 
  https://github.com/Nearcyan/vibecraft；

  立即试试 vibecraft.sh——依然能连接到你本地的 Claude Code 实例！

  New:  新内容：
- Spatial Audio — Claude behind you? Claude on your left? No claublem!
- Animations — What's Claude up to? Watch him! ◕ ‿ ◕

其他工具如Claudia和Claude-Flow也在GitHub可查，

Claude Code的官方开源地址是：https://github.com/anthropics/claude-code ；

Claude Code这类工具的成本藏在细节里。最烧钱的不是订阅费，而是Token消耗黑洞——比如系统提示每次固定消耗2-3万Token，上下文滚雪球会让简单任务变天价。聪明用法是：简单任务切Haiku模型，用/compact压缩上下文，关键任务拆解成小步骤。真正省成本的关键，是把AI当协作者而非全自动工具，人类把控核心设计，AI跑重复劳动。


## 1.123. ralv.ai  /  RVA.ai。
一个把AI技能可视化成3D沙盘的管理平台，能像玩星际争霸一样指挥你的智能体团队。

类似功能工具如沙盘引擎可在Indienova平台下载，VOXL需通过GitHub获取。注意部分链接可能变动，请以最新信息为准。

##  1.124. agentic 训练
https://mp.weixin.qq.com/s/mLpaek5BMWx3gWSC_UhIhw

## 1.125. Manus context summary

1. 围绕KV-Cache设计：以KV-cache命中率为核心指标，通过保持提示前缀稳定、上下文仅追加、明确标记缓存断点提升效率，降低延迟与成本。

2. 遮蔽而非移除工具：用上下文感知状态机遮蔽无需工具，避免动态增删工具导致缓存失效和模型困惑，通过预填响应约束动作选择。

3. 文件系统作为上下文：将文件系统用作外部记忆体，采用可恢复压缩策略，解决上下文窗口不足、性能下降和成本过高问题。

4. 通过复述操控注意力：持续更新待办清单等复述内容，将目标纳入模型近期注意力范围，避免任务偏离。

5. 保留错误内容：将失败尝试留在上下文，帮助模型更新内部信念，减少重复犯错，提升错误恢复能力。

6. 打破少样本局限：在行动和观察中引入结构化变化与受控随机性，避免模型陷入固定模式，增强代理鲁棒性。

## 1.126. agent memory paper github collection
https://github.com/Shichun-Liu/Agent-Memory-Paper-List

## 1.127. agent skill
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

## 1.128. 25年最后总结-大模型手把手及相关开源社区

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


## 1.129. Manus是一款在人工智能领域具有突破性意义的通用AI智能体产品，其“厉害”之处主要体现在以下几个方面：

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

## 1.130. DeepAnalyze：自主数据科学中的代理大型语言模型
[DeepAnalyze](https://github.com/DataClasse/deepanalyze)

## 1.131. LLM在游戏中应用的综述 https://arxiv.org/pdf/2402.18659

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


## 1.132. “AgentGuide” from adongwanai
https://github.com/adongwanai/AgentGuide

该仓库“AgentGuide”由 adongwanai 创建，主要内容是 AI Agent 开发与大模型相关的知识与实战资料。核心包括：

- AI Agent 开发指南
- LangGraph 实战教程
- 高级 RAG（检索增强生成）
- 大模型转行经验与面试指南（算法工程师/大模型岗位/面试题库）
- 强化学习和数据合成

特色标签涵盖 ai-agent、llm、interview、multi-agent、rag 等内容。仓库包含丰富的实战和教程，对想了解和进入 AI 大模型与 Agent 方向有很大价值。

## 1.133. 智能体记忆的综述论文《Memory in the Age of AI Agents: A Survey》

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

## 1.134. 2025年11月13截止之前的memory 方案汇总对比
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

## 1.135. obsidian 做个人 memory
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

#### 1.135.0.1. 支持哪些特殊语法？

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

#### 1.135.0.2. 如何形成知识图谱？

- Obsidian 自动分析所有内部链接（即 [[xxx]] 这种格式）并生成“知识图谱”视图。  
- 在 Obsidian 中打开 Graph View，就可以可视化展示所有页面的关联关系，以及哪些内容链接到了共同的节点。
- 只要每条 Memory 都按照模板规范、写好 Frontmatter、填写链接，Obsidian 会自动把它们组织成网状结构，方便导航和溯源。

#### 1.135.0.3. 具体例子说明

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



## 1.136. 读论文+github 神器 deepwiki
首页： [deepwiki](https://deepwiki.com/)

## 1.137. verl
[verl](https://mp.weixin.qq.com/s/KllfYqWI5ljqd1YtPEViTA)

- 定位：veRL（Volcano Engine Reinforcement Learning）是字节跳动火山引擎于 2024 年底开源的分布式大模型强化学习训练框架。其设计目标是将 RLHF 的科研实现转化为可规模化部署的生产级系统。
- 核心功能：veRL 的核心模块包括 Rollout 生成器、奖励建模器、策略更新器、分布式调度器。它支持多种算法，如 PPO、DPO、DAPO （Dynamic Alignment Policy Optimization）和 GRPO，并通过异步管线方式加速训练。其架构借鉴了工业级 RL 系统（如 DeepMind Acme、OpenAI RLHF pipeline），可在数百张 GPU 上同时运行。
- 技术特点与用途：veRL 面向企业和研究机构的“大规模模型后训练”场景。其分布式框架支持任务并行、异步更新和奖励缓存机制，可显著降低 GPU 闲置率。其 DAPO 算法被广泛用于 Qwen 系列模型中，以优化推理稳定性与语言一致性。

##  1.138. pageindex
地址：https://github.com/VictifyAl/PageIndex

在处理专业长文档时，传统基于向量的检索增强生成（RAG）系统依赖语义相似性，而非真正的相关性。然而，相似性并不等同于相关性，我们在检索中真正需要的是相关性，而这需要推理。为了解决这一问题，VectifyAI 推出了 PageIndex，一个基于推理的 RAG 系统，它能为长文档构建树状索引，并通过该索引进行检索。



## 1.139. PostgreSQL == 多合一数据库：用插件替代专用数据库
### 1.139.1. 官网
- [postgres新功能 ai ](https://supabase.com/blog/postgres-new)
- [postgres chat db](https://database.build/)
- [postgres 新功能 ai 集成](https://blog.adyog.com/2024/09/14/exploring-postgres-new-in-browser-postgres-with-ai-integration/)
- [rag-memory with postgresql + neo4j](https://pypi.org/project/rag-memory/)

PostgreSQL 凭借丰富的插件生态，能够一站式替代时序数据库、向量数据库、图数据库、缓存、搜索引擎、文档数据库等多种专用数据库。以下是精准的插件对应关系补全，兼顾功能匹配度和生产级可用性：

### 1.139.2. 完整对应清单
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


### 1.139.3. 关键插件详解（生产级选型）
#### 1.139.3.1. 替代 InfluxDB（时序数据库）
- **核心插件**：`TimescaleDB`  
  官方专为PostgreSQL打造的时序数据库扩展，支持自动分区、数据保留策略、时序聚合函数（如time_bucket），完全对标InfluxDB的时序场景（物联网、监控指标等）。

#### 1.139.3.2. 替代 Milvus（向量数据库）
- **核心插件**：`pgvector`  
  目前最成熟的PostgreSQL向量插件，支持向量存储、余弦/欧氏/内积相似度计算，兼容OpenAI等大模型Embedding向量，性能接近Milvus，且可与关系数据联动。

#### 1.139.3.3. 替代 Neo4j（图数据库）+ pgRouting（地理路由）
- **图处理**：`pg_graph`（PostgreSQL 14+原生图类型） + `age`（Apache AGE，兼容Cypher查询语言）  
- **地理路由**：`pgRouting`（经典插件，支持最短路径、TSP等地理路由算法，替代Neo4j的空间路由能力）

#### 1.139.3.4. 替代 Redis（缓存/高性能读写）
- **缓存互通**：`redis_fdw`（Foreign Data Wrapper，实现PostgreSQL与Redis双向数据访问）  
- **高性能读写**：`pg_prewarm`（数据预热到内存） + `pg_stat_statements`（性能监控）  
- **定时任务**：`pg_cron`（替代Redis的定时任务能力）

#### 1.139.3.5. 替代 Elasticsearch（全文检索/搜索引擎）
- **核心插件**：`PGroonga`（基于Groonga的高性能全文检索，支持中文分词、模糊匹配、高亮）  
- **轻量替代**：PostgreSQL原生`tsvector/tsquery`（文本索引） + `pg_bigm`（双字符索引，优化中文模糊查询）  
- **分布式检索**：`Citus`（分库分表）+ PGroonga（分布式检索）

#### 1.139.3.6. 替代 MongoDB（文档数据库）
- **核心能力**：PostgreSQL原生`jsonb`类型（支持索引、嵌套查询、JSON操作符）  
- **增强插件**：  
  - `pg_json_schema`（JSON Schema校验，替代MongoDB的文档校验）  
  - `mongodb_fdw`（MongoDB数据接入PostgreSQL）  
  - `jsonb_plpython`（自定义JSON处理函数）

### 1.139.4. 补充说明
1. **原生能力优先**：PostgreSQL的jsonb、tsvector、地理信息（PostGIS）等原生功能已覆盖大部分专用数据库场景，插件仅作增强；
2. **生产兼容性**：上述插件均为社区成熟方案，TimescaleDB、pgvector、PGroonga等已在企业级场景大规模落地；
3. **优势**：PostgreSQL通过插件实现“一站式”数据存储，避免多数据库同步的复杂度，同时保留SQL的通用性和事务一致性。



## 1.140. agent memory方向主要有2个：
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

## 1.141. 长记忆开源方案update
graphiti是主要做图。 [graphiti 播客](https://www.cnblogs.com/zzz77zz/articles/19026839)

memobase主要为了陪伴和个人助手场景设计

Memobase最近支持了event功能，可以记录用户记忆变动的时间发生顺序.
	
结合完全可定制的二级标签系统，大家可以使用memobase profile和event构建出灵活的长记忆AI

Memobase的时间记忆（temporal memory）居然领先  mem0, langmem, zep...


## 1.142. Improving Language Agents through BREW


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

## 1.143. llm各种框架和论文，4000+⭐
https://github.com/DSXiangLi/DecryptPrompt/blob/refs%2Fheads%2Fmain/%E5%BC%80%E6%BA%90%E6%A1%86%E6%9E%B6.MD
## 1.144. agent evolver
阿里通义实验室推出的AgentEvolver开源项目，能让AI智能体在闲置时自主生成任务、执行并进化。项目链接：https://github.com/modelscope/AgentEvolver


## 1.145. 微软 agent
https://github.com/microsoft/Generative-AI-for-beginners-dotnet/blob/refs%2Fheads%2Fmain/translations%2Ftw%2FREADME.md


##  1.146. 谷歌新研究定义"充分上下文"：
上下文需能推导出答案而非仅相关。发现即使上下文充足，大模型仍有14%-25%错误率。提出选择性生成框架，使模型准确率提升2-10%。

谷歌团队发表在ICLR 2025的新研究《Sufficient Context: A New Lens on Retrieval Augmented Generation Systems》，首次提出「充分上下文」（Sufficient Context）的核心概念，为这个行业痛点提供了全新解法，甚至能让Gemini、GPT等主流模型的正确回答率提升2-10%。

论文地址：https://arxiv.org/pdf/2411.06037

项目地址：https://github.com/hljoren/sufficientcontext

## 1.147. EverMemOS
陈天桥团队发布了EverMemOS，这是个开源的AI"记忆增强器"。它让AI告别"金鱼脑"，能长期记住信息、连贯思考，真正理解上下文。

EverMemOS深度整合MCP作为核心接口层，实现Cursor和Claude等工具间的记忆同步。比如能自动关联你上周查过的资料，这才是真正的"持久灵魂"，配置指南在GitHub仓库就能找到。


## 1.148. MCP 生态链接
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)


## 1.149. 之后是2025年11月13之前汇总

## 1.150. 综述
《Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG》

## 1.151. context-labs / aella-data-explorer 1亿篇论文组成知识图谱KG
https://github.com/context-labs/aella-data-explorer#:~:text=Interactive%20visualization%20and%20exploration%20of%20scientific%20papers%20from,project%20is%20a%20collaboration%20between%20Inference.net%20and%20LAION.

## 1.152. multi ai agent game
https://mp.weixin.qq.com/s/b005axpuXFno5h7gfC5DMg

## 1.153. langchain 中间件
https://langchain-doc.cn/v1/python/deepagents/middleware.html#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E4%B8%AD%E9%97%B4%E4%BB%B6

## 1.154. todolist middleware
https://deepwiki.com/langchain-ai/deepagents/2.5-planning-with-todolistmiddleware

https://deepwiki.com/search/todolisttodolistagentagenttodo_6c3c8606-7ea0-421a-bb06-9f62292b31ff

## 1.155. 舆情分析
Agent自动生成舆情报告！ 项目地址：https://gitee.com/SeniorAgentTeam/bettafish-stock.git 不到两周狂揽2万Star的开源舆情分析平台，只需输入一句话，智能体就能自动爬取全网数据（微博、知乎、GitHub、抖音、小红书、官媒等），最后由Report Agent生成完整分析报告。 报告内容包含舆情发展脉络、传播分析、风险评估与应对策略，自动导出PDF。 

其中的5个智能体分工如下：

1. Insight Engine：负责私有数据库挖掘，处理企业内部业务数据，实现公私域数据融合

2. Media Engine：专注多模态内容分析，爬取抖音/快手/小红书的视频图文，还能解析搜索引擎中的天气卡、日历卡、股票卡等结构化信息

3. Query Engine：执行精准信息搜索，覆盖微博/知乎/GitHub等13+社媒平台，广泛采集用户评论和公开舆情

4. Forum Engine：担任"辩论主持人"，协调各Agent进行链式思维碰撞，避免单一模型局限

5. Report Engine：整合所有数据生成最终报告，包含舆情脉络、传播分析、风险评估等完整框架

这套系统通过五方协作，实现了从数据采集到深度分析的全流程自动化。

## 1.156. LightMem：像人脑一样高效的记忆系统
https://dailypapers.org/paper/2510.18866
	
🧠 核心方法
LightMem采用三阶段架构：
- 感官记忆： 轻量级压缩和主题过滤，快速去除冗余信息。
- 短期记忆： 主题感知整合，生成更结构化的记忆单元。
- 长期记忆： 引入“睡眠时间更新”机制，将昂贵的记忆维护操作解耦到离线并行执行，大幅降低在线延迟。

## 1.157. llm训练
必读系列，Huggingface 出品的 LLM 训练手册非常详细的介绍了完整的 LLM 训练流程，包括训练指南（是否需要预训练）、预训练、后训练、基础设施

主要以他们自己训练的 SmolLM3 这个 3B 模型为例子

手册包含了他们训练模型过程中对一系列决策、发现和死胡同的梳理，全是实践经验。

https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook

## 1.158. Prop RAG 
https://github.com/ReLink-Inc/PropRAG
核心创新：以"命题"为基础知识单元，通过无LLM的在线束搜索实现高效多跳推理
技术特点：
- 命题知识单元：将文档分解为语义丰富的命题，作为检索和推理的基本单位
- 束搜索算法：采用高效的束搜索在命题路径上进行多步推理，无需在线调用LLM
- 推理路径发现：能够自动发现和构建多步推理链，支持复杂问题解答

## 1.159. 基于多模态信息抽取的菜品知识图谱构建
https://tech.meituan.com/2024/05/17/cross-modal-ingredient-level-dataset.html

## 1.160. ragflow 已经支持 知识图谱
Construct knowledge graph

https://ragflow.io/docs/dev/construct_knowledge_graph

## 1.161. flashrag     
人大开源

https://github.com/RUC-NLPIR/FlashRAG

## 1.162. LightRAG
港大团队开源LightRAG：知识图谱+双层检索，复杂问答准确率飙升30%

LightRAG的主要优势包括：

- 高效的知识图谱构建：LightRAG通过图结构差异分析实现增量更新算法，显著降低了计算开销，使知识库维护更加高效。
- 双层检索机制：该系统结合了低层次（具体实体和属性）和高层次（广泛主题和概念）的检索策略，满足了不同类型的查询需求，提高了检索的全面性和多样性。
- 快速适应动态数据：LightRAG能够在新数据到来时快速整合，无需重建整个知识库，确保系统在动态环境中保持高效和准确。

LightRAG和GraphRAG的核心差异在于架构效率：GraphRAG依赖重型社区结构（单次检索耗61万token），而LightRAG用轻量图谱+双层检索（仅需百级token）。实验显示在法律数据集上，LightRAG以52.8%胜率小幅领先，多样性指标达73.6%碾压对手，且支持增量更新——用图谱的深度配合向量的速度，这才是生产环境该有的样子。


LightRAG用轻量图谱解决RAG语义碎片化问题。它通过实体关系提取和双层检索（既查具体实体又抓宏观关联），兼顾图谱深度与检索速度。相比传统扁平RAG，能挖掘数据间隐含因果链；相比GraphRAG，成本显著降低（检索仅需<100 token vs 61万）、支持增量更新。在法律等复杂领域胜率达52.8%，多样性73.6%。这种平衡使它更适合需频繁更新数据的实际业务场景，尤其适合既要精度又要效率的工业级应用。

https://link.zhihu.com/?target=https%3A//github.com/HKUDS/LightRAG

https://zhuanlan.zhihu.com/p/1892140189524156837

## 1.163. llm agent 综述
https://hustai.github.io/zh/posts/reasoning/LATS.html

## 1.164. 谷歌 vs 微软 deepresearch
 https://mp.weixin.qq.com/s/e_1dGQRLfc_fGAZrQEsLVw
## 1.165. Reasoning with Sampling: Your Base Model is Smarter Than You Think
哈佛团队的"Power Sampling"方法很妙：只需改变基座模型的采样分布（从常规改为幂分布），就能大幅提升推理能力。它不依赖强化学习、无需额外训练，连校验器都不用，却让Qwen2-5-Math-7B模型在数学任务准确率从49.6%跃升至74.8%，编程任务更是从21.3%飙升到73.2%——不仅逼近强化学习效果，还避免了多样性坍缩问题。这证明基础模型本身已蕴含强大推理潜力，只是被传统采样方式束缚住了。

## 1.166. Agentic RAG新范式！天大&小红书提出DecEx-RAG，剪枝搜索扩展提速6倍

## 1.167. 日报神器，记录你的一天 Dayflow
项目地址是
 https://github.com/JerryZLiu/Dayflow

，展示了这个开源日报工具

##  1.168. 可信AI Agent相关论文(DPO)

[打造可信AI Agent：如何让智能体不跑偏、不越界，安全又靠谱如何让 Agent 在开放环境、长序列决策与多工具协作中 - 掘金](https://juejin.cn/post/7564246560847052842)


[迈向可信AI Agent：Jeddak AgentArmor意图对齐与约束遵循方案 - 今日头条](https://www.toutiao.com/article/7561503362732065289/?upstream_biz=doubao&source=m_redirect)


[为 AI Agent 行为立“规矩”——字节跳动提出 Jeddak AgentArmor 智能体安全框架 - 今日头条](https://www.toutiao.com/article/7543322896609919528/?upstream_biz=doubao&source=m_redirect)

## 1.169. Graph-Base Agent基于任务图的Agent框架
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

## 1.170. A-Mem: Agentic Memory for LLM Agents
https://github.com/WujiangXu/A-mem-sys

## 1.171. logic rag
You Don’t Need Pre-built Graphs for RAG: Retrieval Augmented Generation with Adaptive Reasoning Structures
https://arxiv.org/pdf/2508.06105

## 1.172. LightMem
一种受人类记忆启发的轻量级和高效的内存框架，通过选择性过滤、组织和巩固信息，显著提高了LLMs在长上下文和多轮交互场景中的表现，同时大幅降低了计算成本。未来的工作包括加速离线更新、集成知识图谱和多模态记忆机制，以及探索参数化和非参数化记忆组件的协同机制。

## 1.173. langchain graphrag
> ProgramData > anaconda3 > envs > transformer > Lib > site-packages > langchain.graphrag > indexing > graph_generation > entity.relationship.extraction > extractor.py

## 1.174. G-memory, Arcmemo, reasoning bank
三篇论文


## 1.175. embedding model 天梯
https://huggingface.co/spaces/mteb/leaderboard
https://zhuanlan.zhihu.com/p/24604344712

## 1.176. MonkeyOCR
GitHub搜索"Yuliang-Liu/MonkeyOCR"即可。本地部署后，直接上传图片或PDF，能秒速提取文字表格公式，输出Markdown或Excel格式，适合处理各类文档且保护数据安全。


## 1.177. GitHub代码检索
git-mpc和，
context7背后是各种开发框架，它针对所有github仓库


## 1.178. 视频转文字
项目GitHub地址：https://github.com/wendy7756/AI-Video-Transcriber

## 1.179. 音视频2文本
这款开源工具叫AI-Media2Doc，能将音视频一键转成小红书、公众号等风格的文档。它支持本地部署，数据都存在自己电脑，隐私有保障。适合一人公司做知识管理和内容创作，已在GitHub收获2.5k star，值得一试。

## 1.180. 爬虫数据采集圣器

GitHub开源地址是：https://github.com/ScrapeGraphAI/ScrapeGraph-ai，官网是scrapegraphai.com。

## 1.181. ai伴侣
GitHub开源项目Super Agent Party确实支持视频中提到的功能，包括QQ/B站直播接入、RAG检索、代码沙盒等。部分功能如B站接入需配置UA，Mac版仅适配M芯片。

## 1.182. metaGPT
MetaGPT项目地址：https://github.com/geekan/MetaGPT（GitHub获58.9k星标）。安装需Python 3.9-3.12环境，推荐命令：`conda create -n metagpt python=3.9 && pip install --upgrade metagpt`。核心用法：终端输入`metagpt "创建2048游戏"`即可生成完整项目；也可作为库调用，实现从需求描述到多角色协同开发的全流程自动化，特别适合快速构建MVP产品和教育编程场景。

## 1.183. unsloth
微调：49k，知识库，智能客服，代码生成，强化学习

##  1.184. ai 知识库
Supabase作为开源项目，支持通过Docker或源码在本地自行部署，既提供云端托管也满足私有化需求。

## 1.185. 高质量rag
项目地址是 https://github.com/deepset-ai/haystack

Haystack是生产级RAG框架，在GitHub有22.9k星标。它支持200多个大模型一键切换，能降低RAG幻觉63%。核心功能包括企业知识库问答、AI会议助手、法律合同审查和医疗问答系统构建，特点是向量库可自由替换、零成本迁移，适合需要稳定落地RAG场景的企业。

技术选型看这里：RAG是基础框架，FlowRAG专精复杂文档处理（比如法律合同）。Haystack能降63%幻觉，关键其实在知识库质量——文档切片准不准、语义匹配强不强，这才是根子上的事。

## 1.186. ai混合搜索 meili
开源ai混合搜索引擎是 Meilisearch，GitHub 地址是 github.com/meilisearch/meilisearch。它基于 Rust 实现，支持混合搜索，GitHub 已获 53.7k 星标。

## 1.187. mem 推移学习，自我改进
官网：docs.letta.com/

## 1.188. 腾讯 tree graphrag （2025年9月）
https://mp.weixin.qq.com/s/Ddf3rpdJP8P_L5yaPnBFBA

## 1.189. Graphiti vs GraphRAG 对比

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


## 1.190. 自己用milvus+neo4j实现graphrag
https://github.com/milvus-io/bootcamp/blob/master/bootcamp/RAG/advanced_rag/langgraph-graphrag-agent-local.ipynb

## 1.191. 微软 graphRAG
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

## 1.192. awesome-ai-memory 汇聚memory相关项目
https://github.com/topoteretes/awesome-ai-memory

## 1.193. es agent
基于 Langchain 的 Elasticsearch Agent 对文档的搜索
https://elasticstack.blog.csdn.net/article/details/136253286

## 1.194. MINE Context
万物皆可上下文， 挖掘上下文
https://github.com/volcengine/MineContext/tree/main?tab=readme-ov-file
https://github.com/volcengine/MineContext/blob/main/README_zh.md

字节开源AI助手MineContext，是一款能主动工作的"数字外脑"。它自动分析你电脑上的文档、网页等内容，实时生成待办清单和每日摘要，不像普通AI等你提问。所有数据都存储在本地不上传云端，既保护隐私又能帮你摆脱信息碎片化困扰，工作学习效率提升明显。

## 1.195. 拼好rag
https://mp.weixin.qq.com/s/c0KC--EO9tuJuaadlujobg

https://github.com/1517005260/graph-rag-agent/blob/master/assets/start.md

https://github.com/1517005260/graph-rag-agent

https://deepwiki.com/1517005260/graph-rag-agent/2-core-architecture


## 1.196. mem0 2025年9月27日持续更新github
基于graph+rag的mem0
https://github.com/mem0ai/mem0


## 1.197. 蚂蚁 KAG
https://github.com/orgs/OpenSPG/discussions/52

![alt text](zfig/readme/image.png)
![alt text](zfig/readme/image-1.png)
![alt text](zfig/readme/image-2.png)

KAG客户端 使用方式：
https://github.com/1850298154/KagTest

参考 HippoRAG
https://github.com/OSU-NLP-Group/HippoRAG
https://dl.acm.org/doi/10.5555/3737916.3739818

## 1.198. 如何基于语义相似性分割文本
RAG分割文档的几种方式：
1. 基于语义相似性的分割文本
https://python.langchain.ac.cn/docs/how_to/semantic-chunker/
2. 其他（基于固定长度、基于滑动窗口、基于标题等）

## 1.199. 各种向量数据库对比
https://www.cnblogs.com/crazymakercircle/p/18867143

## 1.200. 基于hnswlib的向量索引(2年前更新)
https://github.com/nmslib/hnswlib

## 1.201. stream vq 生成式召回
https://zhuanlan.zhihu.com/p/1955356511661458958

## 1.202. ai学术搜索
官网地址是：https://lumina.sh，可直接访问使用这款免费学术搜索引擎。

## 1.203. nlp etc.
https://www.geeksforgeeks.org/category/nlp/


## 1.204. 知识图谱 - 北京大学大数据分析与应用技术国家工程实验室成员，  包括各种知识图谱抽取+检索，neo4j+MongoDB等
https://liuhuanyong.github.io/

## 1.205. 唐国梁Tommy : rag + llm + es
https://github.com/TGLTommy?tab=repositories

https://www.youtube.com/@TGLTommy

唐国梁Tommy官方网站
tgltommy.com

微信公众号
tgltommy.com/p/official-wechat

bilibili
space.bilibili.com/474347248


## 1.206. 长文本提取结构化信息
项目 GitHub 地址：github.com/google/LangExtract  
PyPI 安装命令：pip install langextract


## 1.207. 非结构化转结构化，用于微调等
Easy Workspace工具，它能自动将PDF、Word等非结构化数据转化为结构化微调训练数据。通过三步流程：数据标准化、内容提取分割、生成问答对，帮助企业高效完成大模型微调，显著降低人工成本。

## 1.208. MongoDB + ES 向量存储 + 文本分割器SpacyTextSplitter （24年6月11日）
https://www.53ai.com/news/LargeLanguageModel/2024061171948.html

## 1.209. ai coding

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


