# Herencia clase que hereda propiedades de la clase padre

# Clase - Padre

# class Animal:
#     food = 50 # 0 hambriento, 100 no lo esta
    
#     def __init__(self, name, age, velocity, acuatic):
#         self.name = name
#         self.age = age
#         self.velocity = velocity
#         self.acuatic = acuatic
        
#     def isHungry (self):
#         return self.food < 50
    
#     def going_hungry(self, food):
#         self.food -= food
    
#     def eat (self):
#         if self.isHungry():
#             self.food = self.food + 10
            
#     def defend(self):
#         print(f"{self.name} se esta defendiendo de su enemigo")
        
# # Clase - Hijo

# class Mammal(Animal):
#     def __init__(self, name, age, velocity, acuatic, milk):
#        super().__init__(name, age, velocity, acuatic)
#        self.milk = milk
       
#     def lactation(self):
#         print(f"Tiene que amamantar {self.milk} litros")


# # Main
# vaca = Mammal("Lola",1, 5, True, 15)

# vaca.lactation()
# vaca.defend()
# vaca.going_hungry(25)

#-----------------------------------------------------


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print('Hola solicito un puesto.')
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        print('Gracias por aceptarme.')
            
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
    
    def hablar(self):
        print('Solicito practicas pre-profesionales')


robert = Estudiante('Roberto', 24, 'Peruano', 'Programador',100000)
robert.hablar()
    