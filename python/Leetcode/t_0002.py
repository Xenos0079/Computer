l1 = [2,3,4]
x1 = []
for i in range(0 , len(l1)):
    x1.append(str(l1[i]))
y1 = ''.join(x1)
print(y1)
l2 = [2,3,4]
x2 = []
for i in range(0 , len(l2)):
    x2.append(str(l2[i]))
y2 = ''.join(x2)
print(y2)
z = list(str(eval(y1 +'+'+ y2)))
print(z)