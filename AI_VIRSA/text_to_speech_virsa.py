# text_to_speech_virsa.py

import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
    log_response(text)

def log_response(response):
    with open("ai_responses.txt", "a") as file:
        file.write(response + "\n")

if __name__ == "__main__":
    speak("Hello, this is a test.")
