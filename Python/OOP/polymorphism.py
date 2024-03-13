# Dar un mensaje a nuchos objetos y den diferentes resultados.
class Perro:
    def sonido(self):
        print('Guau')
        
        
class Gato:
    def sonido(self):
        print('Miau')
        
class Vaca:
    def sonido(self):
        print('Muuu')
        
def hacersonido(animal_lst):
    for animal in animal_lst:
        animal.sonido()

kody = Perro()
# hacersonido(Gato())
# hacersonido(kody)

lista = [Perro(), Gato(), Vaca()]
#hacersonido(lista)

# ----------------------------------------------

class Vehiculo:
    def __init__(self, model, year, color, placa):
        n_rueda = 4
        self.model = model
        self.year = year
        self.color = color
        self.placa = placa

    def avanzar(self):
        pass

    def frenar(self):
        pass



class Moto(Vehiculo):
    def __init__(self, model, year, color, placa, aro):
        Vehiculo.__init__(self, model, year, color, placa)
        self.aro = aro

    def showmodel(self):
        pass

bmw_R1000 = Moto('R1000', 2023, 'Red', 'BQP5026', True)
bmw_m4 = Vehiculo('M4 cls', 2024, 'White', 'BMX352')











