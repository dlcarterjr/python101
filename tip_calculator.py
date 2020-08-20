bill = float(input("Total bill amount? "))
service = input("Level of service? ")
if service == "good":
    tip = bill * .2
    print(f"Tip amount: ${tip:.2f}")
elif service == "fair":
    tip = bill * .15
    print(f"Tip amount: ${tip:.2f}")
else:
    tip = bill * .1
    print(f"Tip amount: ${tip:.2f}")
total = bill + tip
print(f"Total amount: ${total:.2f}")