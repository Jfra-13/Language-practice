class Users:
    
    users_type = "Free"
    publicity = True

    '''Agregamos *args para agregar mas agumentos aparte de los establecidos''' 
    def __init__(self, nid, alias,name,lastname,*args):
        self.nid = nid
        self.alias = alias
        self.name = name
        self.lastname = lastname
        self.args = args

        
user01 = Users("001","Peque","Paula","Bravo Rojas","Hola","jeje")
print(user01.args)       
        
class PremiumUsers:
    
    users_type = "Premium"
    publicity = False
    
    def __init__(self,nid,alias,name,lastname):
        self.nid = nid
        self.alias = alias
        self.name = name
        self.lastname = lastname
        
print(PremiumUsers.users_type)
        
'''Metodo y funcion - ambos se escriben con def
    el metodo pertenece a una clase y la funcion no
    pero ambos funcionan igual'''
    
'''un def escrita fuera de una clase es una funcion
    un def esta escrito dentro de una clase es metodo'''