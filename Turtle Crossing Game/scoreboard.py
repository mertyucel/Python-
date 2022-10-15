from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.goto(-220, 270)
        self.write(f"LEVEL : {self.score}", align="center", font=FONT)

    def point_update(self):
        self.score += 1
        self.scoreboard_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=FONT)
