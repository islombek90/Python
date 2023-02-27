from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.score_left = 0
        self.score_right = 0

    def score_update(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-100, 250)
        self.write(f"{self.score_left}", font=("Arial", 20, "normal"))
        self.goto(100, 250)
        self.write(f"{self.score_right}", font=("Arial", 20, "normal"))

    def score_increase_left(self):
        self.score_left += 1

    def score_increase_right(self):
        self.score_right += 1


