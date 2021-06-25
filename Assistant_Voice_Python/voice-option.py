import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init() #Init
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 default voice, 1 male voice,2 man vocie, 3 spanish, 
newVoiceRate = 150 #word per minute
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
a = ""
while a!= "exit":
    a = input()
    if a == "exit":
        speak ("Goodbye")
    else:
        speak (a)