import random
import turtle

def get_size():
    size = 0

    while size not in [3,4,5]:
        size=int(turtle.numinput('Sliding Puzzle GUI - 123090401','You need to enter 3 4 or 5 for the size of the board'))

        total = size**2

    return size, total

def solvable_sequence(n):
    sq = list(range(n))
    random.shuffle(sq)
    if sum(1 for i in range(n-1) for j in range(i+1, n) if sq[i] > sq[j]) % 2 != 0:
        sq[-2], sq[-1] = sq[-1], sq[-2]

    return sq

def draw_square():
    text = turtle.Turtle()
    text.hideturtle()
    text.color('black')
    text.speed(3)
    text.up()

    block = turtle.Turtle()
    block.shape('square')
    block.color('light blue')
    block.shapesize(4)
    block.speed(3)
    block.up()

    return block, text


"""
step_5:
generate the puzzle 
"""
def generate_puzzle(size, total, space, sequence): # space =  10
    void = sequence.index(0)
    lar = space + 80 # 90
    block_list, text_list, number_list = [], [], []
    x, y = -(size//2 + 0.5) * 80 + size//2 + space, -size * lar + (size//2) * 80 + size//2 * space
    turtle.tracer(0)
    for serial in range(total):
        b, t = draw_square()
        cy = size - serial // size
        cx = (serial) % size
        b.goto(x + cx*lar, y + cy * lar)
        t.goto(x + cx*lar - 10 , y + cy * lar-19)
        block_list.append(b)
        text_list.append(t)
    block_list[void].hideturtle()
    turtle.tracer(1)
    for i in range(len(text_list)):
        if sequence[i] == 0:
            pass
        else:
            text_list[i].write(sequence[i],font=('Arial',20,'normal'))
        number_list.append(sequence[i])
    return block_list,text_list,number_list
###

"""
step_6:
click the square to move it
"""
#"""
def click(x, y):
    global block_list, text_list, number_list, size, space, total
    if not checkpoint(number_list, total):

        ty_0 = number_list.index(0)
        row, col = (ty_0) % size + 1, (ty_0) // size + 1
        for u in block_list:
            if u.distance(x, y) < 40 + space:
                next = block_list.index(u)
                row_new, col_new = (next) % size + 1, (next) // size + 1
                
                if (col_new - col) * (row_new - row) == 0 \
                    and (col_new - col)+(row_new - row) != 0 \
                        and (col_new - col == 1 or row_new - row == 1 or col_new - col == -1 or row_new - row == -1):
                    x0,y0 = block_list[ty_0].position()
                    x1,y1 = block_list[next].position()

                    text_list[next].clear()
                    text_list[next].goto(x0 - 10, y0 - 19)
                    text_list[ty_0].goto(x1 - 10, y1 - 19)

                    block_list[next].goto(x0,y0)
                    block_list[ty_0].goto(x1,y1)

                    text_list[next].write(number_list[next], font=('Arial', 20, 'normal'))

                    a_b = block_list[ty_0]
                    a_n = text_list[ty_0]

                    block_list[ty_0] = block_list[next]
                    block_list[next] = a_b

                    text_list[ty_0] = text_list[next]
                    text_list[next] = a_n

                    number_list[ty_0] = number_list[next]
                    number_list[next] = 0

                if checkpoint(number_list, size):
                    endgame(block_list,text_list,number_list)
                    turtle.bye()
    else:
      endgame(block_list, text_list, number_list)
      turtle.bye()
###
#"""

"""
step_7:
prepare the endgame() to chamge the color
prepare the checkpoint() to check if the puzzle is finished
"""
def checkpoint(number_list, total):
    if number_list == [i for i in range(1, total)] + [0]:
        return True
    else:
        return False

def endgame(block_list, text_list, number_list):
    turtle.tracer(0)
    for i in block_list:
        i.color('red')    
    turtle.update()
    
    for num in range(len(text_list)):
        if number_list[num] != 0:
            text_list[num].write(number_list[num], font = ('Arial', 20 , 'normal'))
    #turtle.update()
    turtle.done()
###

"""
step_8:
encode the main() function
"""
space = 10
'''
def main():
    s, t = get_size()
    sq = solvable_judge(t)
    block_list, text_list, number_list = generate_puzzle(s, t, space, sq)
    # global block_list, text_list, number_list, size, space
    turtle.onscreenclick(click)
    turtle.mainloop()
###
    
main()
'''
size, total = get_size()
sq = solvable_sequence(total)
block_list, text_list, number_list = generate_puzzle(size, total, space, sq)
turtle.onscreenclick(click)
turtle.mainloop()