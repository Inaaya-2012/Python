import math  
number = float(input("Enter a number: "))
if number >= 0:
    
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")
else:
    print("Square root of a negative number is not a real number.")
