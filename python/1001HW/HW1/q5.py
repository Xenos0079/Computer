import math # have to use log to simplify the program

def is_prime(target): # define a new function to judge whether a given munber is a prime number
    sr = int(target ** 0.5)+1 # get a possible set of factors
    for i in range(2,sr): # set a loop
        if target%i == 0: # if the target can be divisible
            return False # the target won't be a prime number
    return True # if the loop can't satisfy the false request ,then the target is a prime number

N = input('Enter a number:') # let the user enter the number
count = 0 # prepare the count place for each line

try: # In case that the input is invalid
    N = int(N) # change the data type of N
    
    if N > 0:  # judge that N is positive
        len_digit = int(math.log10(N))+1 # find out the length of the digit
        for i in range(2,N): # judge that whether i is a prime number
            if is_prime(i): # use the defined function
                count += 1 # add a count for the place of line
                if count%8 == 0: # We have to start a new line
                    print('%*d'%(len_digit,i),'%s'%' ') # start a new line
                else: # just keep print the number
                    print('%*d'%(len_digit,i),'%s'%' ',end = '') # print the number
                
    else: # point out the input is invalid
        print('invalid input.') # tell the user that the input is invalid
    
except Exception as ex: # find out the type of the error
    print('invalid input:', ex) # print the type of the error
    
        

        
