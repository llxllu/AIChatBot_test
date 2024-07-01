import pyttsx3

def text2voice(text, output_filename):
    # 初始化 TTS 引擎
    engine = pyttsx3.init()

    # 设置语速
    engine.setProperty('rate', 200)

    # 设置音量
    engine.setProperty('volume', 1.0)

    # 设置语音（语言和地区）
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'zh' in voice.id:  # 查找中文语音
            engine.setProperty('voice', voice.id)
            break

    # 保存音频到文件
    engine.save_to_file(text, output_filename)

    # 等待语音生成完成
    engine.runAndWait()
