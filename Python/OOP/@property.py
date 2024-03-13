# class Persona:
#     def __init__(self, nombre, edad):
#         self.__nombre = nombre
#         self._edad = edad
        
#     @property
#     def nombre(self):
#         return self.__nombre
    
#     @nombre.setter
#     def nombre (self,new_nombre):
#         self.__nombre = new_nombre
    
#     @nombre.deleter
#     def nombre(self):
#         del self.__nombre
    
#     # def set_nombre(self, new_nombre):
#     #     self.__nombre = new_nombre
        
        
# persona_1 = Persona('Juan', 21)

# print(persona_1.nombre)

# persona_1.nombre = 'Marco'

# name = persona_1.nombre

# print(name)
 


# del persona_1.nombre
# nom_persona1 = persona_1.nombre
# print(nom_persona1)


"""------------------------------------------------------"""

class Vehiculo:
    def __init__(self, placa, propietario, color):
        self.__placa = placa
        self._propietario = propietario
        self.color = color
        
     
    def movimiento_auto(self, encendido):
        def avanzar():
            if encendido:
                encendido(self)
                print('El auto {} esta avazando'.format(self.placa))               
            else:
                print('El vehiculo necesita encender.')
        return avanzar
    
    
    def encender(self):
        encendido = False
        movimiento = self.movimiento_auto(self._encender)
        movimiento()
        
    
    def _encender(self, vehiculo):
        print('El auto {} de {} encendio'.format(vehiculo.placa, vehiculo._propietario))
        
    
    
    @property   
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, new_placa):
        self.__placa = new_placa
        
    @placa.deleter
    def placa(self):
        del self.__placa
    
        
auto_Juan  = Vehiculo('BXC425', 'Llamoja', 'Blanco')  

auto_Juan.encender()

























