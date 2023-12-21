#'''
a = (1,2,3,4)
print(a[1:-1])
#'''
'''
class Animal:
    def __getinfo(self):
        return 'Animal'
    def printx(self):
        print(self.__getinfo())

class Dog(Animal):
    def __getinfo(self):
        return 'Dog'

Animal().printx()
Dog().printx()
'''

'''
def insertion(lst):
    for i in range(0 , len(lst)-1):
        j = i
        temp = lst[i + 1]
        while lst[j] < temp and j >= 0:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = temp
    return L
L = [3, 5, 2, 1, 6, 4, 9, 8]
insertion(L)
print(L)
'''

'''
def Fibo_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        lst = []
        for i in range(0,n):
            if i == 0 or i == 1:
                lst.append(1)
            else:
                lst.append(lst[i-1]+lst[i-2])
    return lst[n-1]
print(Fibo_1(9))

def Fibo_2(n):
    if n <= 2:
        return 1
    else:
        return (Fibo_2(n-1) + Fibo_2(n-2))
print(Fibo_2(9))
'''

'''
class A:
    def __init__(self,i = 0):
        self.i = i
class B(A):
    def __init__(self,j = 0):
        super().__init__() # modi
        self.j = j
def main():

    b = B()
    a = A() # modi
    print(b.i) # ori
    print(a.i) # modi
    print(b.j)
main() # Call the main function
'''
'''
class Student:
    def __str__(self):
        return 'Student'
    def printStudent(self):
        print(self.__str__())
class GraduateStudent(Student):
    def __str__(self):
        return "Graduate Student"
a = Student()
b = GraduateStudent()
a.printStudent()
b.printStudent()
print(isinstance(b , Student))
print(isinstance(a , GraduateStudent))
'''




