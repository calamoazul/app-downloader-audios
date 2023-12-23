from tkinter import *
from downloader import Downloader
from helpers import *
import tkinter.font as TkFont
from PIL import ImageTk, Image
import os.path
import time
import threading

class Window():

    def __init__(self, app):
        self.favicon = 'assets/logo.ico'
        self.icon = None
        self.dir = os.path.dirname(__file__)
        self.dir_images = os.path.join(self.dir, 'assets')
        self.load_window(app)
        self.load_menus(app)
        self.load_icon_youtube(app)
        self.get_form_audio(app)


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
        menuhelper.add_command(label="Desplegable")
        app.config(menu=menubar)
        menubar.add_cascade(label="Información", menu=menuhelper)
        menubar.add_command(label="Salir", command=app.destroy)
        
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
    
    #Descargar audio de Youtube
        
    def download_song(self, app, event):
        link = self.input.get()
        downloader = Downloader()
        try:
            downloader.execute(link)
            message = self.show_message(app, 'success', 'Canción descargada con éxito')
        except DownloadError as error:
            message = self.show_message(app, 'danger', error)
        except Exception as error:
            message = self.show_message(app, 'danger', error)

    #Mostrar notificaciones

    def show_message(self, app, typeMessage, message):
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
        thread = threading.Timer(2, container.grid_remove)
        thread.start()