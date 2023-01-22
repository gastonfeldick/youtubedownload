from pytube import YouTube
from getpass import getuser
from pytube.cli import on_progress
import time
import webbrowser

def abrirNavegador():
    webbrowser.open_new("https://gitlab.com/users/gastonfeldick/projects")

def on_progress(stream, chunk, bytes_remaining):
    '''
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    inc=int(percentage_of_completion)
    print(inc)
    my_progress["value"]+=inc-my_progress["value"]
    label2.config(text=f"{inc}%")
    if my_progress["value"]==100:
        my_progress.grid_forget()
        label2.grid_forget()
        label2["text"]="0%"
        messagebox.showinfo("Youtube Downloader","Downloaded Successfully...\nPath: C:/Yotube Downloader By Coder Community")
    '''
    pass

def tamañoTitulo(url):
    if(len(url))>25:
        titulo=""

def audio(self,link):
    yt=YouTube(link)
    try:
        audio=yt.streams.get_audio_only()

        self.estado.setText("Descargando")
        audio.download(filename=f"{yt.title}.mp3")
        self.estado.setText("Completado")
        self.barra.setValue(100)
    except:
        print("no hay internet")
    
    

def video(self,link):
    yt=YouTube(link)
    try:
        video=yt.streams.get_highest_resolution()
        self.estado.setText("Descargando")
        video.download(filename=f"{yt.title}.mp4")
        self.estado.setText("Completado")
        self.barra.setValue(100)

    except:
        print("no hay internet")
    


def buscar(self):
    url=self.url.text()
    self.frameDescarga.hide()
    if not(url==""):
        try:
            yt=YouTube(url)
            self.descargar.show()
            self.labelTitulo.show()
            self.titulo.show()
            self.titulo.setText(yt.title)
            
        except:

            self.descargar.hide()
            self.titulo.show()
            self.titulo.setText("No encontrado")
    else:
        self.descargar.hide()
        self.titulo.show()
        self.titulo.setText("No encontrado")
        

        


def descargar(self):
    tipo=self.formato.currentText()
    self.frameDescarga.show()
    url=self.url.text()
    if tipo=="MP4":
        video(self,url)
    elif tipo=="MP3":
        audio(self,url)
    
    self.descargar.hide()
    self.url.setText("")
    '''
    url=self.url.text()
    user=getuser()
    path="/home/"+user+"/Download"
    formato=self.formato.currentText()
    print(path)
    self.frameDescarga.show()
    if not(url==""):
        yt=YouTube(url)
        titulo=yt.title
        print(url)
        print(formato)
        print(titulo)'''
    