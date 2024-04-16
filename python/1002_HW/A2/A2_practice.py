""" 
step_1:
import the crucial module
"""
import random
import turtle
###


"""
step_2:
let the user decide the size of the puzzle
"""
def get_size():
    size = 0
# initialize the size
    while size not in [3,4,5]:
        size = int(turtle.numinput('Sliding Puzzle GUI - 123090401','You need to enter 3 4 or 5 for the size of the board'))
# get the size from the user
# the process would repeat until the input is valid
        total = size ** 2

    return size, total
###

"""
step_3:
initialize a sequence of random numbers and judge if they can be solved as the puzzle
-n- is the -total- from the get_size() function, which represent the length of the sequence of the puzzle,
"""
def solvable_judge(n):
    sq = list(range(n))
    random.shuffle(sq)
    if sum(1 for i in range(n-1) for j in range(i+1, n) if sq[i] > sq[j]) % 2 != 0:
        sq[-2], sq[-1] = sq[-1], sq[-2]
# use inversion until a solvable number sequence is generated
    return sq
###

"""
step_4:
draw a template of the square with its number mark in text box
"""
def draw_square():
    text = turtle.Turtle()
    text.hideturtle()
# the defualt color is black, so the setting is not needed
    text.speed(3)
    text.up()

# above is the textbox and below is the shape of the square
    
    block = turtle.Turtle()
    block.shape('square')
    block.color(173/255, 216/255, 230/255) # light blue code
    block.shapesize(4)
    block.speed(3)
    block.up()

    return block, text
###

"""
step_5:
generate the puzzle
"""
def generate_puzzle(size, total, gap, sequence):
    void = sequence.index(0) # find the void
    lar = gap + 90 # get the size of the square
    block_list, text_list, number_list = [], [], [] # set three list to store
    x, y = -(size//2 + 0.5) * 90 + size//2 + gap, -size * lar + (size//2) * 90 + size//2 * gap # find the position

    turtle.tracer(0) # shut the anime
    for serial in range(total): # every num
        b, t = draw_square()
        pos_x, pos_y =(serial) % size, size - serial // size
        b.goto(x + pos_x * lar, y + pos_y * lar)

        if serial <= 9: # the num has 1 digit
            t.goto(x + pos_x * lar - 5, y + pos_y * lar - 12) # go to right pos
        else: # the num has 2 digit
            t.goto(x + pos_x * lar - 10, y + pos_y * lar - 12) # go to right pos
        block_list.append(b)
        text_list.append(t)
        # add to the list
    block_list[void].hideturtle() # void block
    turtle.tracer(1) # reopen the anime

    for i in range(len(text_list)): # write the text
        if sequence[i] == 0: # void
            pass
        else:
            text_list[i].write(sequence[i],font=('Arial', 20, 'normal')) # type the code
        number_list.append(sequence[i]) # add
    return block_list, text_list, number_list
###

"""
step_6:
click the square to move it
"""
def click(x, y):
    global block_list, text_list, number_list, size, gap, total
    if not checkpoint(number_list, total): # game not over
        void = number_list.index(0) # find void
        row, col = (void) % size + 1, (void) // size + 1 # void pos
        for u in block_list: # every block
            if u.distance(x, y) < 27 + gap: # the neighbor block
                next = block_list.index(u) # ready to exchange
                row_new, col_new = (next) % size + 1, (next) // size + 1 # find pos
                
                if (col_new - col) * (row_new - row) == 0 and (col_new - col)+(row_new - row) != 0 \
                        and (col_new - col == 1 or row_new - row == 1 or col_new - col == -1 or row_new - row == -1):
                    x_void, y_void = block_list[void].position()
                    x_next, y_next = block_list[next].position()
                    # set
                    text_list[next].clear() # ready to rewrite the text
                    if next <= 9: # 1 digit
                        text_list[next].goto(x_void - 5, y_void - 12)
                        text_list[void].goto(x_next - 5, y_void - 12)
                    else: # 2 digit
                        text_list[next].goto(x_void - 10, y_void - 12)
                        text_list[void].goto(x_next - 10, y_void - 12)

                    block_list[next].goto(x_void,y_void)
                    block_list[void].goto(x_next,y_next)
                    # change the position
                    text_list[next].write(number_list[next], font=('Arial', 20, 'normal'))
                    # write the text
                    void_block, void_text = block_list[void], text_list[void]
                    block_list[void], block_list[next] = block_list[next],void_block
                    text_list[void], text_list[next] = text_list[next], void_text
                    number_list[void], number_list[next]= number_list[next], 0
                    # settle the void
                if checkpoint(number_list, size): # check
                    endgame(block_list, text_list, number_list) # endgame 
                    turtle.bye() # end
    else:
      endgame(block_list, text_list, number_list) # endgame
      turtle.bye() # end
###

"""
step_7:
prepare the endgame() to chamge the color
prepare the checkpoint() to check if the puzzle is finished
"""
def checkpoint(number_list, total):
    if number_list == [i for i in range(1, total)] + [0]: # the right sequence
        return True # can be ended
    else:
        return False # must continue

def endgame(block_list, text_list, number_list): 
    turtle.tracer(0) # end the anime
    for i in block_list: # all the block
        i.color('red')
    turtle.update() # refresh
    
    for num in range(len(text_list)):
        if number_list[num] != 0: # not void
            text_list[num].write(number_list[num], font = ('Arial', 20 , 'normal')) # rewrite the text
    turtle.done() # end
###

"""
step_8:
encode the main process
"""
gap = 3
size, total = get_size()
sq = solvable_judge(total)
block_list, text_list, number_list = generate_puzzle(size, total, gap, sq)
turtle.onscreenclick(click)
turtle.mainloop()
###