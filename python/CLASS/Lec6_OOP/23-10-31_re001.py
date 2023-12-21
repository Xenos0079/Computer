# Object = everything
# use ' id() ' or ' type() ' to get info about a project
# id is a unique interger. When the program is executed, it will be created by python
# will not be changed during the program

# type is determined by python according to the value.

# variable is only a reference to an object

# __init__()
# constructor:  __new__()
# the first parameter: self
class Count:
    def __init__(self,count=0):
        self.count=count

def increment(c,times) :
    c.count+=1
    times+=1

def main () :
    c=Count()
    times=0
    for i in range(100):
        increment(c,times)
    print("count is ",c.count)
    print("time is ",times)
main()