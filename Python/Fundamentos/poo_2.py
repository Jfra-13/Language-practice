'''Para usar o crear objetos es necesario hacer una clase y agregarle atributos para
   de ahi darle forma al objeto que queremos elaborar'''

class Alumnos:
    def __init__(self, nombre, apellidos, curso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.curso = curso
        self.materias = []

'''Podemos agregar listas en los atributos'''
alumno01 = Alumnos('Lucia', 'Granados Cisneros', '2')
alumno01.materias.append('Matematica')

alumno02 = Alumnos('Javier', 'Morales Garcia', '4')
alumno02.materias.append('Ingles')
alumno02.materias.append('Musica')


print(alumno01.materias, alumno02.materias)

alumno02.materias.remove("Ingles")
print(alumno02.materias)