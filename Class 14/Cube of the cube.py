def cube(x):
    return x ** 3

def divisible(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False
    
n = int(input("Enter the number"))

print(divisible(n))