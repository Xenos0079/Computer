# dictionary
purse = dict()
print(type(purse))
purse['a'] = 10.11
purse['eee'] = 1
purse[1] = 1
print(purse)


test1 = [1,2,3,4,12,36]
test2 = {'hello':1,'nihao':2,'test!':30}
print(test1,type(test1))
print(test2,type(test2))

# What are keys and values?
# at line 4 ,'a' is key and 10.11 is value and value can only be numbers


# "in" function
wordDict = dict()
while True:
    word = input( 'Enter a word:') 

    if word in wordDict:
        wordDict[word]=wordDict[word]+1
    elif word=='done':
        break
    else:
        wordDict[word]=1

print(' The result of word count:print(wordDict')
print(wordDict)



#Retrieving lists of keys and valuesa
#Bonus: two iteration variables
#tuples

