import math


def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference


radius = float(input("Enter the radius of the circle: "))
circ = calculate_circumference(radius)

print(f"Circumference of the circle is: {circ:.2f}")
