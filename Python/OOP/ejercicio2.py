# class Persona:
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def __str__(self):
#         return 'Datos estudiante {}'.format(self.nombre)
        
#     def datashow(self):
#         print('- {a}: {b}'.format(a=self.nombre, b=self.edad))


# class Estudiante(Persona):
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
    
#     def showmssg(self):
#         print('- {a}: {b}'.format(a=self.nombre, b=self.grado))
        
# estudiante_1 = Estudiante('Juan', 21, 'Pregrado - 08')

# print(estudiante_1)
# estudiante_1.datashow()
# estudiante_1.showmssg()




# class Animal:
#     def comer(self):
#         print('El animal esta comiendo.')
        
# class Ave(Animal):
#     def volar(self):
#         print('El animal esta volando.')
        
# class Mamifero(Animal):
#     def amamantar(self):
#         print('El animal esta amamantando')
        
# class Murcielago(Mamifero, Ave):
#     pass


# ave = Ave()

# Murcielago.comer
# Murcielago.volar
