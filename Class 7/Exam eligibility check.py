# Exam eligibility check

mc = input("Do you have a medical cause? (y/n)")

if mc.lower() == 'y':
    print("You are eligible")
elif mc.lower() == 'n':
    att = int(input("Enter your attendence"))    
    if att > 75:
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("Invalid input")            