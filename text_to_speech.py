from gtts import gTTS
import os 

print("Silahkan masukkan text : \n")
inputText = str(input())

language = 'ID'
output = gTTS(text=inputText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")