class Estudiante:
    def __init__(self, nombre, apellido, edad, grado):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} {self.apellido} esta estudiando.')
        

nombre = input('Nombre: ')
apellido = input('Apellido: ')
edad = input('Edad: ')
grado = input('Grado: ')

   
estudiante_1 = Estudiante(nombre, apellido, edad, grado)


estudiar = input()
if (estudiar.lower() == 'estudiar'):
    estudiante_1.estudiar()