A = float(input('Enter the final account value'))
#let user enter the final account value

B = 1 + (float(input('Enter the annual interest rate')))/100
#let user enter the interest rate, then plus 1 to fit the equation

C = int(input('Enter the number of years'))
#let user enter the number of years

ida = A/(B**C)
#apply the equation and calculate the answer

print('The initial value is: ' ,ida)
#output the answer
    
