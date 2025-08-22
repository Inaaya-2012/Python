ch = ['rock','paper','scissors']
import random
while True:
    comp = random.choice(ch)
    user = input("Enter rock,paper or scissors").lower()
    if user == comp:
        print("It is a tie")
    elif(user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'scissors' and comp == 'paper'):
        print("User wins")
        print(comp)
    else:
        print("Computer wins")
        print(comp)

    choice = input("Do you want to play again (y/n) : ") 
    if choice.lower() == 'n':
        break                  