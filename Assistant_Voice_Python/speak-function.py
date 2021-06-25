import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init() #Init

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
a = ""
while a!= "exit":
    a = input()
    speak (a)