class Cat:
    life = 100
    cat_damage = 25
    
    def __init__(self, name, age, velocity):
        self.name = name
        self.age = age
        self.velocity = velocity
        
    def __repr__(self):
        return f'My cat {self.name} is {self.age} years old.'
    
    def takingDamage(self, dmgRecieve):
        self.life -= dmgRecieve
        

miles = Cat("Miles", 3, 40)
bianca = Cat("Bianca", 2, 35)

miles.age = 5
print(miles.age)

miles.life = 25
print(miles.life)

miles.takingDamage(20)
print(miles.life) 


