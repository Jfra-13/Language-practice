import tkinter
ventana = Tk()

ventana.geometry("480x280")
ventana.title("Nivel de satisfaccion")
def saludar ():
    print("Hola, esperemos que se encuentre bien")
    print("Podría comentarnos del 1 al 5 su nivel de satisfacción")
    print("1 -> Bastante Mejorable, ")
    print("2 -> Mejorable, ")
    print("3 -> Mediocre, ")
    print("4 -> Buena, ")
    print("5 -> Recomendable")
saludar ()
num = input("Ingrese numero: ")
num = int(num)
if (num == 3):
    print ("Sentimos no haber cumplido del todo sus expectativas." "Nos encantaría que dejara un comentario compartiendo cuales fueron los componentes que no le agradaron del todo, eso nos ayudaría a mejorar nuestros servicios.")
    comentario=input ("Ingrese comentario: ")
    print ("Le agradecemos por su honestidad y tiempo brindado, esperamos tenga un buen día.")
elif (num < 3):
print ("Sentimos mucho que haya pasado un mal momento." "Nos encantaría que dejara un comentario compartiendo cuales fueron sus malestares, eso nos ayudaría a mejorar nuestros servicios.")
    comentario=input ("Ingrese comentario: ")
    print ("Nos disculpamos nuevamente por la mala experiencia que tuvo, esperamos tenga un buen día.")
elif (num > 5):
    print ("Esto no es posible")
else:
    print ("Nos sentimos felices de haber cumplido tus expectativas. Si tienes alguna sugerencia, por favor dejanos un comentario.")
    comentario = input ("Ingrese comentario: ")
print ("Muchas gracias por su comentario.")

ventana.mainloop()
