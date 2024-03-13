# Con super() siempre se accede a la clase padre, por mas que reescribamos el metodo en una clase hija

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad  = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        return 'Me presento soy {}'.format(self.nombre)
        

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return 'mi habilidad son los {}'.format(self.habilidad)
    

class Empleado_artista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self ,nombre, edad, nacionalidad)
        Artista.__init__(self ,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola, soy {self.nombre} y {super().mostrar_habilidad()}. Trabajo en {self.empresa}')
        

mari = Empleado_artista('Maria', 18, 'Peruana', 'Malabares', 250, 'Emp. Fran')

herecia = issubclass(Empleado_artista, Artista)
print(herecia)
