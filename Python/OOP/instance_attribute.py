class Celular:
    def __init__(self, modelo, marca, camara):
        self.modelo = modelo
        self.marca = marca
        self.camara = camara
        
    def llamar(self):
        print(f'Ustede esta llamando desde un {self.modelo}')
    
    def cortar(self):
        print(f'Corto la llamada de su {self.marca}')  
        
celular_1 = Celular('S23','Samsung', 48)
celular_2 = Celular('15 Pro', 'Iphone', 48) 

celular_2.llamar()
