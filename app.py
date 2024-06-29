from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import requests
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 使用随机生成的密钥
socketio = SocketIO(app)

def create_message(role, content):
    return {"role": role, "content": content}

def stream_model(messages):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3:8b",
        "messages": messages,
        "stream": True  # 启用流式响应
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

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_message(data):
    messages = data['messages']
    user_message = data['message']

    if not messages:
        messages.append(create_message("system", "请使用中文进行所有对话。"))

    messages.append(create_message("user", user_message))
    emit('receive_message', {'role': 'user', 'content': user_message})

    assistant_message = ""
    for word in stream_model(messages):
        assistant_message += word
        emit('receive_message', {'role': 'assistant', 'content': assistant_message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
