import random

def adivin_el_numero(x):
  print("Bienvenido al juego\nTu meta es adivinar el numero generado por la computadora")
  
  num_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y X

  prediccion = 0

  while prediccion != num_aleatorio:
    prediccion = int(input(f"Adivina un numero entre 1 y {x}:"))
    
    if prediccion < num_aleatorio:
      print("Intenta una vez mas. Numero ingresado es menor")
    elif prediccion > num_aleatorio:
      print("Intenta una vez mas. Numero ingresado es mayor")
  
  print(f"Felicitacion adivinaste el numero {num_aleatorio} correctamente")

adivin_el_numero(10)
