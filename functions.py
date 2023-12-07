from pytube import YouTube
from tkinter import messagebox as MessageBox

def popup():
    MessageBox.showinfo("Sobre mí", 'Programador de Python')
def download_song(link):
    url = link.get()
    song = YouTube(url)
    download = song.streams.get_audio_only()
    download.download()