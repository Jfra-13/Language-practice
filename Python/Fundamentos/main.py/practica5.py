numero = 45
control=0
intentos=1
print("Bienvenido al juego de adivinanza")
while(control==0):
    print("intento numero",intentos)
    print("ingrese un numero")
    num = int(input())
    if (num==numero):
        print("!Adivinaste el numero¡")
        print("Utilizaste",intentos,"intentos")
        print("Fin del juego")
        control=1
    elif(num > numero):
        print("Mayor")
        intentos+=1
    elif(num < numero):
        print("Menor")
        intentos+=1
    