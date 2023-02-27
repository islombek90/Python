from turtle import Turtle
STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
SNAKE_SIZE = 0.5
MOVING_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for seg in STARTING_POSITION:
            new_seg = Turtle(shape="square")
            new_seg.shapesize(stretch_len=0.5, stretch_wid=0.5)
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(seg)
            self.segments.append(new_seg)

    def extend_snake(self):

        new_seg = Turtle(shape="square")
        new_seg.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_seg.color("white")

        new_seg.penup()

        new_seg.goto(self.segments[-1].position())
        self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
