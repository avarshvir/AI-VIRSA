# speech_to_text_virsa.py

import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            log_command(text)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."

def log_command(command):
    with open("ai_responses.txt", "a") as file:
        file.write(f"User: {command}\n")

if __name__ == "__main__":
    print(listen())
