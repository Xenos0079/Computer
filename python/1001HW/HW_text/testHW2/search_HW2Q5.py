#! /usr/bin/python
#Start with 1000 students and 1000 closed lockers
#Student 1 performs function opens every locker
#Student 2 performs function on every other locker.
#Student 3 performs function on every third locker, etc.
#Student 4 performs function on every fourth locker, etc.
#Student n performs function on every nth locker while n is less than or equal to 1000
import math
print("Welcome to Student Locker Program")
lockers=1000
students=1000
lockersOpen=int(math.sqrt(lockers))
lockersClosed=lockers-lockersOpen

resultLockerIsOpen={}
print("\nLockers"),
for a in range(1,lockers+1):
    resultLockerIsOpen[a] = False;
    for b in range (1,students+1):
        if a%b == 0:
            resultLockerIsOpen[a]= not resultLockerIsOpen[a]
    if resultLockerIsOpen[a]:
        print("{},".format(a)),
print("are open.\n\nThe total lockers open are: {} and closed: {}.\n\nGoodbye!".format(lockersOpen, lockersClosed))

