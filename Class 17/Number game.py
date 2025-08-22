import random
cguess = random.randint(1,10)
while True:
    user = int(input("Enter the number"))
    if user == cguess:
       print("You guessed it right")
       break
    else:
        print("Try again")

    