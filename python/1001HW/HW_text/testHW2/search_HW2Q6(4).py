storage = [0 for i in range(1,10)]

column = [False for i in range(1,10)]

diagonal = [False for i in range(1,18)]

alter_diagonal = [False for i in range(1,15)]

def Answer():
    for i in range(1,9):
        for j in range(1,9):
            if(storage[j] == i): 
                print('|Q',end ='')
            else: 
                print('| ', end = "")
            if(j == 8): 
                print('|', end ='\n')
        


def check(x,y):
          if((not column[y]) \
             and (not diagonal[x + y]) \
                and (not alter_diagonal[x - y + 7])):
                  return True
          else: 
               return False
          
def put(x, y, state : bool):
     if(state): 
          storage[x] = y
     column[y] = diagonal[x + y] = alter_diagonal[x - y + 7] = state

     
def search(line):
     for now_column in range(1,9):
          if(check(line,now_column)):
               put(line, now_column, True)
               if(line == 8): 
                    Answer()
                    print()
                    break
               else: 
                    search(line + 1)
               put(line, now_column,False)

search(1)