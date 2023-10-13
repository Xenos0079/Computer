#s1 = eval(input('side1'))
#s2 = eval(input('side2'))
#s3 = eval(input('side3'))

#def isvalid(s1, s2, s3):

#Define a function to check whether the values of three sides is valid
def isValid(side1,side2,side3):
    return (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1)

#Calculate the area of a triangle given the values of its three sides
def area(side1,side2,side3):
    costheta=(side1**2+side2**2-side3**2)/(2*side1*side2)
    sintheta=(1-costheta**2)**0.5
    return 0.5*side1*side2*sintheta

#from MyTriangle import *        #Import all functions in the module MyTriangle

#Define a main function to input three sides of a triangle and judge whether it is a valid triangle
def main():
    a,b,c=eval(input("Enter the three sides of a triangle:"))
    if isValid(a,b,c):
        print("The area of the triangle is %.2f."%area(a,b,c))
    else:
        print("The input is invalid.")

main()