import pyttsx3 #pip install pyttsx3
import datetime
import numpy

engine = pyttsx3.init() #Init
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The hour is " +Time)

def date():
    Month = numpy.array (["Januery", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    year = int(datetime.datetime.now().year) #Get the Year
    month = int(datetime.datetime.now().month) #Get the Month
    day = int(datetime.datetime.now().day) #Get the Day
    speak("Today is ")
    speak(day)
    speak(Month[month-1])
    speak(year)

def wishme():
    speak("Welcome back sir !")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak("Good Morning")
    elif hour > 12 and hour <=18:
        speak("Good afternoon")
    elif hour > 18 and hour <=24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("How I can help you?")

wishme()