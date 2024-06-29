import speech_recognition as sr

def voice2text():
    # 初始化识别器
    recognizer = sr.Recognizer()

    # 设置麦克风作为音频源
    with sr.Microphone() as source:
        print("请说话...")

        # 调整识别器的敏感度以适应环境噪音
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            # 从麦克风捕捉音频，设置超时时间和最大录音时间
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            # 使用Google Web Speech API进行语音识别
            text = recognizer.recognize_google(audio_data, language='zh-CN')
            print("识别结果: " + text)
        except sr.WaitTimeoutError:
            print("录音超时，请重新开始")
        except sr.UnknownValueError:
            print("Google Web Speech无法识别音频")
        except sr.RequestError as e:
            print(f"无法请求Google Web Speech服务; {e}")

voice2text()
