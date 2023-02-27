from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.level = 0
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()

    def write_level(self):

        self.clear()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.write(f"Level: {self.level}", font=("Arial", 10, "bold"))
        self.goto(100, 250)
        self.color("black")
        self.write(f"Highest score: {self.high_score}", font=("Arial", 10, "bold"))
        self.goto(-50, 250)
        self.color("black")
        self.write(f" score: {self.score}", font=("Arial", 10, "bold"))

    def score_increase(self):
        self.score += 1
        self.level += 1

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER")

    def highest_score_record(self):
        with open("data.txt", mode="w") as data_store:
            data_store.write(f"{self.high_score}")
            if self.score > self.high_score:
                self.high_score = self.score
