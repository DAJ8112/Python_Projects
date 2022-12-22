from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()


def draw_shapes(num_sides):
    for j in range(num_sides):
        tim.forward(100)
        tim.left(360/num_sides)


for i in range(3, 11):
    screen.colormode(255)
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    tim.pencolor((a, b, c))
    draw_shapes(i)












screen = Screen()
screen.exitonclick()