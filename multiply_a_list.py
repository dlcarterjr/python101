#Iterates through a list of numbers and multiplies each by a factor.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
multi_factor = 3
multi_nums = []

for current_num in numbers:  #For loop iterates through each number in list.
    multi = current_num * multi_factor  #Multiplies number by factor
    multi_nums.append(multi)  #Adds multiplied number to new list of numbers.
print(multi_nums)