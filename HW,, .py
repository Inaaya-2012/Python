
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


square_values = []
for num in range(start, end + 1):
    square = num ** 2
    square_values.append(square)


even_squares = []
odd_squares = []

for square in square_values:
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)


print("\nAll square values:", square_values)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
