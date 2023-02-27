from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(position)
        self.ymove = 10
        self.xmove = 10

    def move(self):
        newx = self.xcor()+self.xmove
        newy = self.ycor()+self.ymove
        self.goto(newx, newy)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def reset(self):
        self.goto(0, 0)
        self.ymove *= -1



