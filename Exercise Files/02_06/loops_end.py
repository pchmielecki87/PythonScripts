total = 0
while input("Continue? (Y/n) ")=="Y":
    qty = int(input("Enter quantity: "))
    if qty < 0: 
        break
    total += qty
else:
    # after the loop ended without a break
    print("Final quantity: ", total)