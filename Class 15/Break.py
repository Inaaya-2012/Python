str1 = input("Enter the string: ")
for i in str1:
    if i.lower() == "a":
        print("a is present in the given string")
        break
else:
    print("a is not present in the given string")    