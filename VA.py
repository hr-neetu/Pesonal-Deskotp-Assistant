from email import message
from xml.etree.ElementInclude import include
import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import requests
import os
import pyautogui
import psutil
import pyjokes
import cv2
import time
import wolframalpha
import subprocess
import pywhatkit as kit
import phonenumbers


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speech(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


######################### function to capture your requests ##############################
def takeInstructions():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source, duration=2)
        audio = rec.listen(source)

    try:
        print("Recognising...")
        Instruction = rec.recognize_google(audio, language='en-in')
        print(Instruction)

    except Exception as exeptions:
        print(exeptions)
        speech("Say that again please...")
        return "None"
    return Instruction


######################### greetings ##############################
def greatings():
    speech("Hello")
    speech("I am Laila, your personal desktop assistant")



######################### time ##############################
def time():
    TimeRightNow = datetime.datetime.now().strftime("%I:%M:%S")
    hour = 0
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        phase = "morning"
    elif hour >= 12 and hour < 18:
        phase = "afternoon"
    elif hour >= 18 and hour <= 24:
        phase = "eveining"
    else:
        phase = "night"
    speech("Its " + TimeRightNow+" of "+phase)



######################### date ##############################
def date():
    YYYY = int(datetime.datetime.now().year)
    MM = int(datetime.datetime.now().month)
    DD = int(datetime.datetime.now().day)
    speech("current date is "+str(DD)+" "+str(MM)+" "+str(YYYY))



######################### cpu status ##############################
def CPUstatus():
    usage = str(psutil.cpu_percent())
    speech('Current CPU usage is at '+usage + "%")
    battery = psutil.sensors_battery()
    speech("Battery remaining is " + str(battery.percent)+"%")
    hdd = psutil.disk_usage('/')
    hddusage = (hdd.used/hdd.total)*100
    hddusage = round(hddusage, 2)
    speech("Storage used in C Drive is "+str(hddusage)+"%")
    frequency = psutil.cpu_freq()
    speech("Current frequency of CPU is "+str(frequency.current)+" Megha Hetz")
    RAMused = psutil.virtual_memory().percent
    speech("RAM used is "+str(RAMused)+"%")



######################### jokes ##############################
def jokes():
    speech(pyjokes.get_joke())



######################### take screenshot ##############################
def screenshot():
    img = pyautogui.screenshot()
    speech("By what name should I save it?")
    ans = takeInstructions()
    # Replace FolderPath with the path of folder where you want to save your screenshots in your computer
    ans = "Desktop"+ans+".png"
    img.save(ans)
    speech("Screenshot taken")


######################### take picture ##############################
def camera():
    speech("Press space to take image and escape to stop Camera")
    Camera = cv2.VideoCapture(0)
    cv2.namedWindow("Camera")
    img_counter = 0
    while True:
        ret, frame = Camera.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            speech("closing camera")
            break
        elif k % 256 == 32:
            img_name = "camera{}.png".format(img_counter)
            # Replace CameraPath with the path of the folder where you want to save your photos taken by camera
            path = "Desktop"
            cv2.imwrite(os.path.join(path, img_name), frame)
            cv2.imwrite(img_name, frame)
            speech("{} image taken".format(img_name))
            img_counter += 1
    Camera.release()
    cv2.destroyAllWindows()



######################### Wikipedia search ##############################
def Wikipedia(query):
    speech("Searching...")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    speech(result)


######################### OpenWebsite ##############################
def OpenWebsite():
    speech("Which website should i open?")
    # Replace ChromePath with  path of chrome.exe in your computer in the line below where it is written
    path = 'C//Users//pc//AppData//Local//Google//Chrome//Application//chrome.exe'
    website = takeInstructions().lower()
    webbrowser.get(path).open_new_tab(website+'.com')



######################### GoogleSearch ##############################
def GoogleSearch():
    speech("What should I search?")
    SearchData = takeInstructions()
    webbrowser.open(SearchData)
    speech("Here is the search result")


######################### songs ##############################
def Songs():
    songs_dir = 'C://Users//pc//Desktop//songs'
    playsongs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, playsongs[0]))


######################### what you want to rember ##############################
def Remember():
    speech("What should I remember?")
    Information = takeInstructions()
    speech('you said me to remember that '+Information)
    rem = open('data.txt', 'w')
    rem.write(Information)
    rem.close()


######################### know the remember things ##############################
def Knowing():
    remember = open('data.txt', 'r')
    speech("you said me to remember that"+remember.read())



######################### weather status ##############################
def Weather():
    speech("Which city's weather you want to know?")
    city_name = takeInstructions().lower()
    api_key = "6a7fb5fd7d27f9c86e6f2710a8e99826"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        y = data["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = data["weather"]
        weather_description = z[0]["description"]
        speech(" Temperature in kelvin unit is " + 
               str(current_temperature) + 
               "\n humidity in percentage is " +
               str(current_humidiy) + 
               "\n description  " + 
               str(weather_description))
        print(" Temperature in kelvin unit = " 
              + str(current_temperature) + 
              "\n humidity (in percentage) = " +
              str(current_humidiy) + 
              "\n description = " + 
              str(weather_description))



######################### send mail ##############################
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()




######################### send_whatsapp_message ##############################    
def send_whatsapp_message():
    speech("tell me the mobile number where you want to send message")
    phone_number = takeInstructions().lower()
    speech("tell me the message that you want to send")
    message=takeInstructions().lower()
    speech("tell me the hour")
    hour=takeInstructions().lower()
    speech("tell me seconds")
    second=takeInstructions().lower()
    pywhatkit.sendwhatmsg(phone_number,message,hour,second)



######################### open command prompt ##############################    
def opencmd():
    os.system('start cmd')



######################### openCalculator ##############################    
def openCalculator():
    calculator = "C:\\Windows\\System32\\calc.exe"
    subprocess.Popen('calculator')


######################### find_my_ip address ##############################   
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


######################### play_on_youtube ############################## 
def play_on_youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    # speech("youtube is open now")
    # time.sleep(0)


######################### help function ##############################
def help():
    speech("Here are the keywords that should be in your command for following work to be done")
    speech("MY INTRODUCTION to repeat my introduction")
    speech("TIME to get time")
    speech("DATE to get date")
    speech("CPU STATUS to get information about present condition of CPU")
    speech("JOKE to listen a joke")
    speech("SCREENSHOT to get screenshot")
    speech("CAMERA to click photos of you in webcam")
    speech("WIKIPEDIA to get do wikipedia search")
    speech("OPEN WEBSITE to open website")
    speech("SEARCH to do google search")
    speech("SONG to start a song")
    speech("REMENBER if you want me to remember something")
    speech("KNOW if you want me to tell you what you have asked me to remember earlier")
    speech("WEATHER to know a weather forcast")
    speech(" and speak HELP to repeat these thing again")



######################### main function ##############################
if __name__ == "__main__":
    greatings()
    speech("Tell me how can I help you now?")
    speech("I am ready to take command")
    speech("Say help to know all my features else continue to give command ")

    while True:
        query = takeInstructions().lower()
        if 'my introduction' in query:
            greatings()
        elif 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'cpu status' in query:
            CPUstatus()
        elif 'joke' in query:
            jokes()
        elif 'screenshot' in query:
            screenshot()
        elif 'camera' in query:
            camera()
        elif 'wikipedia' in query:
            Wikipedia(query)
        elif 'open website' in query:
            OpenWebsite()
        elif 'search' in query:
            GoogleSearch()
        elif 'song' in query:
            Songs()
        elif 'remember' in query:
            Remember()
        elif 'know' in query:
            Knowing()
        elif 'weather' in query:
            Weather()
        elif 'email to friend' in query:
            sendEmail()
        elif 'open cmd' in query:
            opencmd()
        elif 'open calculator' in query:
            openCalculator()
        elif 'IP Address' in query:
            find_my_ip()
        elif 'Open Youtube' in query:
            play_on_youtube()
        elif 'whatsapp message' in query:
            send_whatsapp_message()
        elif 'help' in query:
            help()
        elif 'offline' in query:
            break
    speech("Shutting Down. Have a nice day!")
