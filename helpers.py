import threading
from tkinter import Frame, Label
import os.path

 #Mostrar notificaciones

def show_message(app, typeMessage, message):
    if(typeMessage == 'success'):
        color = "#22C55E"
    elif(typeMessage == 'danger'):
        color = "#DC2626"
    else: 
        color = "#22D3EE"
    container = Frame(app, background=color, padx=30, pady=10)
    text = Label(container, background=color, text=message, font="Poppins", foreground="#fff", justify="center")
    text.grid(column=0, row=0)
    container.grid(row=4, column=0)
    thread = threading.Timer(5, container.grid_remove)
    thread.start()

#Método para mostrar nombres de canciones
    
def get_songs():
    songs = []
    dir_songs = os.path.join(os.path.dirname(__file__), 'songs')
    with os.scandir(dir_songs) as songs_files:
        for song in songs_files:
            if song not in songs:
                songs.append(song.name)
    return songs
#Clase para gestionar errores de desacarga

class DownloadError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    
class PlayingError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message