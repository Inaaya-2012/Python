


n = int(input("Enter a number: "))


odd_numbers = [x for x in range(1, n) if x % 2 != 0]

print("List of odd numbers under", n, ":", odd_numbers)





fruits = ["apple", "banana", "cherry", "mango", "orange"]


updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits list:", fruits)
print("Updated fruits list:", updated_fruits)