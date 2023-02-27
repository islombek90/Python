from turtle import Screen
import time
from cars import Cars
from race_turtle import RaceTurtle
from score_board import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

turtle = RaceTurtle()
cars = Cars()
score = Score()
screen.onkey(turtle.move, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.create_random_cars()
    cars.move()
    score.write_level()
    if turtle.ycor() > 280:
        turtle.reset()
        cars.level_increase()
        score.score_increase()
        score.highest_score_record()

    for car in cars.new_cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False



screen.exitonclick()
