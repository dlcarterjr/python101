#Takes user input of a number with exception handling of TypeError
while True:
    try:
        day = int(input("Day (0-6) ? "))
        break
    except ValueError:
        print("Please enter a number.")

#Checks user's number against the day of the week and outputs corresponding day.
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Saturday")
