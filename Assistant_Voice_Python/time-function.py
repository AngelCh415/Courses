import pyttsx3 #pip install pyttsx3
import datetime
engine = pyttsx3.init() #Init
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 default voice, 1 male voice,2 man vocie, 3 spanish, 
newVoiceRate = 150 #word per minute
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The hour is " +Time)


time()
