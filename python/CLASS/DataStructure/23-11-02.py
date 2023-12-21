# part 1 get time consumption
from time import time

startTime = time()

for i in range(1 , 10):
    print(i)

endTime = time()

print(endTime - startTime)


# part 2 Visualize the running time? 
# challenge of expermental analysis? No!