import pyttsx3


def text2voice(text):
    # 初始化 TTS 引擎
    engine = pyttsx3.init()

    # 设置语速
    engine.setProperty('rate', 150)

    # 设置音量
    engine.setProperty('volume', 1.0)

    # 设置语音（语言和地区）
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'zh' in voice.id:  # 查找中文语音
            engine.setProperty('voice', voice.id)
            break

    # 转换文本为语音
    engine.say(text)

    # 等待语音播放完成
    engine.runAndWait()


# 示例用法
text = "你好，这是一个文本转语音的示例。"
text2voice(text)
