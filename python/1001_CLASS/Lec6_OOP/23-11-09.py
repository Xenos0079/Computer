def facf(n):
    if n < 0:
        print('Invalid')
    elif n == 0:
        return 1
    else:
        return n*facf(n-1)
    
a = facf(int(input('?')))
print(a)