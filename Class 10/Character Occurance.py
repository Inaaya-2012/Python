str1 = input("Enter a phrase")
ch = input("Enter a character")

count = 0

for i in str1:
    if i == ch:
        count += 1
print(f"The no. of occurance of{ch} in{str1} is {count}")        