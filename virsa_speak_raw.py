import threading
import tkinter as tk
from datetime import datetime
import pyttsx3
import speech_recognition as sr





engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voices[1].id)


def greet_and_introduce():
    # Generate greeting
    hour = datetime.now().hour
    if hour < 12:
        greet_text = "Good Morning Sir"
    elif 12 <= hour < 17:
        greet_text = "Good Afternoon Sir"
    else:
        greet_text = "Good Evening Sir"

    # Speak greeting and introduction
    engine.say(greet_text)
    engine.say("I am VIRSA, Virtual Intelligent Response System of Arshvir")
    engine.runAndWait()



def listen_and_respond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")


        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)

            if "hi" in text or "hello" in text:
                response = " hi Hello Sir, how can I assist you?"
            else:
                response = "Could not understand, please try again"

            engine.say(response)
            engine.runAndWait()

        except:
            print("Sorry, could not recognize your voice")


# Call on start
greet_and_introduce()
listen_and_respond()





