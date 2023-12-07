from tkinter import *
from functions import *
from tkinter import messagebox as MessageBox
import tkinter.font as TkFont
from PIL import ImageTk, Image
import os.path

class Window():

    def __init__(self):
        self.tk = Tk()
        self.favicon = 'assets/logo.ico'
        self.icon = None
        self.dir = os.path.dirname(__file__)
        self.dir_images = os.path.join(self.dir, 'assets')
        self.url = ''


    #Configuración básica de la aplicación de escritorio

    def load_window(self):
        self.tk.geometry("1920x1080")
        #La app no se podrá redimensionar
        self.tk.title('Aplicación para descargar audios de Youtube')
        self.tk.config(bd=50, bg="#c5c5d5")
        self.tk.columnconfigure(0, weight=1)
        self.tk.columnconfigure(1,weight=3)
        self.tk.rowconfigure(0, weight=1)
        self.tk.rowconfigure(1, weight=1, pad="20px")
        self.tk.rowconfigure(2, weight=1)
        
        #Cargar favicon)
        image = PhotoImage(file=self.favicon)
        self.tk.iconphoto( False,image)
    
    #Cargar imagen con el logo de Youtube en la columna izquierda

    def load_icon_youtube(self):
        icon = ImageTk.PhotoImage(Image.open(os.path.join(self.dir_images, 'youtube.png')))
        self.icon = icon
        foto = Label(self.tk, image=self.icon, padx="20px", pady="20px", bg="#c5c5d5")
        foto.grid(row=0, column=0)

    #Cargar menús de la aplicación

    def load_menus(self):
        menubar = Menu(self.tk, bg="#313131", fg="#fff")
        self.tk.config(menu=menubar)
        helpmenu = Menu(menubar, tearoff=0, borderwidth="0px", bd="25", bg="#313131", fg="#fff")
        menubar.add_cascade(label="Para más información", menu=helpmenu)
        helpmenu.add_command(label="Información del autor", command=self.popup)
        menubar.add_command(label="Salir", command=self.tk.destroy)
        fontStyle = TkFont.Font(family="Poppins", size=30)
        instrucciones = Label(self.tk, bg="#c5c5d5", text='Script para descargar canciones de Youtube\n', font=fontStyle)
        instrucciones.grid(row=0, column=1)

    #Obtener audio de Youtube
    def get_audio(self):
        self.link = Entry(self.tk)
        link = self.link
        link.grid(row=1, column=1, padx="40px")
        boton = Button(self.tk, text="Descargar", fg="#fff" , command=self.download_song)
        boton.configure(bg="#007bff")
        boton.grid(row=2, column=1)

    #Marcar mensaje de descarga

    def popup(self):
        MessageBox.showinfo("Sobre mí", 'Programador de Python')
    def download_song(self):
        message = Label(self.tk, text="Descargando canción...")
        message.grid(row=2, column=2)
        self.url = self.link.get()

    #Ejecutar TKinter

    def run(self):
        self.load_window()
        self.load_menus()
        self.load_icon_youtube()
        self.get_audio()
        self.tk.mainloop()

    def get_url(self):
        return self.url
