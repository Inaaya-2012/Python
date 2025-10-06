class BMW:
    def car_info(self):
        print("BMW: Luxury, Performance, and German Engineering.")

class Ferrari:
    def car_info(self):
        print("Ferrari: Speed, Style, and Italian Passion.")



def show_car_info(car):
    car.car_info()



bmw_car = BMW()
ferrari_car = Ferrari()


print("BMW Info:")
show_car_info(bmw_car)

print("\nFerrari Info:")
show_car_info(ferrari_car)



