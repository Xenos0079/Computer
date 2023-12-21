'''
def Power(x , n):
    if n == 0:
        return 1
    elif x != 0 and x % 2 == 1:
        return x * ((n // 2)**2)
    elif x != 0 and x % 2 == 0:
        return x * ((n // 2)**2)
'''
# ?

def power(x,n):
    if n == 0:
        return 1
    else:
        partial =  power(x , n//2)
        result = partial ** 2
        if n % 2 == 1:
            result = result * x
        return result