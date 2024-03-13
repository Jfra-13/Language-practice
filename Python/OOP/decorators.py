"""def decorador(funcion):
    def funcion_modificada():
        print('Voy primero')
        funcion()
        print('Voy tercero')
    return funcion_modificada

def funcion():
    print('Voy segundo')
    
    
empezar = decorador(funcion)
empezar()"""

# space_and_tab = False
# bloq_mayus = True
# tap_w = True

# if tap_w == True:
#     def correr(sprint, desliz):
#         def activar_extras():
#             print('Corriendo...')
#             sprint()
#             desliz()
#             print('Usted se canso')
#         return activar_extras
# else:
#     print('Caminando...')
  
        
# def sprintar():
#     if space_and_tab == True:
#         print('Sprintando...')
#     else:
#         pass
    
# def deslizarse():
#     if bloq_mayus == True: 
#         print('Deslizandose...')
#     else:
#         pass
    

# desplazarse = correr(sprintar, deslizarse)
# desplazarse()


'''def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la funcion.')
        funcion()
    return funcion_modificada

@decorador
def saludo():
    print('Hola como andas')

saludo( )'''





def saltar(impulso):
    def antes_saltar():
        impulso()
        print('Saltar')
    return antes_saltar
    

def correr_saltar(funcion):
    def agarrar_vuelo():
        print('Correr')
        funcion()
    return agarrar_vuelo

@saltar
def tomar_impulso():
    print('Impulso')

saltoLargo = correr_saltar(tomar_impulso)
saltoLargo()


