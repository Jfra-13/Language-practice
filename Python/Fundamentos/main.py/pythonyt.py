nombre = input('Cual es tu nombre?')
print ('Hola ' + nombre)

edad = int(input('Cuantos años tienes?'))
masDe12 = edad >=12
respuestaHijoDelDueño = input('Eres hijo del dueño?')
esHijoDelDueño = respuestaHijoDelDueño == 'Si'
puedePasar = masDe12 or esHijoDelDueño

if puedePasar:
    print('Usted puede ingresar')
else:
    print('Usted no puede ingresar')
