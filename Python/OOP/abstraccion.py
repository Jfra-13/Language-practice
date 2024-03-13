class Vehiculo:
    def __init__(self):
        self._estado = 'Apagado'
        
    def encendido(self):
        self._estado = 'Encendido'
        print('El auto esta encendido')
        
    def conducir(self):
        if self._estado == 'Apagado':
            self.encendido()
        print('Conduciendo el auto')
        
bmw = Vehiculo()
bmw.conducir()
        