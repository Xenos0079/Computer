# import modules
import turtle
import random
from functools import partial
import time

# define the Global variables
g_screen = None
g_head , g_tail = None , 5 # the head of the snake and the size of the snake's tail
g_head_positions = [] # a list to record the positions of the head
g_postion_set = [] # record every random position for foods and monsters to prevent the same position appears
g_monsters = None
g_intro = None
g_status = None 
g_key_pressed = None
count = 0 # initialize the counter
to_stop = False # the pointer to show if the game should be ended
win = False # the pointer to show if the player win the game

# Constants
NUM_FOOD = 5 # 
NUM_MONSTER = 4 # 

COLOR_BODY = ("blue" , "grey")
COLOR_HEAD = "orange"
COLOR_MONSTER = "cyan"

FONT_INTRO = ("Arial" , 20 , "normal")
FONT_STATUS = ("Arial" , 20 , "normal")
FONT_FOOD = ("Arial" , 16 , "normal") #
FONT_END = ("Arial" , 50 , "bold") # 

TIMER_SNAKE = 300   # refresh rate for snake  ###
TIMER_MONSTER = 1000 # refresh rate for monster  ###
TIMER_FOOD = 5000   # refresh rate for food  ###

SZ_SQUARE = 20      # square size

DIM_PLAY_AREA = 500 ###
DIM_STAT_AREA = 60 ###
DIM_MARGIN = 30 ###

KEY_UP , KEY_DOWN , KEY_LEFT , KEY_RIGHT , KEY_SPACE = "Up" , "Down" , "Left" , "Right" , "space"
HEADING_BY_KEY = {KEY_UP: 90 , KEY_DOWN: 270 , KEY_LEFT: 180 , KEY_RIGHT: 0 , KEY_SPACE: 0}

def create_turtle(x , y , color = "orange" , mb = "black"):
    '''
    Creates a new turtle object with the specified position , color , and mb / motion_border
    '''
    t = turtle.Turtle("square")
    t.color(mb , color)
    t.up()
    t.goto(x , y)

    return t

def configure_play_area():
    '''
    Configure the play area for the snake game
    '''
    # drawing the motion_border of the play area and motion_border of states_area at the top
    # mb / st / s / w / h = motion_border / states_area / size / weight / height
    mb , st = create_turtle(0 , 0 , "" , "black")  , create_turtle(0 , 0 , "" , "black")
    mb_s , st_w , st_h = DIM_PLAY_AREA // SZ_SQUARE  , DIM_STAT_AREA // SZ_SQUARE  , DIM_PLAY_AREA // SZ_SQUARE
    mb.shapesize(mb_s , mb_s , 3)
    st.shapesize(st_w , st_h , 3)
    mb.goto(0 , 0) # shift down half the status
    st.goto(0 , DIM_PLAY_AREA // 2 + DIM_STAT_AREA // 2)  # shift up half the motion

    # create a turtle to write introduction and another turtle to write status
    # it_w stands for intro_writer and st stands for status and w stands for writer
    it_w , st_w = create_turtle(-200 , 0)  , create_turtle(0,0)
    it_w.hideturtle()
    st_w.hideturtle()
    it_w.write("Click anywhere to start the game\n\n" + "Use arrow keys to control the snake.\n\n" ,  \
                font = FONT_INTRO)
    st_w.goto(0 , st.ycor() - DIM_STAT_AREA // 3)

    return it_w , st_w

def configure_screen():
    '''
    Configure the screen
    '''
    # sc / h / w stands for the screen / height / width
    sc = turtle.Screen() # initialize the screen
    sc.tracer(0) # disable auto screen refresher , [ 0 = disable , 1 = enable ]
    sc.title("Snake by TianCheng")
    sc_w , sc_h = DIM_PLAY_AREA + DIM_MARGIN * 2  , DIM_PLAY_AREA + DIM_MARGIN * 2 + DIM_STAT_AREA * 2  , 
    sc.setup(sc_w , sc_h)
    sc.mode("standard") # create a standard screen

    return sc

def update_status():
    '''
    Update the status display on the screen with the current key press and snake tail length.
    '''
    g_status.clear()
    if g_key_pressed == KEY_SPACE:
        move = 'Paused'
    else:
        move = g_key_pressed
    st = f'Contact: {count}    Time: {int(time.time() - start_time)}     Motion: {move}'
    g_status.write(st , font = FONT_STATUS , align = "center")
    g_screen.update()

def on_arrow_key_pressed(key):
    '''
    Event handler for arrow key press events.
    '''
    global g_key_pressed  , g_pressed_history
    g_key_pressed = key
    if len(g_pressed_history) > 1:
        g_pressed_history.pop(0)
    g_pressed_history.append(key)
    update_status()

def out_of_bound(x , y):
    edge = DIM_PLAY_AREA // 2 - SZ_SQUARE

    return abs(x) >= abs(edge) or abs(y) >= abs(edge)

def random_position():
    '''
    create a set of (x , y) coordinates to initialize foods and monsters
    '''
    global g_postion_set
    x = random.randint(-DIM_PLAY_AREA // 2 + 15 , DIM_PLAY_AREA // 2 - 15)
    y = random.randint(-DIM_PLAY_AREA // 2 + 15 , DIM_PLAY_AREA // 2 - 15)
    x  , y = x - x % SZ_SQUARE  , y - y % SZ_SQUARE
    if out_of_bound(x , y) or [x  , y] in g_postion_set or  (x ** 2 + y ** 2) < 100:
        return random_position()
    g_postion_set.append([x  , y])
    return (x , y)

def skip():
    '''
    check if the following process should be skipped
    '''
    global to_stop
    if to_stop: # game has ended
        return True
    return False

def on_timer_snake():
    '''
    Advances the snake's movement on a timer.
    '''
    if skip():
        return
    global g_head_positions
    if g_key_pressed is None or g_key_pressed == KEY_SPACE: # snake should standing still
        check_collision()
        update_status()
        g_screen.update()
        g_screen.ontimer(on_timer_snake , TIMER_SNAKE)
        return
    # snake is moving
    g_head.color(*COLOR_BODY) # 1/ change color (old head -> body_color)
    g_head.stamp() # 2/ ready to clone
    g_head.color(COLOR_HEAD) # 3/ (change the old head color to head_color)
    g_head.setheading(HEADING_BY_KEY[g_key_pressed]) # 4/ get the position
    g_head.forward(SZ_SQUARE) # 5/ move the head
    new_head_pos = g_head.position() # 6/ get new position of the head
    g_head_positions.append(new_head_pos) # 7/ relocate the head
    if len(g_head.stampItems) > g_tail: # 8/ which means tail need to be cut
        g_head.clearstamps(1) # 9/ cut tail by one block
        g_head_positions.pop(0) # 10/ remove the cutter block
    check_collision()
    update_status() # 1/
    g_screen.update() # 2/
    g_screen.ontimer(on_timer_snake , TIMER_SNAKE) # 3/ 
    # 1,2 and 3 cannot use chaotic since the snake must move instanly when the keypress occurs

def chaotic_case(t_obj , ott):
    '''
    arg: t_obj , ott = TIMER_OBJECT , on_timer_object
    add randomness to the time of the move
    '''
    g_screen.update()
    delay = random.randint(t_obj - 15 , t_obj + 15)
    g_screen.ontimer(ott , delay) 

def on_timer_monster():
    '''
    Advances the monster's movement based on the timer
    '''
    if skip():
        return
    global count
    if g_key_pressed is None:
        g_screen.ontimer(on_timer_monster , TIMER_SNAKE)
        return
    for monster in g_monsters:
        ang = monster.towards(g_head) # get the relative position
        qtr = ang // 90 # delimit the coordinate quadrant
        ori = qtr * 90 # ori = orientation

        monster.setheading(ori) # set the heading orientation
        monster.forward(random.randint(SZ_SQUARE , SZ_SQUARE * 2)) # set the moving distance
    chaotic_case(TIMER_MONSTER , on_timer_monster)

def on_timer_food():
    '''
    Advances the food items on the screen on a timer.
    '''
    if skip():
        return
    if g_key_pressed is None: # no input
        g_screen.ontimer(on_timer_food , TIMER_SNAKE)
        return
    for food in g_foods:
        food , i = food # decomposite the food , give it a label
        x = random.choice([-SZ_SQUARE , 0 , SZ_SQUARE]) + food.xcor()
        y = random.choice([-SZ_SQUARE , 0 , SZ_SQUARE]) + food.ycor()
        # initialize the postition that food would move to
        if out_of_bound(x , y):
            continue
        food.goto(x , y) # 1/ refresh the new location
        food.clear() # 2/ clear the previous food
        food.penup() # 3/ disable the pen
        # below are the integer writing process , the data int 14 is from a discussion.
        food.sety(food.ycor() - 14)  # 1/ move the position to let the integer could be written in the center
        food.write(str(i) , align = "center" , font = FONT_FOOD) # 2/ write the food
        food.sety(food.ycor() + 14)  # 3/ move the real postition back to the initial position
    chaotic_case(TIMER_FOOD  , on_timer_food)

def check_collision():
    '''
    Check if the snake has collided with the monster or itself.
    '''
    global count , g_key_pressed , g_head_positions , g_tail, win
    for monster in g_monsters:
        #head-monster collision
        if g_head.distance(monster) < SZ_SQUARE:
            endgame()
        #body-monster collision
        if any(monster.distance(pos)<SZ_SQUARE for pos in g_head_positions):
            count += 1
            update_status()
    #head-edge collision
    cor_edge = DIM_PLAY_AREA//2 - SZ_SQUARE
    if abs(g_head.xcor()) >= cor_edge or abs(g_head.ycor()) >= cor_edge:
        g_key_pressed = KEY_SPACE
        update_status()
    #head-food collision
    for food , i in g_foods:
        if g_head.distance(food) < SZ_SQUARE:
            g_foods.remove((food , i))
            g_tail += i
            if len(g_foods) == 0:
                win = True
                endgame()
            update_status()
            food.clear()
            food.hideturtle()

def endgame():
    '''
    Stops the game and displays the  message
    '''
    global to_stop, win
    to_stop = True
    if win == True:
        message = 'YOU WIN'
    else:
        message = 'GAME OVER'
    for press in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE]:
        g_screen.onkey(None, press)
    g_intro.goto(0,0)
    g_intro.clear()
    g_intro.write(message, font = FONT_END , align = "center")
    g_screen.update()


def cb_start_game(x ,y):
    '''
    Starts the game by setting up the initial game state and event handlers.  
    This function is called when the user clicks on the screen to start the game.
    '''
    global start_time
    start_time = time.time()
    g_screen.onscreenclick(None)
    g_intro.clear()

    for key in [KEY_UP , KEY_DOWN , KEY_LEFT , KEY_RIGHT , KEY_SPACE]:
        g_screen.onkey(partial(on_arrow_key_pressed,key) , key)

    on_timer_snake()
    on_timer_monster()
    on_timer_food()

def create_food():
    '''
    Creates the specified number of food items on the screen.
    '''
    g_foods = []
    for i in range(1 , NUM_FOOD + 1):
        x , y = random_position()
        t = create_turtle(x , y , "" , "black")
        t.hideturtle()
        food = (t , i)
        g_foods.append(food)
    return g_foods

def create_monster():
    g_monsters = []
    for _ in range(NUM_MONSTER):
        x , y = random_position()
        monster = create_turtle(x , y , COLOR_MONSTER , "black")
        g_monsters.append(monster)
    return g_monsters

def main():
    '''
    Main function for the snake game.
    '''
    global start_time , g_screen , g_intro , g_status , g_monsters , g_head , g_foods
    start_time = time.time()
    g_screen = configure_screen()
    g_intro , g_status = configure_play_area()

    update_status()

    g_head = create_turtle(0 , 0 , COLOR_HEAD , "black")
    g_monsters = create_monster()
    g_foods = create_food()
    g_screen.onscreenclick(cb_start_game) # set up a mouse-click call back
    g_screen.update()
    g_screen.listen()
    g_screen.mainloop()

if __name__ == "__main__": # start the operation
    main()