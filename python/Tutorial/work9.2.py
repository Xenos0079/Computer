class A:
    def __init__(self,p='a'):
        self.pa=p
    def ma(self):
        print("Method ma() for A")

class B:
    def __init__(self,p='b'):
        self.pb=p
    def mb(self):
        print("Method mb() for B")

class C(A):
    def __init__(self,p='c'):
        super().__init__()
        self.pc=p
    def ma(self):
        print("Method ma() for C")
    def mc(self):
        print("Method mc() for C")

class D(C):
    def __init__(self,p='d'):
        super().__init__()
        self.pd=p
    def mc(self):
        print("Method mc() for D")
    def md(self):
        print("Method md() for D")

class E(B,D):
    def __init__(self,p='e'):
        B.__init__(self)
        D.__init__(self)
        self.pe=p
    def ma(self):
        print("Method ma() for E")
    def me(self):
        print("Method me() for E")

a,b,c,d,e=A(),B(),C(),D(),E()

