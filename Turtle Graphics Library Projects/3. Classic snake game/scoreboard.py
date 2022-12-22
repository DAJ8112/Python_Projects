from turtle import Turtle
FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("data.txt", "r+") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_count} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER ! ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", "r+") as data:
                data.write(f"{self.score_count}")
        self.score_count = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()
