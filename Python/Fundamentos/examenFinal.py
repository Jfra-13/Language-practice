notaUno = int(input("Ingrese calificacion 1: "))
notaDos = int(input("Ingrese calificacion 2: "))

prom = (notaUno + notaDos)/2

if prom >= 9:
    print("A\nAPROBADO")
elif prom >=7.5:
    print("B\nAPROBADO")
elif prom >=6:
    print("C\nAPROBADO")
elif prom >=4:
    print("D\nDESAPROBADO")
elif prom >=0:
    print("E\nDESAPROBADO")

