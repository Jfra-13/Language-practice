H = int(input("Introduzca las horas: "))
T = float(input("Introduzca la tarifa por hora: "))

def calculo_salario():
    if H <= 40:
        s = T * H
        print(s)
    elif H > 40 :
        extras = H - 40
        s = (40 * T) + ((extras * 1.5)*10)
        print(s)

calculo_salario()






