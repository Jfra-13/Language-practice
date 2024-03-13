# Un atributo privado lo declaras con un '_'

"""class Miclase:
    def __init__(self):
        self.__atributo_privado = 'Valor'
        self._atributo_privado = 'Nombre_valor'
        self.atributo = 'Seccion'

    def _hablar(self) -> object:
        print('Hola como estas')

object1 = Miclase()
object1._hablar()"""


"""class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

juan = Persona('Juanfra', 20)

nombre = juan.get_nombre()
print(nombre)

juan.set_nombre('Juan Francisco')

nombre = juan.get_nombre()
print(nombre)"""

#--------------------------------------------------------

"""class Vehiculo:
    def __init__(self,propietario, modelo, marca, placa, soat):
        self.propietario = propietario
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.__soat = soat


    def get_soat(self):
        return self.__soat

    def validacion_soat(self):
        if self.__soat == 'Si':
            return True
        else:
            return False


class BMW(Vehiculo):
    def __init__(self, propietario, modelo, marca, placa, soat):
        super().__init__(propietario, modelo, marca, placa, soat)

    



jf_auto = BMW('Juan', 'M4', 'BMW', 'BXC425', 'Si')


print(jf_auto.validacion_soat())"""















