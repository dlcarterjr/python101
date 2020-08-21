#Prints a triangle with the specified levels using the "*" character.


levels = int(input("How many levels for triangle? "))  #Get the number of levels from user.
row_count = 1
star_count = 1
space_count = levels - 1  #Calculates the number of spaces before the "*"s.

#This while loop builds each row and prints the proper spaces and "*"s.
while row_count <= levels:
    print((" " * space_count) + ("*" * star_count))
    row_count += 1
    star_count += 2  #Stars go up by 2 for each row.
    space_count -= 1
