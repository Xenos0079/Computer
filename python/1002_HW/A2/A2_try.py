from turtle import Screen, Turtle
from functools import partial
from random import random

SIZE = 5
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

screen = Screen()

matrix = [[None for _ in range(SIZE)] for _ in range(SIZE)]

offset = TILE_SIZE * 1.5

for row in range(SIZE):
    for col in range(SIZE):
        if row == SIZE - 1 == col:
            break

        tile = Turtle('square', visible=False)
        tile.shapesize(TILE_SIZE / CURSOR_SIZE)
        tile.fillcolor(random(), random(), random())
        #tile.fillcolor(random())
        # ERROR
        tile.penup()
        tile.goto(col * TILE_SIZE - offset, offset - row * TILE_SIZE)
        tile.onclick(partial(slide, tile, row, col))
        tile.showturtle()

        matrix[row][col] = tile

screen.mainloop()