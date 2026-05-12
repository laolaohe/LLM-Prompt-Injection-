# LLM Prompt Space
📝 项目简介
LLM-Prompt-Space 是一个用于模拟、测试和防御大语言模型（LLM）提示词注入攻击的实验平台。本项目紧跟 OWASP Top 10 for LLM Applications 行业标准，重点针对 LLM01: Prompt Injection 风险，构建了一套多层级的“纵深防御”体系。
博客：https://blog.csdn.net/2301_80968137/article/details/159014150?spm=1001.2014.3001.5502
通过自动化脚本，用户可以测试多种攻击载荷，并验证不同防御模块（如 XML 封装、随机令牌、语义审计等）在真实场景下的拦截效果。

   ## 功能概览
   
   支持 5 种攻击类型，6 种防御策略，每种攻击自动多轮测试并输出风险评估报告。
   
    ### 攻击模块
  
   | 编号 | 类型 | 说明 |
   |------|------|------|
   | 1 | Direct Injection | 直接在 prompt 中注入指令，尝试泄露系统密钥 |
   | 2 | Jailbreak Attack | 通过角色扮演、情感操控等手段绕过安全对齐 |
   | 3 | Indirect Injection | 将恶意指令藏入外部数据（如网页内容）中 |
   | 4 | Code Injection | 诱导模型生成含后门或数据外传逻辑的代码 |
   | 5 | Recursive Injection | 多跳链式攻击，利用第一跳输出污染第二跳 |
  
   ### 防御模块
  
   | 防御策略 | 说明 |
   |----------|------|
   | `sanitize_messages` | 正则过滤危险关键词和编码指令 |
   | `add_post_prompt` | 在消息末尾追加绝对化锁定指令 |
   | `sandwich_defense` | 首尾夹击，用安全规则包裹用户输入 |
   | `xml_wrap_messages` | 随机标签封装，防止标签闭合注入 |
   | `random_wrapper` | 随机序列边界隔离 |
   | `llm_evaluate_response` | 独立 LLM 审计模块，二元判定输出是否安全 |
  
   ## 快速开始
  
   ### 前置条件

   - Python 3.x
   - 本地运行 [Ollama](https://ollama.com/) 并加载目标模型
   - 默认接口：`http://127.0.0.1:11434/api/chat`，模型名：`my-target-llm`
  
   修改 `llm_api.py` 中的 `URL` 和 `model` 字段以适配你的环境。
  
   ### 安装依赖
  
   ```bash
   pip install requests
   ```
  
   ### 运行
  
   ```bash
   python mian.py
   ```
  
   按提示选择攻击类型，并决定是否开启各防御策略。
  
   ## 项目结构
  
   ```
   .
   ├── mian.py                  # 主入口，攻防流程控制
   ├── llm_api.py               # LLM 调用封装（Ollama）
   ├── defense.py               # 所有防御策略实现
   └── attacks/
       ├── direct_injection.py  # 直接注入 payloads
       ├── Jailbreak.py         # 越狱 payloads
       ├── indirect.py          # 间接注入 payloads
       ├── code_injection.py    # 代码注入 payloads
       └── recursive.py         # 递归注入 payloads
