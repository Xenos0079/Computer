# I am late for the lec.


# the sequence of computation and the type of answers
a = int(240)
b = int(60)
print(a/b , type(a/b))

print(divmod(a , b), type(divmod(a , b))) # comment 001

a2 = 3
a2 *= 3 + 2
print('a2 = ', a2)

a3 = 3.6
a3 = int(a3)
print(a3)


# string , int , float


a4 = 5
b2 = 5.0
print(a4 == b2) # true
print(str(a4) == str(b2)) # false
print( a4 is b2) # false

b3 = '6.6'
try:
    print(int(b3)) # Value Error
except:
    print('Error')

print( 'str( 1 + 10 + 100 ) =' , str( 1 + 10 + 100 ) )

a5 = 1
b4 = 2
print(a5 , b4 , end = '...') # end and sep

print()
# eval
print(eval('10 + 20'), print(type(eval('10 + 20')))) # ???None

print()
print(0.5 == 0.1 + 0.1 + 0.1 + 0.1 + 0.1)

print()
print(bool(2 == True))
print(bool(2 == False))
print(bool(2) == True)
print(bool(2) == False)

#try:
    #print(bool(2 = True))
    #print(bool(2 = False))

#except:
    #print('Error 2')

print()
x = 3
if x == 3 :
    print('True 01')
else:
    print('False 01')

if 1 :
    print('True 02')

print()
b5 = 3
if b5 == 1 or 3 or 5:
    print(1)
if b5 == ( 1 or 3 or 5):
    print(3)

# print()
# round(3.45 , 0.1)
# print(round(3.45 , 0.1))
 # I dont know

print() # differences between 'is' and '=='
a = 1
b = 0.5*2
print(a is b)
print(a == b)

print()
c = 1
print(a is c)

print()
a = '123'
b = 123
c = '123'
print(a is b)
print(a is c)
print( a == b)
print(eval(a) is b)

print()
# if, elif, else
x = 5
if x >= 5:
    print(1)
    if x >=6:
        print(2)
    else:
        x = 3
elif x ==3:
    print(3)
else:
    print(4)

# use 'count'