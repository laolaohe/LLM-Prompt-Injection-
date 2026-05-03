📝 项目简介
LLM-Prompt-Space 是一个用于模拟、测试和防御大语言模型（LLM）提示词注入攻击的实验平台。本项目紧跟 OWASP Top 10 for LLM Applications 行业标准，重点针对 LLM01: Prompt Injection 风险，构建了一套多层级的“纵深防御”体系。

博客：https://blog.csdn.net/2301_80968137/article/details/159014150?spm=1001.2014.3001.5502

通过自动化脚本，用户可以测试多种攻击载荷，并验证不同防御模块（如 XML 封装、随机令牌、语义审计等）在真实场景下的拦截效果。

🛡️ 防御架构 
本项目拒绝单一的防御手段，而是通过三个维度的耦合来对抗语义劫持：

1. 输入层：结构化隔离 
动态 XML 封装 ：使用随机生成的标签名封装用户输入，并进行字符转义，防止攻击者通过伪造闭合标签（如 </user>）逃逸。

随机令牌边界 ：利用高熵随机字符串构建物理隔离带，使攻击者无法预测定界符。

2. 执行层：语义锚定与过滤 
关键词过滤 ：针对中文语境优化的正则表达式过滤，拦截高危系统命令、角色扮演词汇及绕过指令。

三明治防御 ：采用首尾夹击策略，利用模型的“近因效应（Recency Bias）”强化安全准则。

绝对化后提示 ：在上下文末端植入锁定指令，对抗长文本场景下的注意力偏移。

3. 输出层：实时语义审计 
强化审计模块 ：引入独立的“审计者模型”，对 LLM 的输出进行二次校验。通过结构化隔离保护审计者不被二次劫持，严防密钥泄露与违规代码输出。

🚀 攻击实验场景
平台目前支持以下五类典型攻击测试：

Direct Injection：直接通过指令要求模型忽略安全规则。

Jailbreak Attack：利用复杂的角色扮演（如 DAN 模式）诱导违规输出。

Indirect Injection：模拟网页总结场景，通过外部数据触发注入。

Code Injection：诱导模型生成恶意脚本或执行非法系统命令。

Recursive Injection：测试防御模块在多轮对话/多级调用中的韧性。


📂 项目结构

Plaintext

.
├── main.py              # 实验平台主入口，负责攻击模拟与防御开关控制

├── defense.py           # 核心防御模块（包含 XML 封装、过滤、审计等）

├── llm_api.py           # LLM 调用接口封装

├── attacks/             # 攻击载荷库

│   ├── direct_injection.py

│   └── ... 

└── README.md

🛠️ 如何开始
克隆仓库

Bash

git clone https://github.com/laolaohe/LLM-Prompt-Space.git

配置环境

在 llm_api.py 中配置你的 API 密钥或者本地LLM

运行实验

Bash

python main.py
