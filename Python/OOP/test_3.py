class Personaje():
    def __init__(self, name, force, speed ):
        self.name = name
        self.force = force
        self.speed = speed
        
    def __repr__(self):
        return f'{self.name} (fuerza: {self.force}, velocidad: {self.speed})'
        
    def __add__(self, otro_pj):
        new_name = self.name + '-' + otro_pj.name      
        new_force = round(((self.force + otro_pj.force)/2)**1.5)
        new_speed = round(((self.speed + otro_pj.speed)/2)**1.5)
        return Personaje(new_name, new_force, new_speed)
        
hero_1 = Personaje('Goku', 100, 100)
hero_2 = Personaje('Vegeta', 99, 99)
hero_3 = Personaje('Jiren', 130, 140)

new_hero = hero_1 + hero_2 + hero_3

print(new_hero)




"""class Animal():
    def __init__(self, nombre, tamaño, velocidad):
        self.nombre = nombre
        self.tamaño = tamaño
        self.velocidad = velocidad
        
    def __repr__(self):
        return '{} (Tamaño: {} cm, Velocidad: {} km/hr)'.format(self.nombre, self.tamaño, self.velocidad)


animal_1 = Animal('Chita', 1.20, 150)"""
