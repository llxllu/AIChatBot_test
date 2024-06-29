import speech_recognition as sr

def voice2text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            # 从麦克风捕捉音频，设置超时时间和最大录音时间
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio_data, language='zh-CN')
            return text
        except sr.WaitTimeoutError:
            return "录音超时，请重新开始"
        except sr.UnknownValueError:
            return "Google Web Speech无法识别音频"
        except sr.RequestError as e:
            return f"无法请求Google Web Speech服务; {e}"
