import random

numero = random.randint(1,100)
intentos = 0

jugando = True

print("Adivina un numero del 1 al 100")

while jugando:
    intentos +=1
    if intentos <= 7:
        eleccion = int(input("Dime un numero: "))
        if eleccion == numero:
            print("Has necesitado",intentos,"intentos")
            jugando = False
        elif eleccion > numero:
            print("Demasiado alto. Llevas", intentos, "intentos")
        elif eleccion < numero:
            print("Demasiado bajo. Llevas", intentos, "intentos")
    else:
        print("Se te acabaron los intentos. Has perdido.")
        jugando = False
        