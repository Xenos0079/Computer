def BinSum(L , start , stop):
    if start > stop :
        return 0
    elif start == stop - 1 :
        return L[start]
    else :
        mid = (start + stop)//2
        return BinSum(L , start , mid) + BinSum(L , mid , stop)

def main():
    L = [1 , 2 , 3 , 4 , 5 , 6 , 7]
    print('BinSum:', BinSum(L , 0 , len(L)))

main()