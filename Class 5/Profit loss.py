actual_cost = float(input("Please enter the actual price"))
sale_amount = float(input("Please enter the sales amount"))

if (sale_amount >actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}".format(amount))
else:
    amount = actual_cost - sale_amount
    print("Loss amount = {0}".format(amount))
    print("No Profit!!!!!!") 
