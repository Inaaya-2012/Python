try:
    n = int(input("Enter the value: "))
    print("The value is",n)
except ValueError as ex:
    print("Error occured",ex)    