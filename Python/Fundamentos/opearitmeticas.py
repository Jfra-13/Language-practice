from __future__ import division


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exponente (a, b):
    return a ** b

def radicacion (a, b):
    return a ** (1/b)

n1  = float(input("Ingrese el primer numero: "))
n2  = float(input("Ingrese el segundo numero: "))

print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Exponenciación")
print("6.Radicación")
 
opc = int(input("Ingrese la opcion que desea: "))

if opc == 1: 
    print(n1, "+",n2, "=",suma(n1,n2))

elif opc == 2: 
    print(n1, "-",n2, "=",resta(n1,n2))

elif opc == 3: 
    print(n1, "*",n2, "=",multiplicacion(n1,n2))

elif opc == 4: 
    print(n1, "/",n2, "=",dividir(n1,n2))

elif opc == 5: 
    print(n1, "**",n2, "=",exponente(n1,n2))

elif opc == 6: 
    print(n1, "^",n2, "=",radicacion(n1,n2))

else:
    print("Error ingrese un numero valido")