'''class Upper:
    def __init__(self, word):
        if type(word) == str:
            print(word.upper())
        print("It is not string")


string_1 = Upper("Hola amigo")'''


"""class Perro:
    pass

color = Perro()
color.color_golden = "Brow"

print(color.color_golden)"""

'''class Perro:
    def __init__(self, color):
        self.color = color

color_golden = Perro("Brown")
print(color_golden.color)'''


'''class Punto:
    pass

id = Punto()
id.hexadecimal = '7FC03B' 

print(int(id.hexadecimal, 16))'''


"""class Punto:
    pass
punto = Punto()

punto.x = 10
punto.y = 5

def distancia(p):
    d = p.x - p.y
    return d

print(distancia(punto))
"""

'''class Rectangulo:
    def __init__(self, anchura, altura):
        self.anchura = anchura
        self.altura = altura

    def encontrarCentro(caja):
        p  = Punto()
        
        

class Punto:
    def __init__(self, esquina):
        self.esquina = esquina
'''



'''class Rectangulo:
    def __init__(self, anchura, altura):
        self.anchura = anchura
        self.altura = altura

    def getCentro(self):
        p = Punto()
        p.x = self.esquina.x + self.anchura / 2
        p.y = self.esquina.y + self.altura / 2
        return p

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

caja = Rectangulo(100, 200)
caja.esquina = Punto(0, 0)

centro = caja.getCentro()
print(caja)



num_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(1, num_alumnos + 1):
    num_notas = int(input(f"Ingrese la cantidad de notas para el alumno {i}: "))

    notas = []
    for j in range(1, num_notas + 1):
        nota = float(input(f"Ingrese la nota {j} para el alumno {i}: "))
        notas.append(nota)
        
    promedio = sum(notas) / len(notas)
    print(f"El promedio para el alumno {i} es: {promedio}")

'''



'''-------------------------------------------------------------------------------------------'''



class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '{a} menu available from {b} to {c}'.format(a=self.name, b=self.start_time, c=self.end_time)
    
    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price = total_price + self.items[item]
        return total_price


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return 'We are located in {a}'.format(a=self.address)
    
    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time < menu.end_time:
                available_menu.append(menu)
        return available_menu



brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
  }



early_bird_items = {
  'salumeria plate': 8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 1.50,
  'espresso': 3.00
}



dinner_items = {
  'crostini with eggplant caponata': 13.00,
  'caesar salad': 16.00,
  'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 2.00,
  'espresso': 3.00
}



kids_items = {
  'chicken nuggets': 6.50,
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
}


brunch = Menu('Brunch', brunch_items, 1100, 1600 )
early_bird = Menu("Early bird", early_bird_items, 1500, 1800)
dinner = Menu("Dinner", dinner_items, 1700, 2300)
kids = Menu("Kids", kids_items, 1100, 2100)

flagship_store = Franchise('1232 West End Road',[brunch, early_bird, dinner, kids])

#print(brunch.calculate_bill(['burger', 'home fries', 'orange juice']))

print(flagship_store.available_menus(1400))
