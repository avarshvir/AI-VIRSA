#virsa_speak.py
import random
import webbrowser
import win32com.client
import speech_recognition as sr
import os


from songs import play_random_song
from virsa_date_time import *
#from wikipedia_content import result

'''def search_and_play_song(song_name):
    music_directory = r"E:\Python Project\Python AI\songs"
    available_songs = [song.lower() for song in os.listdir(music_directory)]

    # Convert song_name to lowercase for case-insensitive comparison
    song_name_lower = song_name.lower()

    if song_name_lower in available_songs:
        # If the requested song is in the list, play it
        speaker.Speak(f"Playing {song_name} sir...")
        # Add logic to play the specific song based on its name
        # For simplicity, play_random_song is used as a placeholder
        play_random_song()
    else:
        speaker.Speak(f"Sorry, {song_name} is not available. Playing a random song instead.")
        play_random_song()'''


def set_voice_by_name(speaker, voice_name):
    voices = speaker.GetVoices()
    for voice in voices:
        if voice.GetDescription() == voice_name:
            speaker.Voice = voice
            break

speaker = win32com.client.Dispatch("SAPI.SpVoice")
set_voice_by_name(speaker, "Microsoft David Desktop - English (United States)")

# Adjust rate (words per minute) and volume (0 to 100)
#speaker.Rate = -1  # Adjust the rate (0 is the default, higher values are faster)
#speaker.Volume = 100  # Adjust the volume (0 to 100)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        return random.choice([
            "Sorry boss, I could not hear you properly. Could you please say again?",
            "I’m sorry, I didn’t catch that. Could you please repeat what you said?",
            "Excuse me, I didn’t hear you clearly. Could you please say that again?",
            "I’m sorry, I missed what you said. Could you please repeat it?"
        ])
    except Exception as e:
        return "Sorry boss, I could not hear you properly. Could you please say again?"


if __name__ == '__main__':
    print('VIRSA')
    speaker.Speak(greet())
    print(greet())
    #print("Enter the word you want to speak it out by computer")

    while True:
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                #break

        # madeBy = takeCommand()
        # madeBy = [["created you"], ["developed you"], ["made you"]]
        # for madeBy in madeBy:
        #     if f"Who {madeBy[0]}".lower() in madeBy.lower():
        #         speaker.Speak(f"I am {madeBy[0]} by Arshvir")

        if "play music" in query.lower() or "open music" in query.lower():
            print("Sure! Which song would you like to listen to?")
            speaker.Speak("Sure! Which song would you like to listen to?")
            user_response = takeCommand().lower()

            if "anyone" or "any" or "play any song" in user_response:
                speaker.Speak("Playing song sir..")
                play_random_song()
            else :
                    #speaker.Speak(f"Searching for {user_response} and playing it.")
                    #search_and_play_song(user_response)
                speaker.Speak("okay sir")

        elif "time" in query:
            response = random.choice(time_responses)
            speaker.Speak(response)



        else :
            speaker.Speak(query)
            #print("v")

        #if query:
         #   speaker.Speak(query)
