class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Departamento:
    def __init__(self, nombre, trabajadores):
        self.nombre = nombre
        self.trabajadores = trabajadores

juan_Ll = Trabajador("Juanfra Llamoja Javier")   
kam_Cs = Trabajador("Maria Kamila Casas")
joa_Ll = Trabajador("Joaquin Llamoja Javier")
     
trabajadores_Molina = [juan_Ll, kam_Cs, joa_Ll]

casa_Molinera = Departamento("Casa Hacienda La molina", trabajadores_Molina)

# Accediendo a los valores

print("Ubicacion:", casa_Molinera.nombre)
print("Trabajadores:")      
for empleado in casa_Molinera.trabajadores:
    print("-", empleado.nombre)
