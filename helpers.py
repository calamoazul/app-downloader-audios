import threading
from tkinter import Frame, Label
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