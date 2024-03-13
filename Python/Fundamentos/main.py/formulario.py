from tkinter import * 
from tkinter import messagebox as MessageBox
from tkinter import ttk
from PIL import ImageTk, Image


def emergente():
    cantidad = valor_input.get()
    m = var1.get()
    f = var2.get()
    #sIndex = lstCursos.curselection()
    #curso = lstCursos.get(sIndex)
    pago = lstDesplegable.get()
    cadena = cantidad +" - "+ pago
    MessageBox.showinfo("Valores ingresados ", cadena)
    

    
my_W = Tk()
    
    #Inicializamos la variable valor_input
valor_input = StringVar()
    
    #Definimos el tamaño de la ventana
my_W.geometry("400x280")
    
    #Creamos labels para que se muestren en nuestra ventana
Label(my_W, text="Introduzca datos", bg="LightGreen").pack()
Label(my_W, text="Total de alumnos", bg="LightGreen").pack()
    
    #Generamos cajas de texto 
txtCantidad = Entry(my_W, textvariable=valor_input)
txtCantidad.pack()
    
Label(my_W, text="Cursos", bg="LightGreen").pack()
    
lstCursos = Listbox(my_W, height=8, width=20, bg="yellow")
    
lstCursos.insert(0,"Matematica")
lstCursos.insert(1,"Filosofia")
lstCursos.insert(2,"Literatura")
lstCursos.insert(3,"Arte")
lstCursos.pack()
    
    #Agregamos una etiqueta tipo de pago
Label(my_W, text="Tipo de pago", bg="LightGreen").pack()
    
    #Lista deplegabble
lstDesplegable = ttk.Combobox(my_W,width=10)
formas_pago = ["Efectivo","Tarjeta"]
lstDesplegable['values']=formas_pago
lstDesplegable.pack()

#checkbox
var1 = IntVar()
var2 = IntVar()
Checkbutton(my_W, text="Masculino",variable=var1).pack()

Checkbutton(my_W, text="Femenino",variable=var2).pack()

#Image
#image1 = Image.open(file="polar.png")
#test = ImageTk.PhotoImage(image1)
#Label(my_W,image=test).pack()



    #Button
b1 = Button(my_W, text='Enviar', bg='White', command="emergente")
b1.pack()

my_W.mainloop()
    
   
