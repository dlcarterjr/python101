#Iterates through a list of numbers and prints the positive numbers to a new list, which it prints.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
positive_nums = []

for current_num in numbers:  #For loop iterates through each number in list.
    if current_num > 0:  #Checks to see if number is positive
        positive_nums.append(current_num)  #Adds positive numbers to list of numbers.
print(positive_nums)