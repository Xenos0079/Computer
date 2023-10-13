num = input('Enter a number')  # let user set a number
num = eval(num)                # change the data type of "num"

little = 1                     # let the loop count start from 1
while little ** 2 <= num:      # compare the little square with num
    little = little + 1        # add 1 to the little and reset

print(little)                  # print the final answer
    
