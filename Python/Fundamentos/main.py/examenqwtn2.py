from tkinter import *

def mensaje():
    lbl = Label(dic, text="Diccionario")
    lbl.pack()

dic = Tk()
dic.geometry("400x280")
dic.title("Pregunta2")
lbl = Label(dic,height=5,width=10)
lbl.pack()

txtword = Entry(dic,textvariable="")
txtword.pack()

Label(dic,text="Diccionario", bg="Green").pack()
Label(dic, text="Significado:").pack()
Label(dic, text="Sinonimo:").pack()
Label(dic, text="Antonimo:").pack()



btn = Button(dic,text="Enviar", command=mensaje)
btn.pack()
dic.mainloop()