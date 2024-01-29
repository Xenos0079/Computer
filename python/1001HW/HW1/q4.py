m = input('Enter a positve interger') # let the user enter the interger
m = eval(m) # change the data type of m
n = 1 # set the start number as 1

print('m      m+1     m**(m+1)') # print the title row of the graph
try: # prevent that the input of m is not a valid number
    while m >= 1 and m > n: # set the loop
        a = str(n) # set each element of the row
        b = str(n + 1) # set each element of the row
        c = str(n ** (n +1 ))  # set each element of the row
        n += 1 # set each element of the row
        print(a.ljust(6), b.ljust(7), c) # print the row. I asked my roommate and know that .ljust can be used to adjust the space between the numbers
except: # for the invalid input:
    print('Invalid input') # tell the user that the input is invalid