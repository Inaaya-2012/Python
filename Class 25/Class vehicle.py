class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
    
car = vehicle("150km/h","16km/litre")    
print("The maxspeed of the car is",car.maxspeed)
print("The mileage of the car is",car.mileage)