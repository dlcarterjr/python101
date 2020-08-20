#sums a list of numbers.

numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]  #number list
count = 0
total = 0

#This while loop lterates through the list and sums the numbers.
while count < len(numbers):
    total += numbers[count]
    count += 1
print(total)
