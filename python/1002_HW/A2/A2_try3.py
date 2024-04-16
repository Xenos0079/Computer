import turtle
import random
from functools import partial

SIZE, TOTAL = 3, 9  # 默认为3x3的拼图

def get_size():
    size = int(turtle.numinput('Sliding Puzzle GUI', 'Enter 3, 4, or 5 for the size of the board', minval=3, maxval=5))
    return size, size**2

def solvable_sequence(n):
    sq = list(range(n))
    random.shuffle(sq)
    if sum(1 for i in range(n-1) for j in range(i+1, n) if sq[i] > sq[j]) % 2 != 0:
        sq[-2], sq[-1] = sq[-1], sq[-2]
    return sq

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
        tile.penup()
        tile.goto(col * TILE_SIZE - offset, offset - row * TILE_SIZE)
        tile.showturtle()

        # 修改点1：移动文本框的位置，使其在方块上方显示
        text_turtle = turtle.Turtle(visible=False)
        text_turtle.penup()
        text_turtle.goto(tile.xcor(), tile.ycor() - TILE_SIZE / 4)  # 调整文本框位置
        text_turtle.write(sequence[row * SIZE + col], align="center", font=("Arial", 20, "normal"))
        text_turtle.showturtle()

        tile.onclick(partial(slide, tile, row, col))

        matrix[row][col] = tile

screen.mainloop()
