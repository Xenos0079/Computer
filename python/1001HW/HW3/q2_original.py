target = input('Enter the polynomial: ') # Enter the polynomial

class polynomial: # create a class
    def __init__(self): # initializer
        self.__init__ = self # self
    
    def locate(): # find variable
        for letter in target: # search the string
            if ord(letter) >= 97 and ord(letter) <= 122 : # find letter
                variable = letter # mark the variable
        return variable # variable
    
    def sort_part(): # break the string into parts
        parts_temp = target.split('-') # use minus mark as seperator
        minus_initial = parts_temp[1:] # the minus parts
        minus = list() # store the minus parts

        for i in minus_initial: # Traverse
            j = '-' + i # add the minus mark
            minus.append(j) # add into list

        negative = list()# store the parts
        plus_initial = list() # store the parts
        first = list() # store the parts

        first.append(parts_temp[0])
        for i in first: # Traverse
            j = i.split('+') # use plus mark as seperator
            positive = j # add

        for i in minus: # Traverse
            j = i.split('+') # use plus mark as seperator
            k = j[0] # the first part
            l = j[1:] # the other are positive
            negative.append(k) # add
            plus_initial.append(l) # add

        for i in plus_initial: # Traverse
            for j in i: # Traverse
                positive.append(j) # add

        invalid = list() # store the parts
        single_variable = list() # store the parts
        one_constant = list() # store the parts
        one_degree = list() # store the parts
        full = list() # store the parts
        all = list() # store the parts

        for i in negative: # Traverse
            all.append(i) # add into list
        for i in positive: # Traverse
            all.append(i) # add into list

        for i in all: # Traverse
            if variable in i: # have variable
                if i == variable or i == '-' + variable : # if single
                    single_variable.append(i) # add into list
                elif '^' in i and '*' in i: # if full
                    full.append(i) # add into list
                elif '^' in i: # if the co-efficient is 1
                    one_constant.append(i) # add into list
                elif '*' in i: # if degree is 1
                    one_degree.append(i) # add into list
                else: # none of the above
                    invalid.append(i) # add into list
            else: # none of the above
                invalid.append(i) # add into list
        return invalid , single_variable , one_constant , one_degree , full , all # return the value
    
    def s_dev(): # Find the derivative of the given parts
        if len(single_variable) != 0: # not empty
            if single_variable[0] == variable: # check
                first_derivative.append('1') # get 1
            elif single_variable[0] == '-'+variable: # check
                first_derivative.append('-1') # get -1
            else: # empty
                return None # none
            
    def oc_dev(): # Find the derivative of the given parts
        for i in one_constant: # Traverse
            if i[0] == '-': # minus
                j = i[3:] # number part
            else: # positive
                j = i[2:] # number part
            num = int(j) - 1 # derivative process
            if num >=2: # need num
                dev = '-'+j+variable+'^'+str(num) # get dev
            elif num == 1: # no need
                dev = '-'+j+variable  # get dev
            first_derivative.append(dev) # add

    def od_dev(): # Find the derivative of the given parts
        if len(one_degree) != 0: # not empty
            for i in one_degree: # Traverse
                j = i[:-2] # number
                dev = j # process
            first_derivative.append(dev) # add
    
    def f_dev(): # Find the derivative of the given parts
        part = list() # store the parts
        for i in full: # Traverse
            j = i.split('*'+variable+'^') # split the two parts of number
            k = str(int(j[0])*int(j[1]))+'*'+variable # co-efficient and variable
            if int(j[1]) - 1 == 1: # degree is 1
                dev_f = k # dev get
                first_derivative.append(dev_f) # add
            elif int(j[1]) - 1 >= 2: # degree bigger than 1
                dev_f = k + '^' + str(int(j[1]) - 1) # dev get
                first_derivative.append(dev_f) # add
    
variable = polynomial.locate() # get variable
invalid , single_variable , one_constant , one_degree , full , all = polynomial.sort_part() # get the parts
first_derivative = list() # store the parts of first_derivative

polynomial.od_dev() # get the parts of first_derivative
polynomial.oc_dev() # get the parts of first_derivative
polynomial.f_dev() # get the parts of first_derivative
polynomial.s_dev() # get the parts of first_derivative

answer = list() # store the answer

if len(first_derivative) != 0: # not empty
    answer.append(first_derivative[0]) # add the first part
    for i in first_derivative[1:]: # the other part
        if i[0] == '-': # negative
            answer.append(i) # add
        else: # positive
            answer.append('+'+i) # add
    sep = '' # set the seperator
    final = sep.join(answer) # dock the parts into one string

if len(first_derivative) == 0: # empty
    final = '0' # answer

print('The first derivative of the given polynomial is: ' , final) # outcome

# Rewrite! You need to follow the order!