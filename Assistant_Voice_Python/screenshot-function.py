import pyttsx3 #pip install pyttsx3
import datetime
import numpy
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy #pip install spotipy
import sys
import pprint
import webbrowser as web
import pyautogui #pip install pyautogui
from time import sleep 

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

def screenshot():
    #You have to install Pillow
    img = pyautogui.screenshot()
    img.save("") #Path to save

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
            chromepath = "C:/Users/angel/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe %s" #path of your browser
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "log out" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            song_dir = "" #Path of the song
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0]))
        elif "spotify" in query:
            #to get client_id and client_secret go  https://developer.spotify.com/dashboard/
            client_id = '8aff2ace649a4629b1781c59d4dcc565'
            client_secret='391383f3b8bf4de7a70ee6fa1c407608'
            flag = 0
            speak("Which song do I search?")
            correct = False
            while correct == False:
                song = takeCommand().upper()
                speak("Is that your song?")
                print(song)
                if takeCommand().lower() == "yes":
                    correct = True
                else:
                    speak("Said that again please")
            speak("Do you lnow the author?")
            correct = False
            if takeCommand().lower()== "yes":
                while correct == False:
                    author = takeCommand()
                    speak("Is that your author?")
                    print(author)
                    if takeCommand().lower() == "yes":
                        correct = True
                    else:
                        speak("Said that again please")
            else:
                author = ''
            #song = 'Fin del Mundo'.upper()
            sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id,client_secret))
            if len(author)>0:
                result = sp.search(author)
                for i in range(0, len(result["tracks"]["items"])):
                    name_song = result["tracks"]["items"][i]["name"].upper()
                    if song in name_song:
                        flag = 1
                        web.open(result["tracks"]["items"][i]["uri"])
                        sleep(5)
                        pyautogui.press("enter")
            if flag == 0:
                song = song.replace(" ", "%20")
                web.open(f'spotify:search:{song}')
                sleep(5)
                for i in range(18):
                    pyautogui.press("tab")        
                for i in range(2):
                    pyautogui.press("enter")
                    sleep(1)
        elif "remember" in query:
            speak("What should I remembrer?")
            data = takeCommand()
            speak("You said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "give me the reminders" in query:
            remember = open ("data.txt", "r")
            speak("You said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done")
        