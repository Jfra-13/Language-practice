from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk




Jf_x = Tk()

Jf_x.geometry("480x280")
Jf_x.config(bg="yellow")
Jf_x.title("EJERCICIO DE CLASE")

#Imagen
image = Image.open('C:\Juanfrapython\main.py\sunflower.jpg')
image = image.resize((100,100), Image.ANTIALIAS)

img = ImageTk.PhotoImage(image)
lbl_img = Label(Jf_x,image=img)
lbl_img.pack()

#Nombre caja de texto 1
Label(Jf_x, text="Usuario").pack()
#Caja de texto 1
txtUsuario = Entry(Jf_x, textvariable="")
txtUsuario.pack()
#Nombre caja de texto 2
Label(Jf_x,text="Contraseña").pack()
#Caja de texto 2
txtContraseña = Entry(Jf_x,textvariable="")
txtContraseña.pack()

#Caja desplegable de opciones
lstDesplegable = ttk.Combobox(Jf_x,width=10)
op_selec = ["Usuario","Administrador"]
lstDesplegable['values']=op_selec
lstDesplegable.pack()

#Checkbox
recordar = IntVar()
Checkbutton(Jf_x, text="Recordarme", variable=recordar).pack()

#Boton
btn = Button(Jf_x, text="Iniciar", bg="white", command="Emergente")
btn.pack()



Jf_x.mainloop()