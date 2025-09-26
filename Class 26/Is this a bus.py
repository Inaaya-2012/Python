class vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
   
class Bus(vehicle):
    pass

bus1 = Bus("Volvo",'130 km','18km/l')

print("The bus details are: ",bus1.name,bus1.max_speed,bus1.mileage)
