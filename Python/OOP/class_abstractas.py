from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print('Hola me llamo: {} y tengo {}'.format(self.nombre, self.edad))
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
   
    def hacer_actividad(self):
        print('Estoy estudiando: {}'.format(self.actividad))   
        

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print('Actualmente en el rubro de: {}'.format(self.actividad))



juan = Estudiante('Juan', 21, 'Masculino', 'Programador')
jonathan = Trabajador('Jonathan', 21, 'Masculino', 'Conductor')


juan.presentarse()
juan.hacer_actividad()

jonathan.presentarse()
jonathan.hacer_actividad()

