from turtle import colormode
import turtle as t
import time

t.setup(1600, 1080, 100, 100)
t.title("Happy")
t.hideturtle()
t.speed(0)


        



def s1(bgcolor):
    t.bgcolor(bgcolor)
    r,g,b = 255, 0, 0
    for i in range(255*2):
        colormode(255)

        if i < 255//3:
            g += 3
        elif i < (255*2)//3:
            r -= 3
        elif i < 255:
            b += 3
        elif i < (255*4)//3:
            g -= 3
        elif i < (255*5)//3:
            r += 3
        else:
            b -= 3
        t.forward(5+i)
        t.right(90.5)
        t.color(r,g,b)
    settings()


def s2(bgcolor,color,angle):
    t.bgcolor(bgcolor)
    x = 0
    
    while x < 600:
        t.color(color)
        t.forward(x)
        t.right(angle)
        x+=1
    settings()


        
def s4(angle, bgcolor, depth):
    if depth == 0:
        return

    t.bgcolor(bgcolor)
    a = angle  # in degrees
    for i in range(360 // a):
        for i in range(4):
            t.color('white')
            t.forward(300)
            t.right(90)
        t.left(a)


    s4(angle + 5, 'black' if depth % 2 == 0 else 'white', depth - 1)

    t.update()
    settings()


def s5(ang,bgcolor,color,sp):
    t.bgcolor(bgcolor)
    t.tracer(2,1)
    N = 5
    angle = ang

    tortues = []
    for position in range(N):
        t.speed(sp)
        look_at = 360/N*position
        new = t.Turtle()
        new.setheading(look_at)
        tortues.append(new)

    for radius in range(360):
        for my in tortues:
            t.speed(sp)
            my.pencolor(color)
            my.circle(radius*radius, angle)

    t.update()
    settings()



def settings():
    t.reset()
    t.hideturtle()
    t.speed(0)

def main():
    
    s1('black')
    s2('black','white',98)
    s2('black','white',110)
    s4(5, 'black', 1)
    s5(30,'black','white',40)
    t.mainloop()
main()



