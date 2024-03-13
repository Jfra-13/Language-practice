import random 

adivina = random.randint(1,10)

print("Hola, cual es tu nombre?: ")
user_name = input()

print("Muy bien " + user_name + " Intenta adivinar el numero que pienso entre el 1 y 10")
print("Aproposito, solo tienes 3 intentos")

num = int(input("Ingresa el numero que crees: "))

if num == adivina:
    print("Ganaste")
else:
    if num > adivina:
        print("Muy altooo")
    else:
        print("Muy pequeñooooo")
        
    print("\nTe quedan 2 intentos")
    num = int(input("Intenta otra vez: "))
    
    if num == adivina:
        print("Ganaste")
    else:
        if num > adivina:
            print("Muy altooo")
        else:
            print("Muy pequeñooooo")
        
        print("\nTe quedan 1 intentos")
        num = int(input("Intenta otra vez: "))
    
        if num == adivina:
            print("Ganaste")
        else:
            print("Perdiste lo siento")




