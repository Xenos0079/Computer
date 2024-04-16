#from turtle import Screen, Turtle
from functools import partial
#from random import random

import turtle
import random


### 
def get_size():
    size = 0

    while size not in [3,4,5]:
        size=int(turtle.numinput('Sliding Puzzle GUI - 123090401','You need to enter 3 4 or 5 for the size of the board'))

        total = size ** 2

    return size, total

def solvable_sequence(n):
    sq = list(range(n))
    random.shuffle(sq)
    if sum(1 for i in range(n-1) for j in range(i+1, n) if sq[i] > sq[j]) % 2 != 0:
        sq[-2], sq[-1] = sq[-1], sq[-2]
###


SIZE, TOTAL = get_size()
sequence = solvable_sequence(TOTAL)
TILE_SIZE = 100
OFFSETS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

CURSOR_SIZE = 20

def slide(tile, row, col, x, y):
    tile.onclick(None)  # disable handler inside handler

    for dy, dx in OFFSETS:
        try:
            if row + dy >= 0 <= col + dx and matrix[row + dy][col + dx] is None:
                matrix[row][col] = None
                row, col = row + dy, col + dx
                matrix[row][col] = tile
                x, y = tile.position()
                tile.setposition(x + dx * TILE_SIZE, y - dy * TILE_SIZE)
                break
        except IndexError:
            pass

    tile.onclick(partial(slide, tile, row, col))

screen = turtle.Screen()

matrix = [[None for _ in range(SIZE)] for _ in range(SIZE)]

offset = TILE_SIZE * 1.5

for row in range(SIZE):
    for col in range(SIZE):
        if row == SIZE - 1 == col:
            break

        tile = turtle.Turtle('square', visible=False)
        tile.shapesize(TILE_SIZE / CURSOR_SIZE)
        tile.fillcolor(173/255, 216/255, 230/255)
        # tile.fillcolor(random())
        # ERROR
        tile.penup()
        tile.goto(col * TILE_SIZE - offset, offset - row * TILE_SIZE)
        tile.onclick(partial(slide, tile, row, col))
        tile.showturtle()

        matrix[row][col] = tile

screen.mainloop()