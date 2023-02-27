from turtle import Turtle, Screen
import  random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
i = 0

is_race_on = False



for turtles in range (-120, 180, 50):
    print(colors[i])
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=turtles)
    i = i+1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        turtle_distance = random.randint(1, 10)
        if turtle.xcor() < 230:
            turtle.forward(turtle_distance)
        else:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You won, the turtle color is {turtle.pencolor()}")
            else:
                print(f"You Lost!, the turtle color is {turtle.pencolor()}")



screen.exitonclick()
