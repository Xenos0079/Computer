num = input('Give')
num = eval(num)
def rev(num):
    num = str(num)
    rev_num = reversed(num)
    print(rev_num)
    #return True

def isP(num):
    num = str(num)
    rev_num = reversed(num)
    if num == rev_num:
        print('Yes')
    #return True

rev(num)
isP(num)