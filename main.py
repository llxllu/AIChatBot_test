import requests
import json

# 设置API的URL（确保端口号正确）
url = "http://localhost:11434/api/generate"

# 定义请求的负载
payload = {
    "model": "llama3:8b",
    "prompt": "你好",
    "stream": False  # 如果希望获得完整的响应而不是流式响应，设置为False
}

# 设置请求头
headers = {
    "Content-Type": "application/json"
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 解析响应
if response.status_code == 200:
    response_data = response.json()
    print("Generated Text: ", response_data["response"])
else:
    print("Failed to get response: ", response.status_code)
    print("Response Content:", response.content)
