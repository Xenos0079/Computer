def m1():
    x = 1+2**3/4*5
    y = 2**3
    z = 2**3/4
    print(x)
    print(y)
    print(z)
    print()

def m2():
    x = 1.33
    x = int(x)
    print(x)

def m3():
    bmi = 69 / (1.806**2)
    print(bmi)

def m4():
    x = 'Hello '
    print(x*8)
    x = 23
    print(eval('5//2')) 
    try:
        print(eval(x)) # eval() arg 1 must be a string, bytes or code object
    except:
        print('invalid')
    print(eval('x'))

def m5():
    __age__ = 24
    print(__age__)

def m6():
    a = 2
    b = 3
    c = 9
    ans = c//a+b*c%b**a
    what = b*c%b**a 
    now = (b*c%b)**a
    why = (b*c)%b**a
    print(ans)
    print(what)
    print(now)
    print(why)

def m7(a , b = 5 , c = 10):
    print('a is ' , a , 'and b is ' , b ,  'and c is ' , c )
#m7(3, 7)
#m7(25 , c=24)
#m7(c = 50 , a = 100)

def m8():
    # s = 'abc' # that is wrong
    # s = ('a','b','c') # wrong
    s = ['a','b','c'] #right
    print(s)
    s[1] = "d"
    print(s)
# m8()

# def m9():
    # c = int(369.g) error

def m10():
    i = 2
    while True:
        if i % 3 ==0:
            break
        print(i)
        i += 2
#m10()

def m11():
    for i in range(2):
        print(i)
#m11()

def m12():
    i = 0
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
#m12() 
# the output is 0 1 2

def m13():
    say = 'that is a string, hhh'
    # a = count(say) # wrong
    # b = say.count() # wrong
    # b = str.count(a) # wrong
    b = say.count('a' , 0) # right , count the string'a' when appear from the first element(0)
    print(b)
    c = say.count('h' , 1) # the '1' (h) is also counted
    print(c)
    d = say.count('h' , 2)
    print(d)

# m13()

#  https://www.runoob.com/python/att-string-strip.html
# when we say strip ,there are lstrip() , rstrip() , strip()

def m14():
    aList = [123, 'xyz', 'zara', 'abc', 'xyz']
    b = aList
    aList.reverse()
    b.reverse()
    c = aList.reverse()
    # b = aList.reverse()
    print ("List : ", aList)
    print(aList.reverse())
    print(b)
    print(c)
#m14()
#List :  ['xyz', 'abc', 'zara', 'xyz', 123]
#None
#[123, 'xyz', 'zara', 'abc', 'xyz']
#None


# reverse() will return None
def m15():
    str = "21442326abcrunoob2632154214444424"
    print (str.strip( '142' )) # no matter about the order and number
#m15()

###

def question(a, b, c):
    a = 4
    b[1] =a**a
    c *= a
    print(a, b, c)
#question(1,[2,4],3)

def m16():
    a = 3
    b = [2, 8]
    c = "9"
    print( 'a = ', a, 'b = ', b, 'c = ',c)
# global a, b, c   # Wrong?
    question(a ,b ,c)
    print( 'a = ', a, 'b = ', b, 'c = ',c) 
#m16()

def m17():
    list1 = [1 , 2 , 3 , 4 , 5]
    print(len(list1[ 1 : -2])) # 2
    print(list1[ 1 : -2]) # 2,3
    print()
    print(len(list1[ -1 : -2])) # 0
    print(list1[-2 : 1]) # empty
    print()
    print(len(list1[ -2 : 1]))
    print(list1[0 : 5])
    print()
    # print(list1[-6]) out of range
    

#m17()

def m18():
    str1 = 'my name is x'
    print(str1[1])
    for i in str1.split('n'):
        print(i , end = '\n')
        print()
        print(i , end = '/')

#m18()
def m20():
    if 'x' in {'x':1 , 45:2}.items():
        print('111')
    elif 1 in {'x':1 , 45:2}.items():
        print('222')
    else:
        print('No 1')

def m19():
    if 'number'.find('u') == 1 :
        print('OK')

#m19()

def m21():
    nums  = []
    while 1:       
        input_value = input('Enter a number:')
        if input_value == 'done': break

        value = float(input_value)
        nums += [value]
        c= sum(nums) / len(nums)
        print(len(nums))
        print('The value of c is' , c)

#m21()


"""
This is a string written over
more than one line
"""

""""
what? Yes
"""

def m22():
    x=5 // 2
    for i in range(10):
        for j in range(-1,-10,-1):
            x += 1
    print(x)

#m22() # 92

def m23():
    sentence = "nothingisimpossible"
    d=dict()
    for char in sentence:
        if char not in d:
            d[char] = 1
        else:
            d[char] = d[char] + 1
    print(d['s'])
    print(d.get('d'))
    print(d.get('d',0))

# m23()

def m24():
    def func(var):
        try:
            result = int(var)
            print(result)
        except ValueError:
            print("Error in ", var)
        else:
            print("No error")
    func("xyz")
    func("134")

# m24()

"""
try:
       # Some Code.... 
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
finally:
      # Some code .....(always executed)
"""
def m25():
    myDict = {' a':100, 'b':10, 'c':11 , 'd':21}
    myList = myDict.items() 

    newList = list()
    whatlist = list() 
    for e in myList:
        newTuple = (e[1],e[0])
        what = (e[1])
        print(newTuple)
        print('000')
        print(what)
        newList.append(newTuple)
        whatlist.append(what)
        print(newList)
        print('xxx')
        print(whatlist)
    print('The list before sorting:')
    print(newList)
    print('222')
    print(whatlist)
    print(' The list after sorting:')
    print(sorted(newList))
    print('333')
    print(sorted(whatlist))

# m25()

def m26():
    lst = [3, 2, 1]
    lst.append(lst)
    lstt =lst.append(lst)
    print(lst)
    print(lstt)
    a = list()
    for i in lst:
        a.append(i)
    print(a)

# m26()
def m27():
    a = 'hello'
    print(a.split("l")[0]) 
    print(a.split("l")[1])
    print(a.split("l")[2])

    for i in range(4):
        if i == 1:
            continue
        elif i == 2:
            break
        print(i)

#m27()

def m28():
    t  = [1,1,1]
    t.append(2)
    print(t)
    print()
    t.insert(1,3)
    print(t)
    print()
    t.pop(4)
    print(t)
    print()
    print(t[::-1])
    print(t[:-1])

#m28()
'''
n =(2,3,4)
y = {2:3,'e':6}
x = list(n)
y.items()
z = list(y)
print(x)
print(z)


print(pow(2,3))
print(pow(3,2))

'''
'''
print([m + n \
       for m in 'ABC' \
       for n in 'XYZ'])


def fact(n):
  return fact_iter(n, 1)
def fact_iter(num, product):
  print(num,product,sep='-')
  if num == 1:
      return product
  return fact_iter(num - 1, num * product)
print(fact(5))

'''

#print("d\s {}1\n\c\"4".format(520))
'''
a=2
b=4
c=6
if a:=b<c:
  print(a,b,c)
  print(a+b+c)
if a and b :
  print(a,b,c)
  print(str(c)*(a+b))
if a+b%c!=0:
  print(not b)


myDict = {"Amy": 18, "Barak": 21, "Daniel":25, "Caroline":17}
mySeq = list(myDict.items())
list1 = list()
list2 = list()
for i in range(len(mySeq)):
    key, value = mySeq[i]
    list1.append((key, value))
    if value < 18: 
        continue
    list2 +=[(value, key)]
print(list1)
print(list2)
list3 = sorted(list1)
list4 = sorted(list2)
print(list3)
print(list4)

print(len(list1))
print(type(list1[1]))

if -1:
    print('O()()')
if 0:
    print('?')
'''



#print(int('0233'))
#print(float('2.22'))

import random
a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)