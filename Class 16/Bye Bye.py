valid = False
while not valid:
    try:
        n = int(input("Enter the value: "))
        while n % 2 == 0:
            print("Bye")
        print("The given value is odd")
        valid = True 
    except:
        print("Invalid input")       