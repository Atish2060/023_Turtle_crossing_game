from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def inc_level(self):
        self.score += 1
        self.clear()
        self.goto(-280, 260)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write(f"GAME OVER!!", align="left", font=FONT)






