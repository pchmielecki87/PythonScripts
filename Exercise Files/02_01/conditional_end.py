
price = input("What's the price? $")
price = float(price)

if price==0:
    print("You didn't enter a price")
elif price<0:
    print("Invalid price")
elif price<10:
    print("Discounted Price", "$", price*0.9)
else:
    print("Price", "$", price)

print("End of program")
