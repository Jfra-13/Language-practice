def calcularIMC(peso,alturam):
    imc = peso / (alturam*alturam)
    return imc


peso = float(input("Ingrese su peso en kg: "))
alturacm = int(input("Ingrese su altura en cm: "))
alturam = alturacm / 100
imc = calcularIMC(peso,alturam)

print("Su imc es de " + str(imc))

if imc < 20:
    print("Estado de delgadez")
if imc >= 20 and imc < 26:
    print("Peso normal")
if imc >= 27 and imc < 30:
    print("Sobre peso")
if imc >= 30:
    print("Obesidad")

