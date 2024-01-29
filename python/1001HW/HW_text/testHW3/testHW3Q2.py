"""
Write a Python class that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial. 
Both the inputted polynomial and its derivative should be represented as strings.
For example...
Note: 
 (1) The inputted polynomial will contain only one variable, and the variable is anEnglish letter that is not necessarily x;
 (2) In the inputted polynomial, the terms are not necessarily arranged in descending or ascending orders;
 (3) The degree of each term of the inputted polynomial must be a non-negative integer; 
 (4) In the inputted polynomial, the coefficients will be placed before the variable;
 (5) In the inputted polynomial, no two terms will have an identical degree.
"""

# try to achieve it by a primary way first.
#  x^7-x^5+26*x^4+10*x^3-6*x^2-10*x+4 
# isalpha()

target = input('Enter the polynomial: ')
for l in target:
    if ord(l) >= 97 and ord(l) <= 122 :
        variable = l

parts_temp = target.split('-')

minus_initial = parts_temp[1:]

minus = list()

for i in minus_initial:
    j = '-' + i
    minus.append(j)

negative = list()
plus_initial = list()
first = list()

first.append(parts_temp[0])
for i in first:
    j = i.split('+')
    positive = j



for i in minus:
    j = i.split('+')
    k = j[0]
    l = j[1:]
    negative.append(k)
    plus_initial.append(l)

for i in plus_initial:
    for j in i:
        positive.append(j)

invalid = list()
single_variable = list()
one_constant = list()
one_degree = list()
full = list()
all = list()


for i in negative:
    all.append(i)
for i in positive:
    all.append(i)

for i in all:
    if variable in i:
        if i == variable or i == '-' + variable :
            single_variable.append(i)
        elif '^' in i and '*' in i:
            full.append(i)
        elif '^' in i:
            one_constant.append(i)
        elif '*' in i:
            one_degree.append(i)
        else:
            invalid.append(i)
    else:
        invalid.append(i)

first_derivative = list()

def s_dev():
    if len(single_variable) != 0:
        if single_variable[0] == variable:
            first_derivative.append('1')
        elif single_variable[0] == '-'+variable:
            first_derivative.append('-1')
        else:
            return None

def oc_dev():
    for i in one_constant:
        if i[0] == '-':
            j = i[3:]
            num = int(j) - 1
            if num >=2:
                dev = '-'+j+variable+'^'+str(num)
            elif num == 1:
                dev = '-'+j+variable
            first_derivative.append(dev)
        else:
            j = i[2:]
            num = int(j) - 1
            if num >= 2:
                dev = j+variable+'^'+str(num)
            elif num == 1:
                dev = j+variable
            first_derivative.append(dev)
    
def od_dev():
    if len(one_degree) != 0:
        for i in one_degree:
            j = i[:-2]
            dev = j
        first_derivative.append(dev)
    
def f_dev():
    part = list()
    for i in full:
        j = i.split('*'+variable+'^')
        k = str(int(j[0])*int(j[1]))+'*'+variable
        if int(j[1]) - 1 == 1:
            dev_f = k
            first_derivative.append(dev_f)
        elif int(j[1]) - 1 >= 2:
            dev_f = k + '^' + str(int(j[1]) - 1)
            first_derivative.append(dev_f)

od_dev()
oc_dev()
f_dev()
s_dev()


answer = list()

if len(first_derivative) != 0:
    answer.append(first_derivative[0])
    for i in first_derivative[1:]:
        if i[0] == '-':
            answer.append(i)
        else:
            answer.append('+'+i)
    sep = ''
    final = sep.join(answer)

if len(first_derivative) == 0:
    final = '0'

print(final)



