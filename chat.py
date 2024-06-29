import requests
import json


def create_message(role, content):
    return {"role": role, "content": content}


def request_model(messages):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3:8b",
        "messages": messages,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get response: ", response.status_code)
        print("Response Content:", response.content)


def main():
    while True:
        messages = [create_message("system", "请使用中文进行所有对话。")]
        while True:
            user_input = input("You: ")
            if user_input == "exit":
                print("Goodbye!")
                break
            messages.append(create_message("user", user_input))
            response_data = request_model(messages)
            print("Assistant: ", response_data["message"]["content"])
            messages.append(create_message("assistant", response_data["message"]["content"]))


main()
