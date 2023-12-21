x = 5
y = 10
min = x if x < y else y
#print(min)
#max = x > y ? x : y
#print(max)

def myfun():
    pass
#print(myfun())

#print([1,2,3]*3)

#print([3] in [1,2,3,4])

#print(3 in [1,2,3,4])

##print(list(range(1,10,3)))

#print(list(range(6))[::2])

#print(1,2,3, sep =":")

#print('ab' in 'acbed')

#x7 = ['11','2','3']
#print(max(x))
#print(max(x7))

#print(sorted({'a':9 , 'b':3,'c':78}.values()))

#count_10 = 0
#k = 1000
#while k > 1:
#    print(k)
#    k = k//2
#    count_10 += 1
#    print(k , count_10)
"""
i = 1
while i+1:
    if i > 4:
        print('%d'%i)
        i += 1
        break
    print('%d'%i)
    i+=1
    i+=1
"""
'''
def demo(*para):
    avg = sum(para)/len(para)
    g = [i for i in para if i > avg]
    return (avg,)+tuple(g)
print(demo(1,2,3,4))
'''
'''
x = ['5', ' ', 'a']
sep = ''
y = ''.join(str(p) for p in x)
print(y)
'''

# 以下为手写代码题
# 03
'''
import random
list_02 = [int(random.randint(1 , 100)) for i in range (1 , 21)]
print(list_02)
temp1 = []
for index , value in enumerate(list_02):
    if index % 2 == 0:
        temp1.append(value)
        temp1.sort(reverse= True)
    print(temp1)
for n in range(0 , len(list_02)-1):
    if n % 2 == 0:
        list_02[n] = temp1[0]

'''
str2 = 'exam'
str1 = 'Runoob example'
#print(str2[5])
print(str1.find(str2 , 5))
print(str1[6])