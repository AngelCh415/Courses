import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init() #Init

engine.say("Hello") #Text -> Speech
engine.runAndWait()
