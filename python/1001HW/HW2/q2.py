'''
(Emirp) An emirp (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime. 
For example, both 17 and 71 are prime numbers, so 17 and 71 are emirps. 
Write a program that displays the first 100 emirps. Display 10 numbers per line and align the numbers properly, as follows:
'''
import math # use the math function

def is_prime(target): # define a new function to judge whether a given munber is a prime number
    sr = int(target ** 0.5)+1 # get a possible set of factors
    for i in range(2,sr): # set a loop
        if target%i == 0: # if the target can be divisible
            return False # the target won't be a prime number
    return True # if the loop can't satisfy the false request ,then the target is a prime number

def emirp(num): # define the emirp() to judge if the number is meet the need
   if not is_prime(num): # the initial judge is failed
      return False # send false signal
   reverse_num = 0 # define the reverse number and set the initial value
   temp = num # restore the num
   while num != 0: # start the process
        d = num % 10 # get the first digit
        reverse_num = reverse_num * 10 + d # place the highest digit
        num = int(num / 10) # get ready for the second digit
   if temp == reverse_num: # when the number is palindromic
        return False # fail the check
   return is_prime(reverse_num) # send the result

N = int(100000) # set the ceiling
count = 0 # prepare the count place for each line
line = 0 # count every line
if N > 0:  # judge that N is positive
    len_digit = int(math.log10(N))+1 # find out the length of the digit
    for i in range(10,N): # judge that whether i is a prime number
        if emirp(i): # use the defined function to judge whether the number is a emirp
            count += 1 # add a count for the place of line
            if count%10 == 0: # We have to start a new line
                print('%*d'%(len_digit,i),'%s'%' ') # start a new line
                line += 1 # count the line
                if line == 10: # when the line is up to 10
                   break # end the loop
            else: # just keep print the number
                print('%*d'%(len_digit,i),'%s'%' ',end = '') # print the number