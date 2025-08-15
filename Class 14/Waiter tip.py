def waiter_tip(amt,p):
    tip = amt * (p/100)
    tamt = amt + tip
    print("The amount = ",amt)
    print("The tip ",round(tip,2))
    print("The total amount ",tamt)

waiter_tip(500,2)