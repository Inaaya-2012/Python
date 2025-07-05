# Counting the notes

n = int(input("Enter your amount"))

note100 = n//100
note50 = (n%100)//50
note10 = ((n%100)%50)//10
print("The number of 100 rupee note is",note100)
print("The number of 50 rupee note is",note50)
print("The number of 10 rupee note is",note10)