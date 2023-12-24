

import pygame
from downloader import Downloader
import os.path
import os
from tkinter import Frame, Label, Button
#Clase para el reproductor de música


class Player(Downloader):
    def __init__(self):
        super().__init__()
        self.icon = ''
        self.songs = []
        self.play_song = None
    def get_player(self, app):
        canciones = os.listdir(self.dir)
        with os.scandir(self.dir) as songs:
            for song in songs:
                if(song not in self.songs):
                    self.songs.append(song.name)
        player = Frame(app, background="#313131", padx=50, pady=50, height=100)
        self.play_song = self.songs[0]
        play_song = Label(player, text=self.play_song, background="#313131", foreground="#22C55E")
        play_song.pack()
        try:
            print(self.dir)
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(self.dir, self.songs[0]))
            pygame.mixer.music.play()
        except Exception as error:
            print(canciones[0])
            print(error)
        return player
