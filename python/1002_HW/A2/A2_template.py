import turtle
import random


def create_square():

    sz=4
    t_1=turtle.Turtle()
    t_1.hideturtle()
    t_1.color('blue')
    t=turtle.Turtle('square')
    t.color('light green')
    t.shapesize(sz,sz)
    t.speed(2)
    t.up()
    t_1.up()
    t_1.speed(2)
    b,n=t,t_1
    return b,n

def is_solvable(number_list):

    n = int(len(number_list) ** 0.5)  
    inversions = 0
    for i in range(n * n - 1):
        for j in range(i + 1, n * n):
            if number_list[i] > number_list[j] and number_list[i] != 0 and number_list[j] != 0:
                inversions += 1

    empty_row = n - (number_list.index(0) // n) 
    if n % 2 == 1:  
        return inversions % 2 == 0
    else:  
        if empty_row % 2 == 0: 
            return inversions % 2 == 1
        else:
            return inversions % 2 == 0


def create_game(dim,space):

    j=0
    while j==0:
        num=random.sample(range(0,dim*dim),dim*dim)
        if is_solvable(num):
            j=1
    empty=num.index(0)
    sz=space+80
    b_g=[]
    n_g=[]
    number_list=[]
    y=-dim*sz+(dim//2)*80+dim//2*space
    x=-(dim//2+0.5)*80+dim//2+space
    turtle.tracer(0)
    for _ in range(dim*dim):
        b,n=create_square()
        cy=dim-_//dim
        cx=(_)%dim
        b.goto(x+cx*sz,y+cy*sz)
        n.goto(x+cx*sz-10,y+cy*sz-19)
        b_g.append(b)
        n_g.append(n)
    b_g[empty].hideturtle()
    turtle.tracer(1)
    for i in range(len(n_g)):
        if num[i]==0:
            pass
        else:
            n_g[i].write(num[i],font=('Arial',20,'normal'))
        number_list.append(num[i])
    #turtle.done()
    return b_g,n_g,number_list


def check_game(number_list,dim):

    key=[i for i in range(1,dim*dim)]+[0]
    if number_list==key:
        return 1
    else:
        return 0


def change_color(b_g,n_g,number_list):

    turtle.tracer(0)
    #turtle.clear()
    for i in b_g:
        i.color('red')    
    turtle.update()
    for i in range(len(n_g)):
        if number_list[i]!=0:
            n_g[i].write(number_list[i],font=('Arial',20,'normal'))
    turtle.done()


def touch(x,y):

    global b_g,n_g,number_list,dim,space
    if check_game(number_list,dim)!=1:
        ty_0=number_list.index(0)
        ty_0=number_list.index(0)
        col=(ty_0)%dim+1
        row=(ty_0)//dim+1
        for u in b_g:

            if u.distance(x,y)<40+space:
                next=b_g.index(u)
                
                col_new=(next)%dim+1
                row_new=(next)//dim+1
                
                if (col_new-col)*(row_new-row)==0 \
                    and (col_new-col)+(row_new-row)!=0 \
                        and (col_new-col==1 or row_new-row==1 or col_new-col==-1 or row_new-row==-1):
                    x0,y0=b_g[ty_0].position()
                    x1,y1=b_g[next].position()
                    n_g[next].clear()
                    n_g[next].goto(x0-10,y0-19)
                    n_g[ty_0].goto(x1-10,y1-19)
                    b_g[next].goto(x0,y0)
                    b_g[ty_0].goto(x1,y1)
                    n_g[next].write(number_list[next],font=('Arial',20,'normal'))
                    a_b=b_g[ty_0]
                    a_n=n_g[ty_0]
                    b_g[ty_0]=b_g[next]
                    b_g[next]=a_b
                    n_g[ty_0]=n_g[next]
                    n_g[next]=a_n
                    number_list[ty_0]=number_list[next]
                    number_list[next]=0
                if check_game(number_list,dim)==1:
                    change_color(b_g,n_g,number_list)
                    turtle.bye()
    else:
      change_color(b_g,n_g,number_list)
      turtle.bye()

dim=int(turtle.numinput('Square Puzzle','Puzzle Size'))
#the dimension of the game

space=10
#the distance between to blocks

while dim not in [3,4,5]:
    dim=int(turtle.numinput('Square Puzzle','Enter 3 4 or 5!'))
b_g,n_g,number_list=create_game(dim,space)
turtle.onscreenclick(touch)
turtle.mainloop()