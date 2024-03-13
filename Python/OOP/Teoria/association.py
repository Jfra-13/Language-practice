class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Curso:
    def __init__(self, nombre, profesor, estudiantes):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = estudiantes
        
pfr_juan = Profesor("Juanfra")

est_joaquin = Estudiante("Joaquin Llamoja")
est_bob = Estudiante("Bob Marley")

est_curso = [est_joaquin, est_bob]

curso_python = Curso("Python 3", pfr_juan, est_curso)

# Accediendo a la informacion

# print("Nombre del curso: ", curso_python.nombre)
# print("Profesor: ", curso_python.profesor.nombre)
# print("Estudiantes: ")

# for estudiantes in curso_python.estudiantes:
#     print("-", estudiantes.nombre)



#---------------------------------------------------------

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        
        
class Equipo:
    def __init__(self, nombre, entrenador, jugadores):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = jugadores
    
dt_roony = Entrenador("Roony")

player_10 = Jugador("Joaquin")
player_7 = Jugador("Kamila")
player_13 = Jugador("Lucho")

players = [player_10, player_7, player_13]

team_acartar = Equipo("Acatar", dt_roony, players)

# Accediendo a la informacion

print("Director tecnico: ", team_acartar.nombre)
print("Director tecnico: ", team_acartar.entrenador.nombre)
print("Delanteros: ")

for jugador in team_acartar.jugadores:
    print("-", jugador.nombre)
