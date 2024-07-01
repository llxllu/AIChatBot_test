import requests
import json
import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return [encoded_string]


def create_message(role, content, image=None):
    if image is None:
        return {"role": role, "content": content}
    return {"role": role, "content": content, "images": image}


def stream_model(messages):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llava:latest",
        "messages": messages,
        "stream": True,
    }
    headers = {
        "Content-Type": "application/json"
    }

    with requests.post(url, headers=headers, data=json.dumps(payload), stream=True) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    yield json.loads(line.decode('utf-8'))['message']['content']
        else:
            print("Failed to get response: ", response.status_code)
            print("Response Content:", response.content)
            yield "Error: Failed to get response from model"


def request_model(messages):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llava:latest",
        "messages": messages,
        "stream": False,
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


def chat_with_Llava():
    while True:
        messages = [create_message("system", "请使用中文进行所有对话。")]
        while True:
            user_input = input("You: ")
            image_input = input("Image: ")
            if user_input == "exit":
                print("Goodbye!")
                break
            messages.append(
                create_message("user", user_input, image=None if image_input == "" else image_to_base64(image_input)))
            response_data = request_model(messages)
            print("Assistant: ", response_data["message"]["content"])
            print(messages)
            messages.append(create_message("assistant", response_data["message"]["content"]))

