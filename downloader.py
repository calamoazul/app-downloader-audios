from window import Window
from pytube import YouTube
from tkinter import *
import os.path

class Downloader():
    
    def __init__(self):
        self.dir = './songs'


    #Marcar mensaje de descarga
       
    def run(self):
        app = Window()
        app.run()
        return app.get_url()
    
    def execute(self, url):
        if(len(url) > 0):
            py = YouTube(url)
            try:
                song = py.streams.filter(only_audio=True).first()
                song.download(self.dir)
            except Exception as error:
                print(error)
            finally:
                print('Fin descarga')
    

        