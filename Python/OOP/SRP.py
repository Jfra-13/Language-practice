class Auto:
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion = self.posicion + distancia
            self.tanque.usar_combustible(distancia/2)
            print('Te moviste exitosamente')
            
        else:
            print('No hay suficiente combustible.')
            
    def obtener_posicion(self):
        return self.posicion
            
            
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
       
    def agregar_combustible(self, cantidad):
        self.combustible = self.combustible + cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible = self.combustible - cantidad
       
galon = TanqueDeCombustible()
       
Autito = Auto(galon)
print(Autito.obtener_posicion())
print(Autito.mover(10))