from math import sin # inport the trigonometric function
from math import cos # inport the trigonometric function
from math import tan # inport the trigonometric function

def isValidInput(a,b,n,ft): # define a function to point out the type of error
    result = True # the default value is true
    if b <= a: # the type of error
        print('invalid range') # point out the type of error
        result = False # change the value to false
    if ft < 1 or ft > 3: # the type of error
        print('invalid function') # point out the type of error
        result = False # change the value to false
    if n < 1: # the type of error
        print('invalid sub-interval') # point out the type of error
        result = False # change the value to false
    return result # return result 



a = input('Enter interval a:') # Enter interval a
b = input('Enter interval b:') # Enter interval b
n = input('Enter the number of sub-intervals n:') # Enter the number of sub-intervals n
print('Select the type of function from 1 for sin, 2 for tan and 3 for cos.') # Give the guide to the user
ft = input(' Enter 1 for sin, 2 for tan and 3 for cos:') # Select the type of function from 1(sin), 2(tan) and 3(cos)
    
try: # to prevent possible error
    a = float(a) # change the data type
    b = float(b) # change the data type
    n = int(n) # change the data type
    ft = int(ft) # change the data type
    temp = 0 # set the default value
    
    if isValidInput(a,b,n,ft): # start to calculate
        d = ((b-a)/n) # intermidiate variable

        func_list = { # set a library to use the trigonometric function
           1: sin, # 1 represents sin
           2: tan, # 2 represents tan
           3: cos, # 3 represents cos
        } # the end of the library
        tri_func = func_list[ft] # use the library
        
        for i in range(1,n+1): # set a loop for summary
            temp += d*tri_func((a + d*(i - 1/2))) # get the answer
        print(temp) # print the answer


        
except: # find the possible error
    print('Wrong') # point out that the program can't execute 


