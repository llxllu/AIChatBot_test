from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import requests
import json
import os
from tools.text2voice import text2voice
from tools.clearCache import clear_folder
from tools.voice2text import voice2text
from Interact import Llama
import uuid

clear_folder()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/text2voice', methods=['POST'])
def text_to_voice_route():
    text = request.form['text']
    audio_filename = f"static/cache/{uuid.uuid4()}.mp3"
    text2voice(text, audio_filename)
    return jsonify(audio_url=f'/{audio_filename}')


@app.route('/voice2text', methods=['POST'])
def voice_to_text_route():
    try:
        text = voice2text()
        return jsonify(text=text)
    except Exception as e:
        return jsonify(error=str(e)), 500


@socketio.on('send_message')
def handle_send_message(data):
    messages = data['messages']
    user_message = data['message']

    if not messages:
        messages.append(Llama.create_message("system", "你现在扮演一个智能语音机器人，并且只能用中文交流。"))

    messages.append(Llama.create_message("user", user_message))
    emit('receive_message', {'role': 'user', 'content': user_message})

    assistant_message = ""
    for word in Llama.stream_model(messages):
        assistant_message += word
        emit('receive_message', {'role': 'assistant', 'content': assistant_message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
