import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import ScoreBoard
from player import Player
FINISH_LINE = 260

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
car_manager = CarManager()
level = ScoreBoard()
player = Player()
screen.listen()

screen.onkey(key='w', fun=player.move)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars((level.level * 10) + 10)

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    if player.ycor() >= FINISH_LINE:
        player.reset()
        time.sleep(1)
        level.increase_level()

screen.exitonclick()