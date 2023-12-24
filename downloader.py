from pytube import YouTube
from tkinter import *
import tkinter.font as TkFont
import os.path
from helpers import *
from moviepy.editor import AudioFileClip



#Clase que gestiona la acción de descarga

class Downloader():
    
    def __init__(self):
        self.dir = os.path.join(os.path.dirname(__file__), 'songs')


    #Cargar formulario de youtube
        
    def get_form_audio(self, app):
        
        container = Frame(app, background="#c5c5d5", height=100, padx=50, pady=50)
        container.grid(row=0, column=1)
        fontStyle = TkFont.Font(family="Poppins", size=18)
        instrucciones = Label(container, bg="#c5c5d5", text='Downloader', justify="left", font=fontStyle, anchor="w")
        instrucciones.grid(row=0, column=0)
        label = Label(container, bg="#c5c5d5", text="Introduce enlace", font=fontStyle, anchor="w")
        label.grid(row=1, column=0)
        self.input = Entry(container, width=50, justify="left")
        self.input.grid(row=2, column=0, pady=10)
        boton = Button(container, text="Descargar", fg="#fff", font=fontStyle)
        boton.bind('<Button-1>', lambda event: self.download_song(container, event))
        boton.configure(bg="#007bff", justify="center")
        boton.grid(row=3, column=0, ipadx=10, pady=30)
        return container
    
    #Descargar audio de Youtube
        
    def download_song(self, app, event):
        link = self.input.get()
        
        try:
            mp4 = self.execute(link)
            message = show_message(app, 'success', 'Canción descargada con éxito')
            self.convert_mp4_to_mp3(mp4['path'], mp4['title'])
        except DownloadError as error:
            message = show_message(app, 'danger', error)
        except Exception as error:
            message = show_message(app, 'danger', error)
            print(error)

    #Marcar mensaje de descarga
    def execute(self, url):
        if(len(url) <= 0):
            raise DownloadError('El enlace no es correcto')
        else:
            py = YouTube(url)
            song = py.streams.filter(only_audio=True).first()
            mp4 = song.download(self.dir)
            path_mp4 = os.path.join(self.dir, py.title + '.mp4')
            print(path_mp4)
            if(mp4 == None):
                raise DownloadError('No se ha generado el mp4')
            else:
                return {'title': py.title, 'path': path_mp4, 'song': song}
            
    def convert_mp4_to_mp3(self, path, title):
        if(os.path.isfile(path)):
            song = AudioFileClip(path)
            song.write_audiofile(os.path.join(self.dir, title + '.mp3'))
            song.close()
            os.remove(path)


            
    

    

        