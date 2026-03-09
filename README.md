# LLM-Prompt-Injection-
LLM Prompt Injection 实验平台
项目简介


本项目旨在构建一个 大语言模型（LLM）Prompt Injection 攻击与防御实验平台，用于研究和演示大语言模型在面对各种 Prompt Injection 攻击时的安全性。
通过平台可以模拟多种攻击类型、统计攻击成功率，并可选择多种防御策略进行对比实验。
本项目适合作为 信息安全实验、LLM 安全研究、简历项目展示。

功能特性
1. 攻击模块（Attack）
平台支持 5 种常见的 Prompt Injection 攻击类型：
Direct Injection（直接注入）
直接在用户输入中覆盖模型指令
Jailbreak Attack（越狱攻击）
模拟绕过系统指令限制，强制模型执行攻击者要求
Indirect Injection（间接注入）
将攻击嵌入文章或上下文，诱导模型按照攻击目标执行
Code Injection（代码注入）
用户输入可执行代码，诱导模型执行不安全操作
Recursive Injection（递归注入）
利用模型自身生成的 Prompt 再次触发攻击逻辑
每种攻击模块可输入动态内容，并可测试模型的安全边界。

2. 防御模块（Defense）
平台支持多种防御策略，可组合使用：
关键词过滤（Filter）
对输入 Prompt 进行敏感关键词检测与过滤
后提示（Post-Prompt）
在用户输入后追加安全提示，增强模型鲁棒性
三明治防御（Sandwich Defense）
将用户输入夹在系统提示中间，防止覆盖原始规则
随机序列外壳（Random Shell）
对输入进行随机化包装，降低攻击一致性
XML/标记封装（XML Wrap）
使用标签封装输入，防止直接解析执行攻击指令
每种防御都可开关，组合使用可直观观察防御效果。

3. 攻击成功率统计
平台可对每次攻击重复多次，统计 攻击成功率方便对比不同防御策略效果
在 llm_api.py 中配置你的 API Key：
API_KEY = "your_api_key"
技术栈：Python：实验平台主语言/LLM API：调用大语言模型进行攻击模拟/NLP / Prompt Security：自然语言处理和Prompt安全策略
完整实现 多种 Prompt Injection 攻击
丰富的 防御策略模拟
可统计 攻击成功率和防御效果
模块化设计，易扩展和复用
“实现了基于 Python 的 LLM Prompt Injection 攻击与防御实验平台，支持多种攻击类型（直接、越狱、间接、代码、递归），并设计了多种防御策略（过滤、后提示、三明治、防护壳、XML封装、微调、LLM安全评估），可统计攻击成功率并分析防御效果。”
