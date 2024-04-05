import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

sr.LANGUAGE = "ru-RU"

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Запись пошла, говорите...")
    audio = r.listen(source)

text = r.recognize_google(audio, language="ru-RU")

print(f"Вы сказали: {text}")
