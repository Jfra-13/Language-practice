from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import moviepy.editor as mp
import shutil

root = Tk()
root.title("Mp4 to Mp3")
root.geometry("500x500")
logo = PhotoImage(file = "mp3.png")
new_logo = logo.subsample(3,3)

def ubi():
    path = filedialog.askdirectory()
    etiquetaUbi.config(text=path, fg="blue")
    

def mp4():
    thefile = filedialog.askopenfilename(initialdir="/", title="Escoge el video", filetypes=(("mp4 files","*.mp4"),("wav files","*.wav")))
    user_path = etiquetaUbi.cget("text")
    clip = mp.VideoFileClip(thefile)
    audio_file = thefile[:-4] + ".mp3"
    clip.audio.write_audiofile(audio_file)
    clip.close()
    shutil.move(audio_file, user_path)
    alert.config(text="Conversion Completa", fg="green")
    



etiqueta = Label(root, text="Convierte tus videos a Mp3", font=("Roboto",11)) 
etiqueta.pack()

etiqueta1 = Label(root, image= new_logo)
etiqueta1.pack()

etiquetaUbi = Label(root, text="Seleccione ruta de descarga", font=("Roboto", 11))
etiquetaUbi.pack()

ubi = Button(root, text="Ruta de descarga", bg="#F9E79F",padx=5, pady=5, font=("Roboto", 11), command=ubi)
ubi.pack(pady=10)

SelectFile = Button(root, text="Select file",bg="white", padx=5,pady=5,font=("Roboto",11) , command=mp4)
SelectFile.pack(pady=10)

alert = Label(root, text="", font=("Roboto", 11), fg="green")
alert.pack()



root.mainloop()