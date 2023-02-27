import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My First snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    point = 0
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        print("game over you hit the wall")
        score.game_over()
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 5:
            game_is_on = False
            print("you hit your tail")
            score.game_over()

    if snake.head.distance(food) < 10:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

screen.exitonclick()
