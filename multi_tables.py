#Prints the multiplication tables from 1 to 10.

left_nums = 1
while left_nums <= 10:  #While loop to print the number of tables 1 - 10.
    right_nums = 1
    while right_nums <= 10:  #While loop to print the number of iterations per left column.
        print(f"{left_nums} X {right_nums} = {left_nums * right_nums}")
        right_nums += 1
    left_nums += 1
