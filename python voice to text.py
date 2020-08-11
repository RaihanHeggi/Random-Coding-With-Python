import speech_recognition as s 
import pyttsx3 as p

start = s.Recognizer()

def voiceToText(command):
    engine = p.init() 
    engine.say(command)  
    engine.runAndWait() 

while(1):
    with s.Microphone() as source: 
        try:
            start.adjust_for_ambient_noise(source, duration=0.2) 
            audioData = start.record(source, duration=5)
            textData = start.recognize_google(audioData, language="id-ID")
            print(textData)
            voiceToText(textData)
        except Exception as e:
            print(e) 