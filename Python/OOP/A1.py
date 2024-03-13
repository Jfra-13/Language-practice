class GrupoAnimal:
    x = 0
    name = ''
    def __init__(self, nom):
        self.name = nom
        print(f'{self.name}, construido')
        
    
    def grupo(self):
        self.x += 1
        print(f"{self.name}, recuento grupal, {self.x}")
        
# s = GrupoAnimal("Sally")
# j = GrupoAnimal("Jimmy")

# s.grupo()
# j.grupo()
# s.grupo()

        


