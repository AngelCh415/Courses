import pyttsx3 #pip install pyttsx3
import datetime
import numpy
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init() #Init
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The hour is " +Time)

def day():
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
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please.")
        return "None"
    return query

def sendmail (to, content): #email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("******", "****")#user and password
    server.sendmail("********", to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "day" in query:
            day()
        elif "offline" in query:
            speak("Goodbye Sir")
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif "search in google" in query:
            speak("What sould I search?")
            chromepath = "" #path of your browser
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
    

