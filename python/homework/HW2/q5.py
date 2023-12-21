'''
(Game: locker puzzle) 
A school has 100 lockers and 100 students. All lockers are closed on the first day of school. 
As the students enter, the first student, denoted S1, opens every locker. 
Then the second student, S2, begins with the second locker, denoted L2, and closes every other locker. 
Student S3 begins with the third locker and changes every third locker (closes it if it was open, and opens it if it was closed). 
Student S4 begins with locker L4 and changes every fourth locker. 
Student S5 starts with L5 and changes every fifth locker, and so on, until student S100 changes L100.
After all the students have passed through the building and changed the lockers, which lockers are open? 
Write a program to find your answer.
(Hint: Use a list of 100 Boolean elements, each of which indicates whether a locker is open (True) or closed (False). Initially, all lockers are closed.)
'''

count_open = 0 # set the count for opened lockers
student = 100 # 100 students 
locker = 100 # 100 lockers
result = {} # store the result
answer = [] # store the answer

for i in range(1 ,locker+1):  # at the beginning
    result[i] = False # all the lockers are closed

def change(n):  #   use the recursion function
    if n <= 100: # below the range
        for j in range(n , student+1): # let student to act
            if j % n == 0: # meet the request
                result[j] = not result[j] # change the locker's state
        change(n + 1) # recursion
    if n == 101:  # out of the range
        return 0 # end the sequence

change(1) # start processing

for i in range(1, locker+1): # set the range
    if result[i] == True: # if open
        answer.append(i) # collect the answer
        count_open += 1 # count to sum

print("In the locker puzzle that has 100 students and 100 lockers, \nand the code of opening lockers are: ") # print the sentence
print(answer) # print the answer
print("So there are" , count_open , "open lockers.") # print the count