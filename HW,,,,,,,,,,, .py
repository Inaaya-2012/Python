
number = input("Enter a number: ")

if number.startswith('-'):
    number = number[1:]


digit_count = len(number)


print("The number has", digit_count, "digit(s).")
