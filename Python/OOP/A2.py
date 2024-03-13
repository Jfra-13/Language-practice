from A1 import GrupoAnimal

class GrilloFan(GrupoAnimal):
    puntos = 0
    def seis(self):
        self.puntos += 6
        #self.grupo()
        print(f'{self.name}, puntos: {self.puntos}')
        
# s = GrupoAnimal('Susan')
# s.grupo()

j = GrilloFan('Jim')
j.grupo()
j.seis()
print(dir(j))



