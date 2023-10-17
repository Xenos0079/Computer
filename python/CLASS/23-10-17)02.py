# Solution: Finding the 10 most common words in a file
fhand = open ( 'myhost.txt','r')
counts = dict()
for line in fhand:
    words = line.split ()
    for word in words :
        counts[word] = counts.get (word,0)+1
lst = list()
for key,val in counts.items():
    lst.append((val,key))

lst.sort(reverse = True)
for val,key in lst[:10]:
    print(key,val)