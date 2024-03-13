class Hora:
    def __init__(self, hour, minuts, second):
        self.hour = hour
        self.minuts = minuts
        self.second = second
    
    def show_time(self):
        print(f'{self.hour}:{self.minuts}:{self.second}')

    def sumahoras(self, t1, t2):
        suma = Hora(0,0,0)
        suma.hour = t1.hour + t2.hour
        suma.minuts = t1.minuts + t2.minuts
        suma.second = t1.second + t2.second
        
        if suma.second >= 60:
            suma.second = suma.second - 60
            suma.minuts = suma.minuts + 1
            
        if suma.minuts >= 60:
            suma.second = suma.second - 60
            suma.hour = suma.hour + 1
        
        return suma
    
hora1 = Hora(23,13,16)
hora2 = Hora(2,10,25)

finalhour = hora1.sumahoras(hora1,hora2)
finalhour.show_time()



