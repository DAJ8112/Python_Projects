from turtle import Turtle, Screen
import heroes
tim = Turtle()
tim.shape("turtle")
tim.color("steel blue")

# draw a square
for i in range(4):
    tim.fd(100)
    tim.left(90)

# draw a dashed line
for i in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)



print(heroes.gen())









screen = Screen()
screen.exitonclick()
