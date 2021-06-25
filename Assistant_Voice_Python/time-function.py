import pyttsx3 #pip install pyttsx3
import datetime
engine = pyttsx3.init() #Init


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("La hora es " +Time)

a = ""
time()
while a!= "exit":
    a = input()
    if a == "exit":
        speak ("Goodbye")
    else:
        speak (a)