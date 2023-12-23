from tkinter import *
from downloader import Downloader
from PIL import ImageTk, Image
import os.path
from player import Player
class Window():

    def __init__(self, app):
        self.favicon = 'assets/logo.ico'
        self.icon = None
        self.dir = os.path.dirname(__file__)
        self.dir_images = os.path.join(self.dir, 'assets')
        self.load_window(app)
        self.load_menus(app)
        self.load_icon_youtube(app)
        self.download = Downloader.get_form_audio(self, app)
        self.player = None
        self.app = app


    #Configuración básica de la aplicación de escritorio

    def load_window(self, app):
        app.title('Aplicación para descargar audios de Youtube')
        app.config(bd=50, bg="#c5c5d5")
        app.resizable(0,0)
        
        #Cargar favicon
        image = PhotoImage(file=self.favicon)
        app.iconphoto(True, image)

    #Cargar imagen con el logo de Youtube en la columna izquierda

    def load_icon_youtube(self, app):
        container = Frame(app)
        icon = ImageTk.PhotoImage(Image.open(os.path.join(self.dir_images, 'youtube.png')))
        self.icon = icon
        foto = Label(container, image=self.icon, padx="20px", pady="20px", bg="#c5c5d5", anchor="center")
        foto.grid(column=0, row=0)
        container.grid(column=0)
        container.anchor('center')

    #Cargar menús de la aplicación

    def load_menus(self, app):
        menubar = Menu(app, background="#313131", foreground="#fff")
        menuhelper = Menu(menubar, tearoff=0)
        menuhelper.add_command(label="Datos del desarrollador")
        app.config(menu=menubar)
        menubar.add_command(label="Inicio", command=self.show_downloader)
        menubar.add_command(label="Reproductor", command=self.show_downloader)
        menubar.add_cascade(label="Información", menu=menuhelper)
        menubar.add_command(label="Salir", command=app.destroy)

    #Función para mostrar el panel de descargas
    
    def show_downloader(self):
        if(self.player is not None):
            self.player.grid_remove()
        self.download.grid(row=0, column=1)

    #Función para cargar el reproductor   
    def show_player(self):
        self.download.grid_remove()
        self.player = Player.get_player(self, self.app)
    
   