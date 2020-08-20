coins = 0
print(f"You have {coins} coins.")
answer = input("Do you want another? ")
answer = answer.lower()
while answer != "no":
    coins += 1
    print(f"You have {coins} coins.")
    answer = input("Do you want another? ")
    answer = answer.lower()
print("Bye")
