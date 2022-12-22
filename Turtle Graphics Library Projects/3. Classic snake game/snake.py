from turtle import Turtle
MOVE_DISTANCE = 20  # It's a constant hence written in all caps .
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.seg.append(snake)

    def move(self):
        for seg_num in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[seg_num - 1].xcor()
            new_y = self.seg[seg_num - 1].ycor()
            self.seg[seg_num].goto(new_x, new_y)
            self.seg[0].forward(MOVE_DISTANCE)

    def up(self):
        self.seg[0].setheading(90)

    def down(self):
        pass

    def right(self):
        pass