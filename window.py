from tkinter import *
from downloader import Downloader
from helpers import *
import tkinter.font as TkFont
from PIL import ImageTk, Image
import os.path

class Window():

    def __init__(self, app):
        self.favicon = 'assets/logo.ico'
        self.icon = None
        self.dir = os.path.dirname(__file__)
        self.link = ''
        self.dir_images = os.path.join(self.dir, 'assets')
        self.load_window(app)
        self.load_menus(app)
        self.load_icon_youtube(app)
        self.get_form_audio(app)


    #Configuración básica de la aplicación de escritorio

    def load_window(self, app):
        app.geometry("1920x1080")
        app.title('Aplicación para descargar audios de Youtube')
        app.config(bd=50, bg="#c5c5d5")
        #Cargar favicon
        image = PhotoImage(file=self.favicon)
        self.tk.iconphoto( False,image)
    
    #Cargar imagen con el logo de Youtube en la columna izquierda

    def load_icon_youtube(self, app):
        container = Frame(app)
        icon = ImageTk.PhotoImage(Image.open(os.path.join(self.dir_images, 'youtube.png')))
        self.icon = icon
        foto = Label(container, image=self.icon, padx="20px", pady="20px", bg="#c5c5d5")
        foto.grid(column=0, row=0)
        container.grid(column=0, rowspan=1)

    #Cargar menús de la aplicación

    def load_menus(self, app):
        menubar = Menu(app, background="#313131", foreground="#fff")
        app.config(menu=menubar)
        menubar.add_command(label="Salir", command=app.destroy)
        

    #Cargar formulario de youtube
        
    def get_form_audio(self, app):
        
        container = Frame(app, padx=30)
        fontStyle = TkFont.Font(family="Poppins", size=18)
        instrucciones = Label(container, text='Script para descargar canciones de Youtube\n', font=fontStyle)
        instrucciones.grid(row=0, column=0)
        label = Label(container, text="Introduce enlace", font=fontStyle, justify="left", padx=20)
        label.grid(row=1, column=0, padx=20)
        inputForm = Entry(container, width=100, justify="left")
        self.link = input.get()
        inputForm.grid(row=2, column=0, padx="40px")
        boton = Button(container, text="Descargar", fg="#fff", font=fontStyle, command=self.download_song(app))
        boton.configure(bg="#007bff", justify="center")
        boton.grid(row=3, column=0)
        container.grid(row=1, column=1)

    #Descargar audio de Youtube
        
    def download_song(self, app):
        info_message = self.show_message(app, 'info', 'Descargando canción')
        info_message.grid(row=2, column=1)
        downloader = Downloader()
        try:
            song = downloader.execute(self.link)
            if song:
                info_message.grid_remove()
                message = "Canción: {} descargada con éxito".format(song)
                self.show_message(app, 'success', message)
            else:
                info_message.grid_remove()
                successmessage = self.show_message(app, 'success', 'Canción descargada con éxito')
                successmessage.grid(row=2, column=1)
        except DownloadError as error:
            info_message.grid_remove()
            message_error = self.show_message(app, 'danger', error)
            message_error.grid(row=2, column=1)
    
    #Mostrar notificaciones

    def show_message(self, app, typeMessage, message):
        if(typeMessage == 'success'):
            color = "#22C55E"
        elif(typeMessage == 'danger'):
            color = "#DC2626"
        else: 
            color = "#22D3EE"
        container = Frame(app, background=color, padx=30, pady=30)
        text = Label(container, textvariable=message, font="Poppins", foreground="#fff", justify="center")
        text.grid(column=0, row=0)
        return container