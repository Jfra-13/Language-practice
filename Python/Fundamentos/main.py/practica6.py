from tkinter import *

def mensaje():
    lbl = Label(ventana, text="Este es un [Label] tkinter click")
    lbl.place(relx=0.5, rely=0.5, anchor='center')
    
if __name__ == '__main__':
    
    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("Clase 20 - Estructura de datos")
    
    l1 = Listbox(ventana, height=30, width=40, bg='black')
    l1.place(x=10, y=12)
    
    b1 = Button(ventana, text='boton', bg='black')
    b1.place(x=20, y=5)

    ventana.mainloop()