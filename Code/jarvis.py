import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import json
import random
import requests
from bs4 import BeautifulSoup
import psutil
import pywhatkit
import googletrans
import gtts
import playsound
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovies
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI3 import Ui_Jarvis

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)



def speak(audio):
    ''' speak function for string output in speaker '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    ''' wishes me according to the time as sson as I activate my assistant '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I'm Optimus Sir, how may I help you?")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.takeCommand

        def takeCommand(self):
            ''' It takes microphone input from user and return string output '''
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listenting...")
                r.pause_threshold = 1
                audio = r.listen(source)
            
            try:
                print("Recognizing...")
                self.query = r.recognize_google(audio,language='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                # print(e)
                print("Say that again please...")
                return "None"
            return query

if __name__ == "__main__":

    wishMe()
    while True:
        self.query = self.takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open github' in query:
            webbrowser.open("github.com")
    
        elif 'play music' in query:
            music_dir = r'C:\Users\adri2\OneDrive\Desktop\Songs'
            songs = os.listdir(music_dir) 
            print(songs)
            sng = random.randint(1,9)
            os.startfile(os.path.join(music_dir, songs[sng]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strtime}")

        elif 'the date' in query:
            strday = datetime.datetime.now().strftime("%A %d %B %Y")
            speak(f"Sir, the date is {strday}")

        elif 'open code' in query:
            code_path = r"C:\Users\adri2\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
        
        elif 'open sublime' in query:
            sublime_path = r"C:\Users\adri2\OneDrive\Desktop\Sublime Text Build 3211 x64\sublime_text.exe"
            os.startfile(sublime_path)
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'weather' in query:
            user_api = 'e0d4692367a91ec92b7aad360ae37e3e'
            speak('Please, tell me the location')
            search = takeCommand()
            url = f"http://api.openweathermap.org/data/2.5/weather?q="+search+"&appid="+user_api
            api_link = requests.get(url)
            api_data = api_link.json()
            # print(api_data)
            if api_data['cod'] == '404':
                print(f'Invalid City {search}, please check your city name.')
            else:
                temp = round(((api_data['main']['temp']) - 273.15), 2)
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

                print('-----------------------------------------------------------------')
                print(f'Weather Stats for - {search} || {date_time}')
                print('-----------------------------------------------------------------')

                print(f'Current Temperature is: {temp} deg Celcious')
                print(f'Current weather description : {weather_desc}')
                print(f'Current Humidity: {hmdt}%')
                print(f'Wind speed: {wind_spd} km/hr')

                speak(f"Currently in {search} it is {temp} degree celcious with {weather_desc}, and wind speed about {wind_spd} kilometers per hour, and humidity with {hmdt}%")
        
        elif 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percent = str(battery.percent)

            print(f'Your device has been running on {percent}% battery')
            speak(f'Your device has been running on {percent}% battery')

        elif 'send message' in query:
            phno = int(input("Please tell the recipient mobile's number: "))
            speak("Please tell the recipient mobile's number")
            hrs = int(input("Enter hours: "))
            mint = int(input("Enter minutes: "))
            msg = input("Enter the message: ")

            pywhatkit.sendwhatmsg('+91'+str(phno), msg, hrs, mint)

        elif 'news today' in query:
            speak("News for today.. Lets begin")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=79dac29996d0466f9e431942d9c4c1ba"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                print(article['title'])
                speak(article['title'])
                speak("Moving on to the next news..Listen Carefully")

            speak("Thanks for listening...")

        elif 'translate' in query:
            translator = googletrans.Translator()
            print("Please! tell the word or statement you want to translate...")
            speak("Please! tell the word or statement you want to translate...")
            stmt = takeCommand()
            # print("In which language you want to translate...?")
            # speak("In which language you want to translate...?")
            out_lang = 'hi'
            translated = translator.translate(stmt, dest=out_lang)
            print(translated.text)
            converted_audio = gtts.gTTS(translated.text, lang=out_lang)
            converted_audio.save('sample.mp3')
            playsound.playsound('sample.mp3')
            
        elif 'power down' in query:
            speak("See you soon sir...")
            break



