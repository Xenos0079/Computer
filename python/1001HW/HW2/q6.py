'''
(Game: Eight Queens) 
The classic Eight Queens puzzle is to place eight queens on a chessboard such that no two queens can attack each other 
(i.e., no two queens are in the same row, same column, or same diagonal). 
There are many possible solutions. 
Write a program that displays one such solution.
'''

storage = [0 for i in range(1,10)] # create a box to store the answer

column = [False for i in range(1,10)] # set the column

diagonal = [False for i in range(1,18)] # set the diagonal

alter_diagonal = [False for i in range(1,15)] # set the reverse diagonal

def put(x, y, state : bool): # put the queen into the board
     if(state): # the position is valid
          storage[x] = y # the Xth row , Yth column is filled
     column[y] = diagonal[x + y] = alter_diagonal[x - y + 7] = state # record the position of column, diagonal and alter_diagonal

def check(x,y): # check if the postion is valid
          if((not column[y]) \
             and (not diagonal[x + y]) \
                and (not alter_diagonal[x - y + 7])): # use \ to spilt the code line, and the position must meet all the requirements
                  return True # the postion is valid
          else: # if not
               return False # the postion is invalid

def Answer(): # print the answer
    for i in range(1,9): # the column
        for j in range(1,9): # the row
            if(storage[j] == i): # if the position is valid --- line 19
                print('|Q',end ='') # set a queen
            else: # if not
                print('| ', end = "") # set a blank space
            if(j == 8): # end the line
                print('|', end ='\n') # set a |

def search(line): # the main function, integrate other functions
     for now_column in range(1,9): # the column we want to fill now
          if(check(line,now_column)): # check if valid
               put(line, now_column, True) # mark the queen's position
               if(line == 8): # all the rows is done
                    Answer() # print the answer
                    print() # print space
                    break # only print 1 answer
               else: # if the process is not done yet
                    search(line + 1) # start a new row
               put(line, now_column,False) # reset the position when it has been used

search(1) # start the program