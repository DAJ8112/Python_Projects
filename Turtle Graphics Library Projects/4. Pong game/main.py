from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(p1.go_up, "Up")
screen.onkeypress(p1.go_down, "Down")
screen.onkeypress(p2.go_up, "w")
screen.onkeypress(p2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
