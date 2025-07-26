l = int(input("Enter the lower limit "))
u = int(input("Enter the upper limit "))
print(f"The prime numbers between {l} and {u} ")
for i in range(l,u+1):
    for j in range (2,l):
        if i % j == 0:
            break
    else:
        print(i)        
