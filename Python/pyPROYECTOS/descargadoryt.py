from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

def select_path():
    path = filedialog.askdirectory()
    label3.config(text = path, fg="blue")
    
def dowload():
    get_link = entry1.get()
    user_path = label3.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    shutil.move(mp4_video, user_path)
    alert.config(text="Descarga Completa", fg="green")



root = Tk()
root.title("YouTube Downloader")
#root.geometry("568x519")
logo = PhotoImage(file = "Yt.png")
new_logo = logo.subsample(3,3)

label = Label(root, text="Descarga tus videos", font=('Roboto',15))
label.pack()

label1 = Label(root, image=new_logo)
label1.pack()

label2 = Label(root,text="Coloque el enlace", font=('Roboto', 11))
label2.pack()

entry1 = Entry(root, width = 40, highlightcolor= "red", highlightthickness=2, font= ('Roboto', 11))
entry1.pack()

label3 = Label(root, text="Seleccione la ruta de descarga", font=('Roboto', 11))
label3.pack()

boton1 = Button(root,text="Ruta de descarga", bg="#F9E79F", padx=5, pady=5, font=("Roboto", 11), command=select_path)
boton1.pack()

boton2 = Button(root, text="Descargar", bg="#82E0AA",padx=5, pady=5, font=("Roboto",11), command=dowload)
boton2.pack(pady=10)

alert = Label(root, text="", font=("Roboto",11), fg="green")
alert.pack()

root.mainloop()



