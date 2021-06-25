import pyttsx3 #pip install pyttsx3
import datetime
import numpy
import speech_recognition as sr #pip install SpeechRecognition
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

def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1 #Wait 1 second before listen
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please.")
        return "None"
    return query

takeCommand()