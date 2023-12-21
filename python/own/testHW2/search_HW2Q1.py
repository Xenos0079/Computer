def babylonian_method(number, tolerance=1e-10):
    if number < 0:
        raise ValueError("Square root not defined for negative numbers.")
    guess = number
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2
    return guess

number = eval(input("Enter a number to get the square root of it."))
square_root = babylonian_method(number)
print(f"The square root of {number} is {square_root}.")