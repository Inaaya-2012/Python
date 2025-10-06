# Parent class
class Vehicle:
    def __init__(self, name, capacity):
        self.name = name          
        self.capacity = capacity  

    def get_info(self):
        print("Vehicle Name:", self.name)
        print("Seating Capacity:", self.capacity)



class Bus(Vehicle):
    def calculate_fare(self):
        fare_per_person = 10  
        total_fare = self.capacity * fare_per_person
        return total_fare





my_bus = Bus("City Bus", 50)


my_bus.get_info()


fare = my_bus.calculate_fare()
print("Total Bus Fare: $", fare)

