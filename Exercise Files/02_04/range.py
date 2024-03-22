total = 0
for number in range(4):
    price = input("Price for item " + 
                  str(number) + ": ")
    total += float(price)

print("The total to pay is", total)
