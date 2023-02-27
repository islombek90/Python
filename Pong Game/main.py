from turtle import Screen

from ball import Ball
from padles import Paddles
from score_board import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball((0, 0))
game_is_on = True
score = Score()


while game_is_on:

    time.sleep(0.05)
    screen.update()
    ball.move()
    score.score_update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    if ball.xcor() < -380:
        score.score_increase_left()
        print("ball is out")
        ball.reset()
    if ball.xcor() > 380:
        score.score_increase_right()
        print("ball is out")
        ball.reset()

screen.exitonclick()
