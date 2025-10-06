
age_input = input("Enter your age: ")


if age_input.isdigit():
    age = int(age_input)

    
    if age <= 0 or age > 120:
        print("Invalid age entered. Please enter a valid age between 1 and 120.")
    else:
        print("Valid age entered:", age)

      
        if age % 2 == 0:
            print("The age is Even.")
        else:
            print("The age is Odd.")

else:
    print("Invalid input. Please enter a numeric value.")
