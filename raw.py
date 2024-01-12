import speech_recognition as sr
import pyttsx3
import datetime
from transformers import GPT2LMHeadModel, GPT2Tokenizer

name = "VIRSA (Virtual Intelligent Response System of Arshvir)"

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voices[0].id)

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def speak(text):
    print(f"{name}: {text}\n")
    engine.say(text)
    engine.runAndWait()

def wishMe():
    try:
        hour = int(datetime.datetime.now().hour)
    except Exception as e:
        print(f"Error getting current hour: {e}")
        hour = 0

    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Arsh, oops I mean boss!")

    else:
        speak("Good Evening Arsh, oops I mean boss!")

    speak("I am " + name)

def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt", max_length=100)
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
        return query
    except Exception:
        print("Say that again please...")
        return "None"

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'hi' in query or 'hello' in query:
            speak("Hello, how can I help you?")
        elif 'who are you' in query:
            speak("I am " + name)
        elif 'how are you' in query:
            speak("I am fine, thanks for asking")
        elif 'bye' in query:
            speak("Bye. Have a nice day")
            exit()
        else:
            response = generate_response(query)
            speak(response)
