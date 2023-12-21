import random # import random to use the shuffle()

class eco_system: # create a class
    def __init__(self , length, fish , bear): # initializer
        self.river = [] # a list
        self.length = int(length) # the river's length to store the animal
        self.fish = int(fish) # fish number
        self.bear = int(bear) # bear number
        if self.fish + self.bear <= self.length: # the storage is enough
            for i in range(1 , self.fish+1): # count fish
                self.river.append('F') # add to river
            for i in range(1 , self.bear+1): # count
                self.river.append('B') # add to river
            for i in range(1 , self.length-self.bear-self.fish+1): # count the empty
                self.river.append('N') # add
            random.shuffle(self.river) # shuffle it to have a random order
        else: # if the input is invalid or the the storage is not enough
            print('Fail to initialize the river, because the sum of fish and bears is larger than the room of river length. \
                  Other reason may be your input are invalid.') # report the error

    def left_edge(self , index): # judge if the index is located in the left edge
        if index == 0: # identify the location
            return True # pass
        else: # if not
            return False # fail

    def right_edge(self , index): # judge if the index is located in the right edge
        if index == len(self.river)-1: # identify the location
            return True # pass
        else: # if not
            return False # fail
    
    def choose(): # use random x to judge the animal will move to left or right or still
        from random import random # use random
        x = random() # create a number x
        if x <= 1/3: # condition 1
            return 'left' # go left
        elif x <= 2/3: # condition 2
            return 'right' # go right
        else: # condition 3
            return 'still' # still
        
    def simulation(self): # the simulation()
        for index , animal in enumerate(self.river): # extract the index and the value
            if not eco_system.right_edge(self , index) and eco_system.choose() == 'right': # go right when not in the right edge
                eco_system.move(self , index , animal , index+1) # move
            if not eco_system.left_edge(self , index) and eco_system.choose() == 'left': # go left when not in the left edge
                eco_system.move(self , index , animal , index-1) # move

    def move(self , index , animal , change): # move in condition
        if self.river[change] == 'N' and animal != 'N': # animal move to none space
            self.river[change] = animal # none space change into animal
            self.river[index] = 'N' # animal has gone
        if self.river[change] != 'N'  and animal == self.river[change]: # animal meet the same species
            space = list() # create a list to store the None space
            for location , target in enumerate(self.river): # search the river
                if target == 'N': # the value meets the need
                    space.append(location) # record the index of the target location
            from random import choice # need to use choice()
            if len(space) != 0: # vaild location is/are exist
                self.river[choice(space)] = animal # choose a random None space to spawn a new animal
        if self.river[change] == 'B'  and animal == 'F': # fish meets bear
            self.river[index] = 'N' # fish dies
        if self.river[change] == 'F'  and animal == 'B': # bear meets fish
            self.river[index] = 'N' # bear gone
            self.river[change] = 'B' # bear eat fish

    def get_river(self): # get the river
        return self.river # return

def main(): # the provcess
    print('Create a eco-system by your own! You need to enter the initial values and the times of cycle.') # annoucement
    length = input('Enter the length of the river: ') # input the length
    fish = input('Enter the amount of the fish: ') # input the fish
    bear = input('Enter the amount of the bear: ') # input the bear
    N = int(input('Enter the number N which is the times of simulation required: ')) # input the N

    base = eco_system(length , fish , bear) # create the base in eco class
    sep = '' # no seperator
    for i in (1 , N+1): # execute simulation for N times
        base.simulation() # execute
    print(sep.join(base.get_river())) # print the answer
        
main() # operate