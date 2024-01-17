
import random
import os
def play_random_song():
    music_directory = r"E:\Python Project\Python AI\songs"
    songs = os.listdir(music_directory)
    random_song = random.choice(songs)
    music_path = os.path.join(music_directory, random_song)
    os.startfile(music_path)


'''
def search_and_play_song(song_name):
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