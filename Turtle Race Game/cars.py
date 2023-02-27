from turtle import Turtle
import random
COLORS = ["red", "green", "blue", "black", "purple"]


class Cars:
    def __init__(self):

        self.new_cars = []
        self.car_speed = 10

    def move(self):
        for car in self.new_cars:
            car.backward(self.car_speed)

    def create_random_cars(self):
        random_number = random.randint(1, 5)
        if random_number == 1:
            car = Turtle("square")
            car.penup()
            car.goto(300, random.randint(-220, 220))
            car.shapesize(1, 3)
            car.color(random.choice(COLORS))
            self.new_cars.append(car)

    def level_increase(self):
        self.car_speed += 10

