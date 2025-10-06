def shutdown():
    user_input = input("Do you want to shut down the system? (yes/no): ").lower()

    if user_input == "yes":
        print("Shutting down the system...")
        
    elif user_input == "no":
        print("Shutdown cancelled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


shutdown()
