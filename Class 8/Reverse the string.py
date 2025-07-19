str1 = input("Enter the string")
rev = ""
for i in str1:
    rev =  i + rev
print(f"The reverse of the {str1} is {rev}")    