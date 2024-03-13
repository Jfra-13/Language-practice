class Motor: 
    def arancar(self):
        print("El motor esta arrancando...")
        
class Auto:
    def __init__(self):
        self.motor = Motor()
        
    def conducir(self):
        self.motor.arancar()
        print("El auto esta en movimiento...")
        
# bmw = Auto()
# bmw.conducir()


# ----------------------------------------------------

class Bateria:
    def cargar(self):
        print("La bateria esta cargando...")
        
class Celular:
    def __init__(self):
        self.bateria = Bateria()
        
    def usar(self):
        self.bateria.cargar()
        print("El celular esta en uso...")
        
# xiaomi = Celular()
# xiaomi.usar()

# ----------------------------------------------------


class Pantalla:
    def proyectar(self):
        print("Se esta proyectando...")
        
class Cpu:
    def __init__(self):
        self.pantalla = Pantalla()
        
    def encendido(self):
        print("Se esta encendiendo....")
        self.pantalla.proyectar()
        
asus = Cpu()
asus.encendido()