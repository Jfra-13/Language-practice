"""print(len("Hola")) cantidad de letras
print("b".isupper())  mayuscula o minuscula
print("hola".isnumeric()) saber si es numero o no
cadena = "Hola"
print(cadena[2])
for i in range(len(cadena)): muestra en cadena las letras o numeros 
    print(cadena[i])"""

def comprobarContraseña(password):
    largo = False
    mayus = False
    numer = False
    if len(password) > 8 :
        largo = True
    for i in range(len(password)):
        if password [i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True
    if largo and mayus and numer:
        return True
    else:
        return False
    

password = input("Ingrese su contraseña: ")

verificacion = comprobarContraseña(password)

if verificacion:
    print("La contraseña es segura ")
else:
    print("La contraseña no es segura")









    
    