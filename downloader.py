from pytube import YouTube
from tkinter import *
import os.path
from helpers import *

#Clase que gestiona la acción de descarga
class Downloader():
    
    def __init__(self):
        self.dir = os.path.join(os.path.dirname(__file__), 'songs')



    #Marcar mensaje de descarga
    def execute(self, url):
        if(len(url) > 0):
            raise DownloadError('El enlace no es correcto')
        else:
            py = YouTube(url)
            song = py.streams.filter(only_audio=True).first()
            song.download(self.dir)
            if(song.title == None):
                return False
            else:
                return song.title
    
    

    

        