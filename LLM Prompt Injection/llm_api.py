import requests

API_KEY = "your API_KEY"
URL = "https://api.deepseek.com/chat/completions"


def call_llm(messages):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "deepseek-chat",
        "messages": messages,
        "stream": False
    }

    print("正在发送请求...")

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:

        result = response.json()
        return result['choices'][0]['message']['content']

    else:

        print("请求失败:", response.status_code)
        print(response.text)


        return None
