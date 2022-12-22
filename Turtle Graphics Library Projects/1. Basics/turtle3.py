from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(7)
tim.fd(20)
screen.colormode(255)


def rand_pattern(index):
    tim.pensize(10)
    tim.speed('normal')
    x = random.randint(1, 255)
    y = random.randint(1, 255)
    z = random.randint(1, 255)
    tim.pencolor((x, y, z))
    if index == 1:
        tim.fd(30)
    elif index == 2:
        tim.bk(30)
    elif index == 3:
        tim.rt(90)
        tim.fd(30)
    elif index == 4:
        tim.lt(90)
        tim.fd(30)
    else:
        "Bruh"


for i in range(100):
    a = random.randint(1, 4)
    rand_pattern(a)


screen.exitonclick()
