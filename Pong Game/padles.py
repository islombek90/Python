from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(position)
        self.shapesize(5, 1)

    def move_up(self):
        newy = self.ycor() + 30
        self.goto(self.xcor(), newy)

    def move_down(self):
        newy = self.ycor() - 30
        self.goto(self.xcor(), newy)
