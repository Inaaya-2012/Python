ch = input("1.Bike\n2.Car\nEnter your choice")
if ch == "1":
    ch1 = input("1.Harley Davidson\n2.Yamaha\nEnter your choice")
    if ch1 == "1":
        print("You have selected Harley Davidson")
    elif ch1 == "2":
        print("You have selected Yamaha")
    else:
        print("Invalid choice")


elif ch == "2":
    ch1 = input("1.KIA\n2.Mahindra\nEnter you choice")
    if ch1 == "1":
        print("You have selected KIA")
    elif ch1 == "2":
        print("You have selected Mahindra")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")        
