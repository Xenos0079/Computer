# HW2 q1

def sqrt(n):
    if n < 0:
        print("Wrong!")
    if n >= 0:
        lastGuess = 1
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        while abs(nextGuess - lastGuess) > 0.0001:
            lastGuess = nextGuess
            nextGuess = (lastGuess + (n / lastGuess)) / 2
    return nextGuess

        

n = eval(input("?"))
# sqrt = sqrt(n)
print(sqrt(n))
exit()
# The program is wrong
# but I fix it!

## use babylonian function tu calculate square root
'''
def babylonian_method(number, tolerance=0.0001):
    if number < 0:
        raise ValueError("Square root not defined for negative numbers.")
    guess = number
    while abs(guess ** 2 - number) > tolerance:
        guess = (guess + number / guess) / 2
    return guess

number = eval(input("Number?"))
square_root = babylonian_method(number)
print("The square root of " , number , " is " , square_root , ".")

'''
'''
def sqrt(number):
    if number < 0:
        print("Square root not defined for negative numbers.")
        return None
    if number >= 0:
        lastGuess = 1.0
        tolerance = 0.0001
        nextGuess = (lastGuess + (number / lastGuess)) / 2
        while abs(nextGuess - lastGuess) >= tolerance:
            lastGuess = nextGuess
            nextGuess = (lastGuess + (number / lastGuess)) / 2
    return nextGuess

'''