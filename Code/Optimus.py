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
from DataBase import database
import json
import time
import psutil
import pyautogui
from pywikihow import search_wikihow
import speedtest
import operator
from translate import Translator
# from plyer import notification
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI3 import Ui_Optimus


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)
engine.setProperty('volume', 1.0)

''' speak function for string output in speaker '''


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


''' wishes me according to the time as sson as I activate my assistant '''


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
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


'''Adding Contact to database'''


def addContact(self):
    speak("Please tell the name of the person")
    # name = self.takeCommand()
    name = input("Name: ")
    speak("Please tell the valid mobile number of the person")
    # phno = self.takeCommand()
    phno = input("Mobile No.: ")
    print(
        f"Please check the details of the person is valid\nName:- {name}\tPhone:- {phno}")
    speak("say 'yes' to continue")
    # choice = self.takeCommand()
    choice = input("yes/no: ")
    if choice == 'yes':
        database.addOne(name.lower(), phno)
        speak(f"{name} added to your contact")


''' Send WhatsApp message '''


def message(self):
    speak("What should I say?")
    msg = self.takeCommand()
    speak("Whom should I send this message?")
    name = self.takeCommand().lower()
    num = str(database.showPhno(name))
    t = datetime.datetime.now()
    if num != None:
        speak("Your message will be send within few seconds...")
        pywhatkit.sendwhatmsg("+91"+num, msg, int(
            t.strftime('%H')), int(t.strftime('%M'))+1)
    else:
        print("No such name exists...")
        speak("No such name exists...")


''' How to do mode '''


def how_to_do(self):
    speak("How to do moode is activated")
    while True:
        speak('Please tell me what do you want to know...')
        how = self.takeCommand()
        try:
            if 'exit' in how or 'close' in how:
                speak('Okay sir, how to do mode is terminated...')
                break
            else:
                max_result = 1
                how_to = search_wikihow(how, max_result)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)
        except Exception as e:
            speak('Sorry sir, I am unable to find this...')


''' In which city we are in '''


def location(self):
    speak('wait sir, let me check')
    try:
        ipAddr = requests.get('https://api.ipify.org').text
        url = "https://get.geojs.io/v1/ip/geo/"+ipAddr+".json"
        geo_rqst = requests.get(url)
        geo_data = geo_rqst.json()
        city = geo_data['city']
        country = geo_data['country']
        print(
            f"Sir I'm not sure, but I think we are in {city} city of country {country}")
        speak(
            f"Sir I'm not sure, but I think we are in {city} city of country {country}")
    except Exception as e:
        speak("Sorry sir, due to network issue I'm unable to fetch the location...")
        pass
        return self.query


''' Weather updates according to your location '''


def weather(self):
    user_api = 'e0d4692367a91ec92b7aad360ae37e3e'
    speak('Please, tell me the location')
    search = self.takeCommand()
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

        speak(f"Currently in {search} it is {temp} degree celcious with {weather_desc}, humidity with {hmdt}% and wind speed about {wind_spd} kilometers per hour")


''' COVID-19 stats in your state/city '''


def stats_of_covid(self):
    speak('For which state or city you want me to show stats')
    name = self.takeCommand()
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

    headers = {
        'x-rapidapi-key': "01df05162fmsh3d9cbd5c4b11eb9p1ab742jsn819cf5fb84f5",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()

    for state in response['state_wise']:
        if int(response['state_wise'][state]['active']) != 0:
            if state.lower() == name.lower():
                print('----------------------------------------')
                print(f"COVID-19 Stats for {state} state:-")
                print('----------------------------------------')
                print(
                    f"Confirmed cases: {response['state_wise'][state]['confirmed']}")
                print(
                    f"Active cases: {response['state_wise'][state]['active']}")
                print(
                    f"Death rate: {response['state_wise'][state]['deaths']}")
                print(
                    f"Recovered rate: {response['state_wise'][state]['recovered']}")
                speak(f"Showing stats of {state} state...")
                speak(
                    f"Confirmed cases are {response['state_wise'][state]['confirmed']}")
                speak(
                    f"Active cases are {response['state_wise'][state]['active']}")
                speak(
                    f"Death rate are {response['state_wise'][state]['deaths']}")
                speak(
                    f"And recovered rate are {response['state_wise'][state]['recovered']}")

        for city in response['state_wise'][state]['district']:
            if city.lower() == name.lower():
                print('----------------------------------------')
                print(f"COVID-19 Stats for {city} city:-")
                print('----------------------------------------')
                print(
                    f"Confirmed cases: {response['state_wise'][state]['district'][city]['confirmed']}")
                print(
                    f"Active cases: {response['state_wise'][state]['district'][city]['active']}")
                print(
                    f"Death rate: {response['state_wise'][state]['district'][city]['deceased']}")
                print(
                    f"Recovered rate: {response['state_wise'][state]['district'][city]['recovered']}")
                speak(f"Showing stats of {city} city...")
                speak(
                    f"Confirmed cases are {response['state_wise'][state]['district'][city]['confirmed']},")
                speak(
                    f"Active cases are {response['state_wise'][state]['district'][city]['active']}")
                speak(
                    f"Death rate are {response['state_wise'][state]['district'][city]['deceased']}")
                speak(
                    f"And recovered rate are {response['state_wise'][state]['district'][city]['recovered']}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        while True:
            self.query = self.takeCommand()
            if 'hi' in self.query or 'hello' in self.query or 'are you there' in self.query:
                self.taskExecution()

    def takeCommand(self):

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
                print('Say that again please...')
                return 'None'
            query = query.lower()
            return query

    def taskExecution(self):
        wishMe()
        while True:

            ''' Logic for executing tasks based on query '''
            self.query = self.takeCommand()
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to wikipedia...")
                print(results)
                speak(results)

            elif 'open google' in self.query:
                speak("what do you want to search?")
                srch = self.takeCommand()
                speak('Opening google...')
                webbrowser.open("https://www.google.com/search?q="+srch+".com")

            elif 'gmail' in self.query or 'email' in self.query:
                speak('Opening gmail...')
                webbrowser.open("https://gmail.com")

            elif 'open youtube' in self.query:
                speak('Opening youtube...')
                webbrowser.open("https://youtube.com")

            elif 'open github' in self.query:
                speak('Opening github...')
                webbrowser.open("https://github.com/")

            elif 'close google' in self.query:
                speak('Closing google chrome...')
                os.system('taskkill /f /im chrome.exe')

            elif 'music' in self.query:
                music_dir = r'C:\Users\adri2\OneDrive\Desktop\Songs'
                songs = os.listdir(music_dir)
                sng = random.choice(songs)
                os.startfile(os.path.join(music_dir, sng))

            elif 'time' in self.query:
                strtime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {strtime}")

            elif 'date' in self.query:
                strday = datetime.datetime.now().strftime("%A %d %B %Y")
                speak(f"Sir, the date is {strday}")

            elif 'open code' in self.query:
                code_path = r"C:\Users\adri2\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                speak('Opening vs code...')
                os.startfile(code_path)

            elif 'close code' in self.query:
                speak('Ok sir, closing VS Code...')
                os.system("taskkill /f /im Code.exe")

            elif 'open sublime' in self.query:
                sublime_path = r"C:\Users\adri2\OneDrive\Desktop\Sublime Text Build 3211 x64\sublime_text.exe"
                speak('Opening sublime text...')
                os.startfile(sublime_path)

            elif 'close sublime' in self.query:
                speak('Ok sir, closing sublime text...')
                os.system("taskkill /f /im sublime_text.exe")

            elif 'open command prompt' in self.query:
                speak('Opening command prompt...')
                os.system('start cmd')

            elif 'open onedrive' in self.query:
                drive_path = r"C:\Users\adri2\OneDrive\Desktop\OneDrive"
                speak('Ok sir, opening onedrive')
                os.startfile(drive_path)

            elif 'open file explorer' in self.query:
                drive_path = r"C:\Users\adri2\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\File Explorer"
                speak('Ok sir, opening File Explorer')
                os.startfile(drive_path)

            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif 'volume up' in self.query:
                pyautogui.press('volumeup')

            elif 'volume down' in self.query:
                pyautogui.press('volumedown')

            elif 'mute' in self.query:
                pyautogui.press('volumemute')

            elif 'hello' in self.query or 'hi' in self.query:
                speak('yes sir, what can I do for you?')

            elif 'thank' in self.query or 'thanks' in self.query:
                speak("It's my pleasure sir")

            elif 'translate' in self.query:
                speak("Please tell me the text you want me to translate ")
                stmt = self.takeCommand()
                print(stmt)
                speak("To which language do you want to translate:")
                dst = self.takeCommand()
                print(dst)
                translator = Translator(to_lang=dst)
                translation = translator.translate(stmt)
                print(translation)
                speak(translation)

            elif 'message' in self.query:
                speak('Sir, Please make sure your are logged in to whatsApp')
                message(self)

            elif 'add contact' in self.query:
                addContact(self)

            elif 'remove contact' in self.query:
                speak("Please tell the name of the person you want to remove")
                # name = self.takeCommand()
                rmname = input("Enter the name")
                database.deleteOne(rmname)
                speak(f"{rmname} deleted successfully...")

            elif 'all contacts' in self.query:
                speak("Please wait a second...")
                database.showAll()

            elif 'play youtube song' in self.query or 'songs on youtube' in self.query:
                speak("Please, tell me the song's name")
                sng = self.takeCommand()
                speak('Opening YouTube...')
                pywhatkit.playonyt(sng)

            elif 'activate how to do mode' in self.query:
                how_to_do(self)

            elif 'battery percentage' in self.query:
                battery = psutil.sensors_battery()
                percent = str(battery.percent)
                print(f'Your device has been running on {percent}% battery')
                speak(f'Your device has been running on {percent}% battery')

            elif 'internet speed' in self.query:
                speak('Checking for internet speed, it might take few seconds...')
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                print(
                    f' Downloading Speed:- {round(dl*0.000000125, 3)} MB \n Uploading Speed:- {round(up*0.000000125, 3)} MB')
                speak(
                    f'Sir, we have {round(dl*0.000000125, 3)} MB downloading speed and {round(up*0.000000125, 3)} MB uploading speed...')

            elif 'news' in self.query:
                speak('Fetching the latest news... Please wait.')
                news()

            elif 'where i am' in self.query or 'where we are' in self.query:
                location(self)

            elif 'weather' in self.query:
                weather(self)

            elif 'covid-19' in self.query:
                stats_of_covid(self)

            elif 'calculate' in self.query or 'calculation' in self.query:
                speak('what do you want to calculate, example 4 plus 4')
                while True:
                    cal = self.takeCommand()
                    try:
                        if 'no' in cal or 'close' in cal:
                            speak('Thank you sir...')
                            break
                        else:
                            def get_operator_fn(op):
                                return{
                                    '+': operator.add,  # plus
                                    '-': operator.sub,  # minus
                                    'x': operator.mul,  # multiplied by
                                    'divided': operator.__truediv__,  # divided
                                }[op]

                            def eval_binary_expr(op1, opr, op2):
                                op1, op2 = int(op1), int(op2)
                                return get_operator_fn(opr)(op1, op2)
                            print(
                                f'your result is: {eval_binary_expr(*(cal.split()))}')
                            speak(
                                f'your result is: {eval_binary_expr(*(cal.split()))}')
                            speak('want to calculate again?')
                            cal = self.takeCommand()

                    except Exception as e:
                        speak('Invalid numbers, try again')

            elif 'screenshot' in self.query:
                speak(
                    'Sir, please hold the screen for few seconds, I am taking screenshot...')
                time.sleep(3)
                img = pyautogui.screenshot()
                speak("Sir, please tell me the name of the screenshot file")
                name = self.takeCommand().lower()
                img.save(f"{name}.jpeg")
                speak("I am done sir, the screenshot is saved in our main folder...")

            elif 'copy the text' in self.query:
                pyautogui.hotkey('ctrl', 'c', interval=0.15)
                speak('Copied sir...')

            elif 'cut the text' in self.query:
                pyautogui.hotkey('ctrl', 'x', interval=0.15)
                speak('done sir...')

            elif 'paste the text' in self.query:
                pyautogui.hotkey('ctrl', 'v', interval=0.15)
                speak('Pasted sir...')

            elif 'power down' in self.query:
                speak("See you soon sir...")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Optimus()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            r"Images\7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            r"Images\T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        # self.ui.movie = QtGui.QMovie(
        #     r"C:\Users\adri2\OneDrive\Desktop\Python GUI\GUI\gif-3.gif")
        # self.ui.label_4.setMovie(self.ui.movie)
        # self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.textBrowser_2.setText(label_time)
        self.ui.textBrowser_2.setAlignment(QtCore.Qt.AlignCenter)


app = QApplication(sys.argv)
Optimus = Main()
Optimus.show()
exit(app.exec_())
