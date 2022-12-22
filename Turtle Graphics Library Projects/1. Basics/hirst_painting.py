# import colorgram
# colors = colorgram.extract('image.jpg', 20)
# print(colors)
# pallete = []
# for i in colors:
#     rgb = i.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_tuple = (r, g, b)
#     pallete.append(color_tuple)
#
# print(pallete)

from turtle import Turtle, Screen
import random

color_list = [(141, 176, 206), (25, 32, 48), (28, 105, 156), (208, 161, 112), (238, 222, 234), (230, 211, 94),
              (131, 31, 64),
              (5, 162, 195), (182, 45, 84), (217, 60, 85), (226, 80, 44), (195, 129, 168), (54, 167, 116),
              (29, 61, 115),
              (108, 181, 91), (109, 99, 88), (2, 102, 119)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
pos = 0
tim.hideturtle()
for i in range(10):
    tim.home()
    tim.sety(pos)
    pos += 50

    for j in range(10):
        tim.pendown()
        tim.dot(10, random.choice(color_list))
        tim.penup()
        tim.fd(50)

screen.exitonclick()
