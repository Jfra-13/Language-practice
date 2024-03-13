"""class R1000:
    def arranque(self):
        print('Moto // 30 km/h')

class M4_cls:
    def arranque(self):
        print('Carro // 38 km/h')



listVehiculos = [ R1000(), M4_cls() ]

def regresiva(lstV):
    for vehiculo in lstV:
        vehiculo.arranque()

regresiva(listVehiculos)"""

# ----------------------------------------

car_tu = ('BMW', 'Audi', 'Mercedes', 'Toyota')
car_lst = ['BMW', 'Audi', 'Mercedes', 'Toyota']
car_dct = {
    'BMW': 'car 1',
    'Audi': 'car 2',
    'Mercedes': 'car 3',
    'Toyota': 'car 4'
}
car_1, car_2, car_3, car_4 = car_tu


"""while True:
    name = input('Ingresa tu nombre: ')
    if name:
        break"""

def param_arbitriarios(param_fijo, *arbitrario):
    print(param_fijo)
    for argumentos in arbitrario:
        print(argumentos)

# param_arbitriarios('Fixed', 'arbitrario1', 'arbitrario2', 'arbitrario3')

"""def arbitrarios_dobles(param_fijo, **kwargs):
    for i in param_fijo:
        print(i)
    for clave in kwargs:
        print(kwargs[clave])"""

# arbitrarios_dobles('Fixed', clave='valor uno', clave2='valor dos', )

"""def calcular_importe_lista(importe, descuento):
    return importe - (importe * descuento/100)

datos = [1500,10]
print(calcular_importe_lista(*datos))


def calcular_importe_dct(importe, descuento):
    return importe - (importe * descuento / 100)

data = {'descuento': 10, 'importe': 1500}
print(calcular_importe_dct(**data))"""


"""def funcion(nombre):
    return nombre
def llamada_retorno(func=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]('Laura')
        else:
            return 'Funcion no encontrada'

print(llamada_retorno("funcion"))"""

"""head = 'Class Python'
print(head.rjust(50,'='))"""

"""number = 2316
print(str(number).zfill(5))"""

"""kmi = "Good morning".capitalize()
print(kmi.count('d'))"""

"""kami = 'Ay mira como hablas eres muy cochino'.capitalize()
print(kami.find('muy'))
print(kami.find('muy', 1, 27))"""


"""joaquin = 'Mira como le hice el daño a este jugador'.capitalize()
print(joaquin)
print(joaquin.startswith('mira'))
print(joaquin.endswith('jugador'))"""

psswr = '72200571@Jf'
def contraseña(contra):
    if contra == psswr:
        print('Correcta')
    else:
        print('Incorrecto')
        
contraseña(psswr)


while True:
    input('')