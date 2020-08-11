import pyttsx3

engine = pyttsx3.init()

inputText = str(input("Silahkan Masukkan Text yang ingin diucapkan: "))
engine.voice.Voice(languages="ID")
engine.say(inputText)

engine.runAndWait()