from turtle import Screen, Turtle
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake da game")

segments = []
y = -40
for i in range(3):
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.setposition(y, 0)
    segments.append(snake)
    y += 20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()
