n = input("Enter the number ")

str1 = str(n)
l = len(str1)

if l % 2 == 0:
    mid = l//2 -1
else:
    mid = l//2

product = int(str1[mid]) * int(str1[mid+1])
print("The mid product is ",product)        