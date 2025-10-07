
char = input("Enter a single character: ")


if len(char) != 1:
    print("Please enter only one character.")

elif char.isalpha():
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is NOT an alphabet.")
