from window import Window
from pytube import YouTube
from tkinter import messagebox as MessageBox
from tkinter import *
import os.path

class Downloader():
    
    def __init__(self):
        self.dir = os.path.join(os.path.dirname(__file__), 'songs')
        self.notification = None


    #Marcar mensaje de descarga
       
    def run(self):
        self.app = Window()
        self.app.run()
        url = self.app.get_url()
        self.execute(url)
        self.app.loop()
    def execute(self, url):
        if(len(url) > 0):
            py = YouTube(url)
            try:
                song = py.streams.filter(only_audio=True).first()
                song.download(self.dir)
                self.notification = self.show_message("info", "Canción descargada")
                self.notification.grid(row=2, columnspan=2)
                self.notification.grid_remove()
                self.notification = self.show_message("success", "Canción descargada")
                self.notification.grid(row=2, columnspan=2)
            except Exception as error:
                self.notification.grid_remove()
                self.notification = self.show_message("danger", error)
                self.notification.grid(row=2, columnspan=2)
                print(error)
            else:
                return song.title
    
    def show_message(self, typeMessage, message):

        if(typeMessage == 'success'):
            color = "#22C55E"
        elif(typeMessage == 'danger'):
            color = "#DC2626"
        else: 
            color = "#22D3EE"
        container = Frame(self.app.tk, background=color, padx=30, pady=30)
        text = Label(container, textvariable=message, font="Poppins", foreground="#fff", justify="center")
        text.grid(column=0, row=0)
        return container

    

        