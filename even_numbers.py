#Iterates through a list of numbers and prints the even numbers.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
even_nums = []

for current_num in numbers:  #For loop iterates through each number in list.
    if current_num % 2 == 0:  #Checks to see if the current number is even.
        even_nums.append(current_num)  #Adds even numbers to list of numbers.
print(even_nums)
