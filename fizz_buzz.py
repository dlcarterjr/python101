### Takes a users input for a number and prints out from one to that number.
### Any number divisible by 3, it prints 'fizz'.
### Any number divisible by 5, it prints 'buzz'.
### Any number divisible by 3  AND 5, it prints 'fizzbuzz'.


# Get user input number (as integer) = "num".
while True:

    try:       
        num =  int(input("\nEnter number to count up to: "))
        print("\n")
        break
    except:
        ValueError
        print("\nPlease enter a WHOLE number, only:\n")

## Loop iteration up to the entered number, starting with "1".
for count in range(1, num):

#  This is what checks the number.
    if count % 3 == 0 and count % 5 == 0:  ## CHECK MOST RESTRICTIVE CHECK FIRST (DIVISIBLE BY BOTH FACTORS)
        print("fizzbuzz")
    
    elif count % 3 == 0:  ## If num is divisible by 3, print "fizz".
        print("fizz")
    
    elif count % 5 == 0:  ## If num divisible by 5, print "buzz".
        print("buzz")  

    else:  ## Print current_num
        print(count)

print('\n')
    

    