
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid by the customer: "))

due_amount = total_bill - amount_paid


if due_amount > 0:
    print(f"Amount still due: ₹{due_amount:.2f}")
elif due_amount < 0:
    print(f"Extra amount paid: ₹{abs(due_amount):.2f} (Change to be returned)")
else:
    print("The bill is fully paid. No amount is due.")
