from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.speed("fastest")


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def resett():

    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# when using higher order functions it's a
# good practice to use keyword arguments instead of positional arguments

screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=resett)
screen.exitonclick()
