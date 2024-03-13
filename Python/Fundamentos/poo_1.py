'''def -> reservada para crear funciones'''
'''Los atributos son las propiedades de un objeto'''
'''Nombrar de manera adecuada cada atributo para recordar '''
'''-------------------------------------------------------------------'''
''' METODO __init__ y self'''
'''self hace referencia a cualquier nombre de objeto que creemos,
    la palabra self puede cambiar dependiendo de metodo donde estes para 
    evitar confusiones'''
    
'''Se pueden crear nuevos atributos desde fuera del contructor'''


class NinjaPrincipal:
    def __init__(self,HP,resistencia, xp, vidas):
        self.HP = HP
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas
    
    def game_over(self):
        print('Game Over')
        
'''Creacion del ninja principal y enemigo con uso de init y self''' 
ninja = NinjaPrincipal(100,50,1,3)  
ninja.salto = True
ninjaEnemigo = NinjaPrincipal(25,10,1,1) 
print(ninja.salto)

       
'''ninja = NinjaPrincipal()
print(ninja.HP)

ninja_enemigo = NinjaPrincipal()
ninja_enemigo.HP = 25
ninja_enemigo.resistencia = 10
ninja_enemigo.vidas = 1

print(ninja_enemigo.HP, ninja_enemigo.resistencia, ninja_enemigo.vidas)'''