from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Saap thi sali")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "up")
screen.onkey(snake.down, "down")
# screen.onkey(snake.left, "left")
# screen.onkey(snake.right, "right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()

