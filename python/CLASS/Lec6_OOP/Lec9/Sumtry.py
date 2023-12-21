def summing(l , n):
    if n == 0:
        return 0
    else:
        return summing(l , n-1) + l[n-1]

def main():
    l = [1 , 2 , 3 , 4 , 5 , 6 , 9 , 100 , 46 , 7]
    print('Sum:' , summing(l , len(l)))

main()