"""
Write a Python class to simulate an ecosystem containing two types of creatures, bears and fish.
The ecosystem consists of a river, which is modeled as a relatively large list. 
Each element of the list should be a Bear object, a Fish object, or None. 
In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. 
If two animals of the same type are about to collide in the same cell, then they stay where they are, 
but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list 
(if there is no empty location in the list, the newly generated animal will be discarded). 
If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
Write an initializer for the ecosystem class, 
the initializer should allow the user to assign the initial values of the river length, the number of fishes 
and the number of bears. Before the simulation, fishes and bears should be allocated randomly into the river. 
The ecosystem class should also contain a simulation() method, which will simulate the next N steps of the random moving process. 
N should be inputted by the user. In each step of your simulation, all animals in the river should try to take some random moves. 
In each step of your simulation, the animals should take actions one by one. The animals on the left will take action first. 
The newly generated animals will NOT take actions in the current step.
For example, assume that before the simulation, the initial state of the river is:
In which, 'F', 'B' and 'N' denote fish, bear and empty location respectively. 
Assume that in the first step of simulation, the first fish will move to the left, 
the first bear will move to the right, and the second bear will remain still. 
Then after the first step, the state of the river is:
To generate random numbers in Python, you should import the random() function by using the following statement:
By assigning the return of the random() function to a variable, you will get a random floating point number in the range of [0, 1].
The following code is an example of using the random() function:
"""
import random

class eco_system:
    def __init__(self , length, fish , bear):
        self.river = []
        self.length = int(length)
        self.fish = int(fish)
        self.bear = int(bear)
        if self.fish + self.bear <= self.length:
            for i in range(1 , self.fish+1):
                self.river.append('F')
            for i in range(1 , self.bear+1):
                self.river.append('B')
            for i in range(1 , self.length-self.bear-self.fish+1):
                self.river.append('N')
            random.shuffle(self.river)
        else:
            print('Fail to initialize the river, because the sum of fish and bears is larger than the room of river length. \
                  Other reason may be your input are invalid.')

    def left_edge(self , index):
        if index == 0:
            return True
        else:
            return False

    def right_edge(self , index):
        if index == len(self.river)-1:
            return True
        else:
            return False
    
    def choose():
        x = random.random()
        if x <= 1/3:
            return 'left'
        elif x <= 2/3:
            return 'right'
        else:
            return 'still'
        
    def simulation(self):
        for index , animal in enumerate(self.river):
            if not eco_system.right_edge(self , index) and eco_system.choose() == 'right':
                eco_system.move(self , index , animal , index+1)
            if not eco_system.left_edge(self , index) and eco_system.choose() == 'left':
                eco_system.move(self , index , animal , index-1)

    def move(self , index , animal , change):
        if self.river[change] == 'N' and animal != 'N':
            self.river[change] = animal
            self.river[index] = 'N'
        if self.river[change] != 'N'  and animal == self.river[change]:
            space = list()
            if animal == 'N':
                space.append(index)
            from random import choice
            if len(space) != 0:
                self.river[choice(space)] = animal
        if self.river[change] == 'B'  and animal == 'F':
            self.river[index] = 'N'
        if self.river[change] == 'F'  and animal == 'B':
            self.river[index] = 'N'
            self.river[change] = 'B'

    def get_river(self):
        return self.river

def main():
    input('Create a eco-system by your own! You need to enter the initial values and the times of cycle.')
    length = input('Enter the length of the river: ')
    fish = input('Enter the amount of the fish: ')
    bear = input('Enter the amount of the bear: ')
    N = int(input('Enter the number N which is the times of simulation required: '))

    base = eco_system(length , fish , bear)
    for i in (0 , N):
        base.simulation()
    sep = ''
    print(sep.join(base.get_river()))
        
main()



      