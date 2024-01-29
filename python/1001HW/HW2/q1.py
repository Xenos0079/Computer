'''
(Math: approximate the square root) 
There are several techniques for implementing the sqrt function in the math module. 
One such technique is known as the Babylonian function. 
It approximates the square root of a number, n, by repeatedly performing a calculation using the following formula:
nextGuess = (lastGuess + (n / lastGuess)) / 2
When nextGuess and lastGuess are almost identical, nextGuess is the approximated square root. 
The initial guess can be any positive value (e.g., 1). 
This value will be the starting value for lastGuess. 
If the difference between nextGuess and lastGuess is less than a very small number, such as 0.0001, 
you can claim that nextGuess is the approximated square root of n. 
If not, nextGuess becomes lastGuess and the approximation process continues. 
Implement the following function that returns the square root of n.
def sqrt(n):
'''
def sqrt(n): # define a fuction to execute the squareroot process
    try: # when the input is valid:
        if n >= 0: # the input that meet the test
            lastGuess = 1 # begin with 1 as the question mentioned. 
            nextGuess = (lastGuess + (n / lastGuess)) / 2 # get the 1st 'next guess'
            while abs(nextGuess - lastGuess) > 0.0001: # if the answer isn't meet the minimum error:
                lastGuess = nextGuess # reset the guess value 
                nextGuess = (lastGuess + (n / lastGuess)) / 2 # repeat the sequence, until the error is small enough
        return nextGuess # get the final apprpximation
    except: # when the input is invalid:
        print("Invalid input.") # send the message

n = eval(input("Enter the taegrenumber to get its square-root: ")) # let the user enter the number
print('The square-root of the number ' , n , 'is: ' , sqrt(n)) # print the output


