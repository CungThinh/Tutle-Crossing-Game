from random import random
from turtle import Turtle, Screen
import random

Colors = ["red", "green", "blue", "purple"]


class CarManager:
    cars = []

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(Colors))
            self.cars.append(new_car)
            new_car.goto(x=300, y=random.randint(-220, 220))

    def move_cars(self, speed):
        for car in self.cars:
            car.backward(speed)



