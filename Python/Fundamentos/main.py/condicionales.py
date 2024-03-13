from tkinter import Label


edad = int(input("Ingrese su edad"))

if (edad < 0):
    print("Error: Ingreso edad negativa")
elif(edad>=18):
    print("Es mator de edad")
    if(edad>=60):
        print("Hace parte de la tercera edad")
else:
    print("Es menor de edad")


    
