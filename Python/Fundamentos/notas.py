def comprobarContraseña(password):    
    largo = False
    mayus = False
    numer = False
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True
    if largo and mayus and numer:
        return True
    else:
        return False
password = input("Enter your password: ")
verificacion = comprobarContraseña(password)
if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña es incorrecta")




    