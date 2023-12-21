# (Emirp) An emirp (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime. 
# For example, both 17 and 71 are prime numbers, so 17 and 71 are emirps. 
# Write a program that displays the first 100 emirps. Display 10 numbers per line and align the numbers properly, as follows:

import math

def is_prime(target): # define a new function to judge whether a given munber is a prime number
    sr = int(target ** 0.5)+1 # get a possible set of factors
    for i in range(2,sr): # set a loop
        if target%i == 0: # if the target can be divisible
            return False # the target won't be a prime number
    return True # if the loop can't satisfy the false request ,then the target is a prime number

def emirp(num):
   if not is_prime(num):
      return False
   reverse_num = 0
   temp = num
   while num != 0:
        d = num % 10
        reverse_num = reverse_num * 10 + d
        num = int(num / 10)
   if temp == reverse_num:
        return False
   return is_prime(reverse_num)

N = int(100000) # enter the number
count = 0 # prepare the count place for each line
line = 0
if N > 0:  # judge that N is positive
    len_digit = int(math.log10(N))+1 # find out the length of the digit
    for i in range(10,N): # judge that whether i is a prime number
        if emirp(i): # use the defined function
            count += 1 # add a count for the place of line
            if count%10 == 0: # We have to start a new line
                print('%*d'%(len_digit,i),'%s'%' ') # start a new line
                line += 1
                if line == 10:
                   break
            else: # just keep print the number
                print('%*d'%(len_digit,i),'%s'%' ',end = '') # print the number
 


   