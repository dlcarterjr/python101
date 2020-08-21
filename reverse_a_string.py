#Prints a list of numbers in reverse order.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
pos_num = len(numbers)-1  #  Sets index of the last number in the list.
reverse_list = []
for position in numbers:  # For loop appends starts with last number and
    reverse_list.append(numbers[pos_num])  #  adds each to a list in reverse order.
    pos_num -= 1  #  Decrements index number.
print(reverse_list)