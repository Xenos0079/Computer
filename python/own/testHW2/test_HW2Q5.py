#! /usr/bin/python
#Start with 1000 students and 1000 closed lockers
#Student 1 performs function opens every locker
#Student 2 performs function on every other locker.
#Student 3 performs function on every third locker, etc.
#Student 4 performs function on every fourth locker, etc.
#Student n performs function on every nth locker while n is less than or equal to 1000

'''
import math
print("Student Locker Program")

lockers = 100
students = 100
lockersOpen = int(math.sqrt(lockers))
lockersClosed = lockers - lockersOpen

resultLockerIsOpen={}
print("\nLockers\n"),
for a in range(1,lockers + 1):
    resultLockerIsOpen[a] = False;
    for b in range (1,students + 1):
        if a%b == 0:
            resultLockerIsOpen[a]= not resultLockerIsOpen[a]
    if resultLockerIsOpen[a]:
        print("{},".format(a)),
print("are open.\n\nThe total lockers open are: {} and closed: {}.\n\nGoodbye!".format(lockersOpen, lockersClosed))
'''
'''
result = {}
def lockerGame(student = 100 , locker = 100):
    for i in range(1 , locker+1):
        result[i] = False
        for j in range(1 , student + 1):
            if i % j == 0 :
                result[i] = not result[i] 
        if result[i]:
            print('{},'.format(i))

lockerGame()
'''
count_open = 0
student = 100
locker = 100
result = {}
answer = []

for i in range(1 ,locker+1):
    result[i] = False

def change(n):
    if n <= 100:
        for j in range(n , student+1):
            if j % n == 0:
                result[j] = not result[j]
        change(n + 1)
    if n == 101:
        return 0

change(1)

for i in range(1, locker+1):
    if result[i] == True:
        answer.append(i)
        count_open += 1

print(result)
print(answer)
print(count_open)

        






