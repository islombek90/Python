from turtle import  Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write("Score: 0")

    def increase_score(self):
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.score+=1
        self.write(f"Score {self.score}")

    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -270)
        self.write("Game Over")


