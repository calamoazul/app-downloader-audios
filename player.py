

from pygame import *
from downloader import Downloader
import os.path
import os
from tkinter import Frame, Label, Button
#Clase para el reproductor de música


class Player(Downloader):
    def __init__(self):
        super.__init__()
        self.icon = ''
        self.songs = []

    def get_player(self, app):
        with os.scandir(self.dir) as songs:
            for song in songs:
                if(song not in self.songs):
                    self.songs.append(song.name)
        player = Frame(app, background="313131", padx=50, pady=50)
        self.play_song = self.songs[0]
        play_song = Label(player, textvariable=self.play_song, background="#313131", foreground="#22C55E")
        play_song.pack()
        return player
