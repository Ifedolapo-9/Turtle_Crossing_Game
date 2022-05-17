from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def gen_random(self):
        no = random.randint(1,6)
        if no == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.turtlesize(stretch_wid=0.5, stretch_len=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    #  Get car to move faster
    def faster(self):
        self.car_speed += 10
        for car in self.car_list:
            car.forward (self.car_speed)














