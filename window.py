from tkinter import *
from functions import *
import os.path

class Window():

    def __init__(self):
        self.tk = Tk()
        self.favicon = './assets/logo.ico'
        self.icon = './assets/youtube.png'

    #Configuración básica de la aplicación de escritorio

    def __load_window(self):
        """  self.tk.geometry("750x450") """
        #La app no se podrá redimensionar
        self.tk.resizable(0,0)
        self.tk.title('Aplicación para descargar audios de Youtube')
        self.tk.config(bd=15, bg="#c5c5d5")
        #Cargar favicon
        favicon = os.path.abspath(self.favicon)
        if os.path.isfile(favicon):
            image = PhotoImage(file=favicon)
            self.tk.iconphoto( False,image)
    
    #Cargar imagen con el logo de Youtube en la columna izquierda

    def __load_icon_youtube(self):

        image = os.path.abspath(self.icon)
        if os.path.isfile(image):
            icon = PhotoImage(file=image)
            foto = Label(self.tk, image=icon, bd=0)
            foto.pack(padx="10px", pady="10px")
            foto.grid(row=0, column=0)

    #Cargar menús de la aplicación

    def __load_menus(self):
        menubar = Menu(self.tk)
        menubar.config(bg='#313131')
        self.tk.config(menu=menubar)
        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Para más información", menu=helpmenu)
        helpmenu.add_command(label="Información del autor", command=popup)
        menubar.add_command(label="Salir", command=self.tk.destroy)
        instrucciones = Label(self.tk, text='Script para descargar canciones de Youtube\n')
        instrucciones.grid(row=0, column=1)

    #Obtener audio de Youtube

    def get_audio(self):
        link = Entry(self.tk)
        link.grid(row=1, column=1)
        boton = Button(self.tk, text="Descargar")
        boton.bind('<Enter>', download_song)
        boton.configure(bg="#007bff")
        boton.grid(row=2, column=1)

    #Ejecutar TKinter

    def run(self):
        self.__load_window()
        self.__load_icon_youtube()
        self.__load_menus()
        self.get_audio()
        self.tk.mainloop()
