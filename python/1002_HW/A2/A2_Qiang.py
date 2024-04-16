import turtle
import random

# 初始化基本游戏设置
tile_size = 80  # 每个瓷砖的大小
gap_size = 2  # 瓷砖之间的间隙大小
grid_size = 3  # 默认网格大小，玩家选择后会更新
empty_space = None  # 初始化空白位置，将在游戏开始时确定
tiles = []

# 瓷砖的默认和完成时的颜色
default_tile_color = 'lightblue'  # 默认瓷砖颜色
solved_tile_color = 'red'  # 游戏解决时的瓷砖颜色
number_color = 'darkblue'  # 数字颜色
game_solved = False  # 游戏是否已解决


def initialize_game():
    global grid_size, empty_space, tiles, game_solved
    game_solved = False
    empty_space = (grid_size - 1, grid_size - 1)
    tiles = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    shuffle_tiles()
    draw_puzzle()


def choose_grid_size():
    global grid_size
    size = turtle.numinput("选择大小", "请输入拼图的大小 (3, 4, 5):", default=3, minval=3, maxval=5)
    if size is not None:  # 确保玩家做出了选择
        grid_size = int(size)
        initialize_game()


def shuffle_tiles():
    numbers = list(range(1, grid_size * grid_size))
    random.shuffle(numbers)
    numbers.append(None)  # None代表空白位置
    for i in range(grid_size):
        for j in range(grid_size):
            tiles[i][j] = numbers.pop(0)


def draw_puzzle():
    turtle.clear()
    for row in range(grid_size):
        for col in range(grid_size):
            if tiles[row][col] is not None:
                draw_tile(row, col, tiles[row][col])
    turtle.update()


def draw_tile(row, col, number):
    # 计算瓷砖中心的坐标
    x_center = col * (tile_size + gap_size) + gap_size / 2 - (grid_size * tile_size / 2) + tile_size / 2
    y_center = (grid_size * tile_size / 2) - row * (tile_size + gap_size) - gap_size / 2 - tile_size / 2

    # 绘制瓷砖
    turtle.penup()
    turtle.goto(x_center - tile_size / 2, y_center + tile_size / 2)
    turtle.color(default_tile_color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(tile_size - gap_size)
        turtle.right(90)
    turtle.end_fill()

    # 在瓷砖中心写上数字
    turtle.penup()
    font_size = 20  # 假定的字体大小
    # 将Turtle定位到瓷砖中心稍上一点的位置，以使文本垂直居中
    turtle.goto(x_center, y_center - font_size / 2)  # 根据字体大小调整Y坐标
    turtle. turtle.color(number_color)
    turtle.write(str(number), align="center", font=("Arial", font_size, "normal"))


def move_tile(x, y):
    global empty_space, game_solved
    if game_solved:
        return
    row, col = get_tile_row_col(x, y)
    if (row, col) != empty_space and (row, col) in adjacent_tiles(*empty_space):
        tiles[empty_space[0]][empty_space[1]], tiles[row][col] = tiles[row][col], None
        empty_space = (row, col)
        draw_puzzle()
        if is_solved():
            game_solved = True
            draw_puzzle()
            print("恭喜，拼图完成！")


def get_tile_row_col(x, y):
    col = int((x + (grid_size * (tile_size + gap_size) / 2)) / (tile_size + gap_size))
    row = int(((grid_size * (tile_size + gap_size) / 2) - y) / (tile_size + gap_size))
    if 0 <= row < grid_size and 0 <= col < grid_size:
        return row, col
    return None, None


def adjacent_tiles(row, col):
    return [(row + dx, col + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if
            0 <= row + dx < grid_size and 0 <= col + dy < grid_size]


def is_solved():
    expected = 1
    for row in range(grid_size):
        for col in range(grid_size):
            if tiles[row][col] != expected:
                if row == grid_size - 1 and col == grid_size - 1 and tiles[row][col] is None:
                    return True
                return False
            expected += 1 if expected < grid_size * grid_size else None
    return True


def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)
    turtle.bgcolor("white")

    choose_grid_size()  # 允许玩家选择游戏大小
    turtle.onscreenclick(lambda x, y: move_tile(x, y))

    turtle.mainloop()


if __name__ == "__main__":
    main()