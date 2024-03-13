h = int(input("Introduzca las horas: "))
t = float(input("Introduzca la Tarifa por hora: "))

if h <= 40 :
    s = t * h 
    print(s)
  
elif h > 40 :
  extras = h - 40
  s = (40 * t) + ((extras * 1.5)*10)
print(s)
