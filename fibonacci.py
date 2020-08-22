####  Asks user for a number input and prints out the Fibonacci sequence up to that sequence number.



##  Get the input number from the user = num.
while True:
    try:
        num = int(input("\nEnter Fibonacci sequence number to reach: "))
        break
    except ValueError:
        print('\nPlease enter WHOLE numbers, only.')

##  Declare beginning variables (a and b) to beginning values (a = 1, b = 1, c = 0).
a = 1
b = 1
c = 1
counter = 1
## First print a and b (prints 1 and 1 as first numbers of Fib sequence).
print(f'\n{a}\n{b}')
##  Set loop to run as long as counter <= num.
while counter < num - 1:  ##"-1" accouts for the first two "1" values.
    c = a + b  ## formula is c = a + b
    print(c)  ## Print 
    a = b  ## a is then assigned b
    b = c  ## b is then assigned c
    counter += 1
print('\n')
    
        
        
        
