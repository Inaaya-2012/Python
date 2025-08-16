try:
    n1,n2 =  eval(input("Enter the numbers seperated by commas"))
    r = n1/n2
    print("The answer is",r)
except ZeroDivisionError:
    print("The number is divided by zero")
except SyntaxError:
    print("Type the number seperated by comma as n1,n2")
except:
    print("Error occured")
else:
    print("No exception")
finally:
    print("Whatever happens the progress gets executed")                    