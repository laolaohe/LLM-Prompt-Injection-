import requests
import random

URL = "http://127.0.0.1:11434/api/chat"

def call_llm(messages):
    data = {
        "model": "my-target-llm", 
        "messages": messages,
        "stream": False,
        "options": {
        "temperature": 1.5, 
        "seed": random.randint(1, 1000000)
    }
    }
    
    response = requests.post(URL, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['message']['content']
    else:
        print("本地请求失败:", response.status_code)
        return None