import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder

        self.tracks = [
            f for f in os.listdir(music_folder)
            if f.endswith(".mp3")
        ]

        self.tracks.sort()

        print("TRACKS:", self.tracks)  # debug

        self.index = 0

    def load(self):
        path = os.path.join(self.music_folder, self.tracks[self.index])
        print("PLAYING:", path)  # debug
        pygame.mixer.music.load(path)

    def play(self):
        self.load()
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()