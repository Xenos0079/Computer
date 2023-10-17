dict1 = {'b':2,'c':3,'d':4,'a':1,'123':9,'e':5}

print(dict1)
print()

list1 = list(dict1.items())
print(list1)
print()

list2 = list1.sort()
print(list2) # WHAT HAPPENED?
print(list1)