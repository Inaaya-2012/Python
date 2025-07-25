n = int(input("Enter the number"))
num = n
sum = 0
while num != 0:
    rem = num%10
    sum =  sum + rem ** 3
    num = num // 10

if sum == n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")        