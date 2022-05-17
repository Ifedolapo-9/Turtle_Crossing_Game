
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.gen_random()
    cars.move()
    for car in cars.car_list:
        # To detect Collision
        if car.distance(player) < 20:
            score.over()
            game_is_on = False

    # After crossing successfully
    if player.restart():
        cars.faster()
        score.increase()



screen.exitonclick()
