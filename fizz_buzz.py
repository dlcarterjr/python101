### Takes a users input for a number and prints out from one to that number.
### Any number divisible by 3, it prints 'fizz'.
### Any number divisible by 5, it prints 'buzz'.
### Any number divisible by 3  AND 5, it prints 'fizzbuzz'.


# Get user input number (as integer) = "num".
num =  int(input("Enter number to count up to: "))
num_list = []

# Build list of numbers from 1 to the "num". num_list ### WRONG!  no list needed. Just check each number
for index in range(num):
    num_list.append([index])


#  This is what checks the number.

    #####CHECK MOST RESTRICTIVE CHECK FIRST (DIVISIBLE BY BOTH FACTORS)
    # If current_num divisible by 3, check to see if divisible by 5 also.
        # If also divisible by 5, print 'fizzbuzz'.
        # If not, append 'fizz' to print.
        #print current_num

    #If current_num divisible by 5, check to see if disible by 3, also.
        # If also divisible by 3, append 'fizzbuzz' to output_list.
        # If no, append 'buzz' to output_list.
        # If neither, go to next step.

    # Print current_num