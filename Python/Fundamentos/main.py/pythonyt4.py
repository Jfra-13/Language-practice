from cgitb import text

seguirChateando = True
while seguirChateando:
    texto = input(">")
    if text =="Salir":
        seguirChateando = False
    texto = texto.replace(":)","🙂")

print(texto)



