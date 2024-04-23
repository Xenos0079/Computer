import turtle
import random
from functools import partial

# 设置窗口大小
WIDTH, HEIGHT = 600, 600
turtle.setup(WIDTH, HEIGHT)
turtle.title("贪吃蛇")

# 设置边界
BOUNDARY = WIDTH // 2 - 10

# 设置食物大小
FOOD_SIZE = 20

# 初始化游戏速度
SPEED = 0.1

# 初始化游戏得分
SCORE = 0

# 初始化贪吃蛇的坐标
snake = [(0, 0)]

# 初始化食物的坐标
food_pos = (random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

# 设置蛇的方向
direction = 'right'

# 创建turtle对象
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  # 关闭动画

# 画蛇的函数
def draw_snake(snake):
    turtle.clearstamps()
    for segment in snake:
        turtle.goto(segment)
        turtle.stamp()

# 移动蛇的函数
def move_snake():
    global direction, SCORE
    x, y = snake[0]
    if direction == 'up':
        y += 20
    elif direction == 'down':
        y -= 20
    elif direction == 'left':
        x -= 20
    elif direction == 'right':
        x += 20

    # 检查是否吃到食物
    if (x, y) == food_pos:
        SCORE += 10
        generate_food()
    else:
        # 移动蛇的身体
        snake.pop()

    # 检查是否撞墙
    if abs(x) >= BOUNDARY or abs(y) >= BOUNDARY:
        screen.bye()
        print("游戏结束！得分：", SCORE)
        return

    # 检查是否撞到自己
    if (x, y) in snake:
        screen.bye()
        print("游戏结束！得分：", SCORE)
        return

    snake.insert(0, (x, y))
    draw_snake(snake)
    screen.update()
    screen.ontimer(move_snake, int(SPEED * 1000))

# 生成食物的函数
def generate_food():
    global food_pos
    food_pos = (random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
    turtle.goto(food_pos)
    turtle.dot(FOOD_SIZE, "red")

# 改变蛇的方向
def change_direction(new_direction):
    global direction
    if (new_direction == 'up' and direction != 'down') or \
       (new_direction == 'down' and direction != 'up') or \
       (new_direction == 'left' and direction != 'right') or \
       (new_direction == 'right' and direction != 'left'):
        direction = new_direction

# 设置键盘监听事件
screen.listen()
screen.onkey(partial(change_direction, 'up'), 'Up')
screen.onkey(partial(change_direction, 'down'), 'Down')
screen.onkey(partial(change_direction, 'left'), 'Left')
screen.onkey(partial(change_direction, 'right'), 'Right')

# 初始化游戏
draw_snake(snake)
generate_food()
move_snake()

# 显示窗口
screen.mainloop()
