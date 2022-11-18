import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes
import pywhatkit
import sys
import requests
import json
import time
import pyautogui


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

''' speak function for string output in speaker '''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

''' It takes microphone input from user and return string output '''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')

        except Exception as e:
            speak('Say that again please...')
            return 'None'
        return query


''' wishes me according to the time as sson as I activate my assistant '''
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning")
    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    print("I'm Optimus Sir, how may I help you?")
    speak("I'm Optimus Sir, how may I help you?")

''' Latest news updates '''
def news():
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=79dac29996d0466f9e431942d9c4c1ba"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news, listen carefully")
    speak("Thanks for listening...")

''' In which city we are in '''
def location():
    speak('wait sir, let me check')
    try:
        ipAddr = requests.get('https://api.ipify.org').text
        url = "https://get.geojs.io/v1/ip/geo/"+ipAddr+".json"
        geo_rqst = requests.get(url)
        geo_data = geo_rqst.json()
        city = geo_data['city']
        country = geo_data['country']
        print(f"Sir I'm not sure, but I think we are in {city} city of country {country}")
        speak(f"Sir I'm not sure, but I think we are in {city} city of country {country}")
    except Exception as e:
        speak("Sorry sir, due to network issue I'm unable to fetch the location...")
        pass

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak('Opening google...')
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak('Opening gmail...')
            webbrowser.open("gmail.com")

        elif 'open youtube' in query:
            speak('Opening youtube...')
            webbrowser.open("youtube.com")

        elif 'open github' in query:
            speak('Opening github...')
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = r'C:\Users\adri2\OneDrive\Desktop\Songs'
            songs = os.listdir(music_dir) 
            # print(songs)
            sng = random.choice(songs)
            os.startfile(os.path.join(music_dir, sng))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strtime}")

        elif 'the date' in query:
            strday = datetime.datetime.now().strftime("%A %d %B %Y")
            speak(f"Sir, the date is {strday}")

        elif 'open code' in query:
            code_path = r"C:\Users\adri2\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            speak('Opening vs code...')
            os.startfile(code_path)
        
        elif 'open sublime' in query:
            sublime_path = r"C:\Users\adri2\OneDrive\Desktop\Sublime Text Build 3211 x64\sublime_text.exe"
            speak('Opening sublime text...')
            os.startfile(sublime_path)
        
        elif 'open command prompt' in query:
            speak('Opening command prompt...')
            os.system('start cmd')
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'send message' in query:
            speak("Please tell the recipient mobile's number")
            phno = int(input("Please tell the recipient mobile's number: "))
            hrs = int(input("Enter hours: "))
            mint = int(input("Enter minutes: "))
            msg = input("Enter the message: ")

            pywhatkit.sendwhatmsg('+91'+str(phno), msg, hrs, mint)

        elif 'play youtube song' in query:
            speak("Please, tell me the song's name")
            sng = input("Please, tell me the song's name: ")
            speak('Opening YouTube...')
            pywhatkit.playonyt(sng)

        elif 'news' in query:
            speak('Fetching the latest news... Please wait.')
            news()
        
        elif 'where I am' in query or 'where we are' in query:
            location()

        elif 'take screenshot' in query:
            speak("Sir, please tell me the name of the screenshot file")
            name = takeCommand().lower()
            speak('Sir, please hold the screen for few seconds, I am taking screenshot...')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.jpeg")
            speak("I am done sir, the screenshot is saved in our main folder...")

        elif 'power down' in query:
            speak("See you soon sir...")
            sys.exit()