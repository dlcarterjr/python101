#Iterates through a list of numbers and prints the positive numbers.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list

for current_num in numbers:  #For loop iterates through each number in list.
    if current_num > 0:  #Checks to see if number is positive, then
        print(current_num)  #Prints the positive number.