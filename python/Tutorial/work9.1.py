class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")
    def __init__(self):
        print("A's __init__() invoked")


class B(A):
    def __init__(self):
        print("B's __init__() invoked")


def main():
    b = B()
    print()
    a = A()

main()



#(self) :newinit  (self)self.i nvoked")print("A'snew
#__init__(self)defprint("A'sinvoked")init
#class B(A)init (self)defprint("B'sinit__() invoked")
#def ma in () 
#b=B ()a=A()