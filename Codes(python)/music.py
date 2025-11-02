import os
import pygame

music_path = "/storage/emulated/0/CODES/music"
songs = [f for f in os.listdir(music_path) if f.endswith(".mp3")]
print(songs)

player = input("Enter the song name: ")

if player in songs:
    song_path = os.path.join(music_path, player)
    
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    
    k = input("type stop to stop: ").lower()
    if k == "stop":
        pygame.mixer.music.stop()
    
else:
    print("No song found")