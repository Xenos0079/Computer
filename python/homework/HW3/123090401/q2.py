class Polynomial(object): # create a class
    def __init__(self , polynomial): # initializer
        self.polynomial = polynomial # polynomial
        self.first_derivative = [] # first_derivative
 
    def derivative(self): # break the string into parts
        for letter in self.polynomial: # search the string
            if ord(letter) >= 97 and ord(letter) <= 122 : # find letter
                variable = letter # mark the variable
        new_poly = self.polynomial.replace('-' , '+-') # add dummy '+' for the split process
        true_list = new_poly.split('+') # split to get parts
        for i in true_list: # Traverse
            if variable in i: # have variable
                if i == variable or i == '-' + variable : # if single
                    self.s_dev(i , variable) # deri get
                elif '^' in i and '*' in i: # if full
                    self.f_dev(i , variable) # deri get
                elif '^' in i: # if the co-efficient is 1
                    self.oc_dev(i , variable) # deri get
                elif '*' in i: # if degree is 1
                    self.od_dev(i , variable) # deri get
        for i in range(1, len(self.first_derivative)): # search
            if self.first_derivative[i][0] != '-' : # positive
                self.first_derivative[i] = '+' + self.first_derivative[i] # add sign
        sep = '' # set the sep
        answer = sep.join(self.first_derivative) # combine
        return answer # return answer

    def s_dev(self , x , variable): # Find the derivative of the given parts
        if x == variable: # positice
            self.first_derivative.append('1') # get 1
        elif x ==  '-' + variable: # negative
            self.first_derivative.append('-1') # get -1
            
    def oc_dev(self , x , variable): # Find the derivative of the given parts
        if x[0] == '-': # negative
            j = x[3:] # number part
            num = int(j) - 1 # derivative process
            if num >=2: # need num
                dev = '-'+j+variable+'^'+str(num) # get dev
            elif num == 1: # no need
                dev = '-'+j+variable  # get dev
            self.first_derivative.append(dev) # add
        else: # positive
            j = x[2:] # number part
            num = int(j) - 1 # derivative process
            if num >=2: # need num
                dev = j+variable+'^'+str(num) # get dev
            elif num == 1: # no need
                dev = j+variable  # get dev
            self.first_derivative.append(dev) # add

    def od_dev(self , x , variable): # Find the derivative of the given parts
        dev = x[:-2] # number
        self.first_derivative.append(dev) # add

    def f_dev(self , x , variable): # Find the derivative of the given parts
        j = x.split('*'+variable+'^') # get two parts
        k = str(int(j[0])*int(j[1]))+'*'+variable # part 1
        if int(j[1]) - 1 == 1: # degree is 1
            dev_f = k # dev get
            self.first_derivative.append(dev_f) # add
        elif int(j[1]) - 1 >= 2: # degree bigger than 1
            dev_f = k + '^' + str(int(j[1]) - 1) # dev get
            self.first_derivative.append(dev_f) # add