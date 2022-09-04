
from base64 import encode
from time import time
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I: %M %p')
        print(time)
        talk('current time is ' + time)
    elif 'wiki' in command:
        person = command.replace('wiki','')
        info = wikipedia.summary(person, 1)
        print((info).encode('utf8'))
        talk(info)
    elif "are you happy" in command:
        talk('I am very happy. What about you?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif '+' in command:
        #num1=int('+'-1)
        #num2=int('+'+1)
        #sum= num1 + num2
        #talk('the result is ' + sum)
        talk('do your homework on your own')
    else:
        talk("I couldn't get you please repeat one more time.")
while True:
    run_alexa()