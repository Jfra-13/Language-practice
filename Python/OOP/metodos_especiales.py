class Persona:
    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre
        
    def __str__(self):
        return 'Persona (nombre = {}, edad = {})'.format(self.nombre, self.edad)
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre , nuevo_valor)
    
    
persona_1 = Persona('Juan', 21)
persona_2 = Persona('Kami', 18)

nueva_persona = persona_1 + persona_2
print(nueva_persona)




