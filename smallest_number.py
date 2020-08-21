#Sorts though a list of numbers and prints the smallest.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
count = 0
small_num = 0

#This for loop itertates through the list and checks if current small_num is lower than the current number.
for ck_num in numbers:
    if ck_num <= small_num:   #If current number if smaller than current small found number, then
        small_num = ck_num    # Replaces small_num with current number
print(small_num)