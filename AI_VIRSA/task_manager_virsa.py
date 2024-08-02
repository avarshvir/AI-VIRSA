# task_manager_virsa.py

import webbrowser
import requests
from bs4 import BeautifulSoup
from text_to_speech_virsa import speak
from speech_to_text_virsa import listen
import os
import random
import subprocess
import threading
import time

# Define the absolute path for the Songs directory
MUSIC_FOLDER = r"E:\Python Project\Python AI\AI-VIRSA\AI_VIRSA\Songs"

# Global variable for listening state
listening = True


def open_browser(browser_name):
    browsers = {
        "edge": "microsoft-edge:",
        "microsoft edge": "microsoft-edge:",
        "opera": "opera"
    }

    if browser_name in browsers:
        webbrowser.get(browsers[browser_name]).open_new("")
        speak(f"Opening {browser_name}.")
    else:
        speak(f"Sorry, I don't support opening {browser_name} yet.")


def open_website(website_name):
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "instagram": "https://www.instagram.com"
    }

    if website_name in websites:
        webbrowser.open(websites[website_name])
        speak(f"Opening {website_name}.com.")
    else:
        speak(f"Sorry, I don't support opening {website_name} yet.")


def get_top_news():
    url = "https://news.google.com/news/rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")

    news_list = soup.find_all("item", limit=5)
    top_news = "Here are the top news for today: "

    for news in news_list:
        top_news += news.title.text + ". "

    speak(top_news)


"""def play_music(genre):
    global listening
    genre_folders = {
        "soothing": "soothing_songs",
        "romantic": "romantic_songs",
        "gangster": "gangster_songs",
        "party": "party_songs"
    }

    if genre in genre_folders:
        genre_path = os.path.join(MUSIC_FOLDER, genre_folders[genre])
        if os.path.exists(genre_path):
            songs = [os.path.join(genre_path, song) for song in os.listdir(genre_path) if song.endswith('.mp3')]
            if songs:
                song_to_play = random.choice(songs)
                speak(f"Playing a {genre} song.")
                try:
                    if os.name == 'nt':  # Windows
                        process = subprocess.Popen(['start', song_to_play], shell=True)
                    else:
                        process = subprocess.Popen(('open', song_to_play))

                    thread = threading.Thread(target=monitor_music_process, args=(process,))
                    thread.start()
                except Exception as e:
                    speak(f"An error occurred while trying to play the song: {e}")
            else:
                speak(f"No songs found in the {genre} genre.")
        else:
            speak(f"The {genre} genre folder does not exist.")
    else:
        speak("Sorry, I didn't understand the genre.")


def monitor_music_process(process):
    global listening
    listening = False
    time.sleep(120)  # Pause listening for 2 minutes

    # Wait for the music process to complete if it's still running
    while process.poll() is None:
        time.sleep(1)

    listening = True
"""

#MUSIC_FOLDER = r"E:\Python Project\Python AI\AI-VIRSA\AI_VIRSA\Songs"

def play_music(genre):
    global listening
    genre_folders = {
        "soothing": "soothing_songs",
        "romantic": "romantic_songs",
        "gangster": "gangster_songs",
        "party": "party_songs"
    }

    if genre in genre_folders:
        genre_path = os.path.join(MUSIC_FOLDER, genre_folders[genre])
        if os.path.exists(genre_path):
            songs = [os.path.join(genre_path, song) for song in os.listdir(genre_path) if song.endswith('.mp3')]
            if songs:
                song_to_play = random.choice(songs)
                speak(f"Playing a {genre} song.")
                try:
                    os.startfile(song_to_play)  # Open the mp3 file with the default media player
                    thread = threading.Thread(target=monitor_music_process)
                    thread.start()
                except Exception as e:
                    speak(f"An error occurred while trying to play the song: {e}")
            else:
                speak(f"No songs found in the {genre} genre.")
        else:
            speak(f"The {genre} genre folder does not exist.")
    else:
        speak("Sorry, I didn't understand the genre.")

def monitor_music_process():
    global listening
    listening = False
    time.sleep(120)  # Pause listening for 2 minutes
    listening = True

def check_news_keywords(task):
    with open("news_keywords.txt", "r") as file:
        keywords = file.read().splitlines()
    for keyword in keywords:
        if keyword in task:
            return True
    return False


def handle_task(task):
    global listening
    task = task.lower()

    if check_news_keywords(task):
        get_top_news()
        return

    if "open browser" in task:
        speak("Which browser should I open?")
        browser_name = listen().lower()
        open_browser(browser_name)
    elif "open" in task:
        website_mapping = {
            "youtube": "youtube",
            "google": "google",
            "instagram": "instagram",
            "microsoft edge": "edge",
            "edge": "edge",
            "opera": "opera"
        }
        for keyword, browser_or_website in website_mapping.items():
            if keyword in task:
                if browser_or_website in ["edge", "opera"]:
                    open_browser(browser_or_website)
                else:
                    open_website(browser_or_website)
                return
        speak("Which browser should I open?")
        browser_name = listen().lower()
        open_browser(browser_name)
    elif "top news" in task:
        get_top_news()
    elif "play music" in task:
        speak("What genre of music would you like to listen to?")
        genre = listen().lower()
        play_music(genre)
    else:
        speak("Sorry, I didn't understand the task.")


if __name__ == "__main__":
    speak("Testing task manager.")
    handle_task("open youtube")
    handle_task("what are today's top news")
