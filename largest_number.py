#Sorts through a list of numbers and prints out the largest.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
count = 0
big_num = 0

#This for loop itertates through the list and checks if current big_num is higher than the current number.
for ck_num in numbers:
    if ck_num >= big_num:   #If current number if bigger than biggest found number, then
        big_num = ck_num    # Replaces big_num with current number
print(big_num)