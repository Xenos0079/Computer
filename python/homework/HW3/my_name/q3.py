import random # import random
class Ecosystem: # class
    def __init__(self , river_length, num_fish , num_bears): # data
        self.sep = '' # sep
        self.river = [] # river
        self.length = int(river_length) # length
        self.fish = int(num_fish) # fish
        self.bear = int(num_bears) # bear
        if self.fish + self.bear <= self.length: # meet the need
            for i in range(1 , self.fish+1): # add fish
                self.river.append('F') # add
            for i in range(1 , self.bear+1): # add bear
                self.river.append('B') # add
            for i in range(1 , self.length-self.bear-self.fish+1): # add none space
                self.river.append('N') # add
            random.shuffle(self.river) # shuffle to random order
            # print('initial condition:') # message
            print(self.sep.join(self.river)) # the initial condition
        else: # overflow
            print('Fail to initialize the river, because the sum of fish and bears is larger than the room of river length. \
                  Other reason may be your input are invalid.') # error report

    def left_edge(self , index): # left edge
        if index == 0: # meet
            return True # true
        else: # not
            return False # false

    def right_edge(self , index): # right edge
        if index == len(self.river)-1: # meet
            return True # true
        else: # not
            return False # false
    
    def choose(self): # use random x to judge the animal will move to left or right or still
        from random import random # use random
        x = random() # create a number x
        if x <= 1/3: # condition 1
            return 'left' # go left
        elif x <= 2/3: # condition 2
            return 'right' # go right
        else: # condition 3
            return 'still' # still
        
    def execute(self): # the simulation()
        for index in range(1, len(self.river)): # Traverse
            if not 'x' in self.river[index]: # no mark detected
                if not self.right_edge(index) and self.choose() == 'right': # go right when not in the right edge
                    self.move(index , index+1) # move
                elif not self.left_edge(index) and self.choose() == 'left': # go left when not in the left edge
                    self.move(index , index-1) # move
        alter = {'Fx':'F' , 'Bx':'B'} # remove the mark
        new_river =[alter[i] if i in alter else i for i in self.river] # remove the mark
        self.river = new_river # change the river
        print(self.sep.join(self.river)) # print the output

    def move(self , index , change): # move in condition
        if self.river[change] == 'N' and self.river[index] != 'N': # animal move to none space
            self.river[change] = self.river[index] + 'x' # none space change into animal
            self.river[index] = 'N' # animal has gone
        if self.river[change] == self.river[index] and self.river[index] != 'N': # meet the spawn process
            space = list() # create a list to store the None space
            for location , target in enumerate(self.river): # search the river
                if target == 'N': # the value meets the need
                    space.append(location) # record the index of the target location
            from random import choice # need to use choice()
            if len(space) != 0: # vaild location is/are exist
                self.river[choice(space)] = self.river[index]+'x' # choose a random None space to spawn a new animal
        if self.river[change] == 'B'  and self.river[index] == 'F': # fish meets bear
            self.river[index] = 'N' # fish dies
        if self.river[change] == 'F'  and self.river[index] == 'B': # bear meets fish
            self.river[index] = 'N' # bear gone
            self.river[change] = 'Bx' # bear eat fish
    def display_river(self): # get the river
        return self.river # return

    def simulate(self , steps): # the simulation process
        steps = int(steps) # steps type
        for i in range(1 , steps+1): # for loop
            # print('step' , i) # message
            self.execute() # print every step

'''test code below'''
ecosystem_1 = Ecosystem(river_length=3, num_fish=1, num_bears=1)
ecosystem_1.simulate(steps=2)
print()

ecosystem_2 = Ecosystem(river_length=10, num_fish=3, num_bears=2)
ecosystem_2.simulate(steps=5)
print()

ecosystem_3 = Ecosystem(river_length=8, num_fish=2, num_bears=1)
ecosystem_3.simulate(steps=10)
print()

ecosystem_4 = Ecosystem(river_length=10, num_fish=2, num_bears=3)
ecosystem_4.simulate(steps=10)