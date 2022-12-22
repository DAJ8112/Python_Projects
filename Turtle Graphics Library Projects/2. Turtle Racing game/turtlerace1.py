from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y)
    y += 30

# tom = Turtle(shape="turtle")
# tom.color("orange")
# tom.penup()
# tom.goto(x=-230, y=-70)
#
# tam = Turtle(shape="turtle")
# tam.color("yellow")
# tam.penup()
# tam.goto(x=-230, y=-40)
#
# tum = Turtle(shape="turtle")
# tum.color("green")
# tum.penup()
# tum.goto(x=-230, y=-10)
#
# tem = Turtle(shape="turtle")
# tem.color("blue")
# tem.penup()
# tem.goto(x=-230, y=20)
#
# tmm = Turtle(shape="turtle")
# tmm.color("purple")
# tmm.penup()
# tmm.goto(x=-230, y=50)

screen.exitonclick()
