from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.speed("fastest")

x = 3
for i in range(120):
    tim.color(random_color())
    tim.circle(150)
    tim.setheading(x)
    x += 3


screen.exitonclick()
