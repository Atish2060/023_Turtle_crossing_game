from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.start = STARTING_MOVE_DISTANCE
        self.rand_y = None
        self.car_list = []
        self.create_car()

    def create_car(self):
        self.rand_y = random.randint(-270, 290)
        random_chance = random.randint(1,6)
        if random_chance == 3:
            tim = Turtle()
            tim.shape("square")
            tim.penup()
            tim.shapesize(1, 2)
            tim.color(random.choice(COLORS))
            tim.goto(340, self.rand_y)
            self.car_list.append(tim)

    def move(self):
        for car in self.car_list:
            car.backward(self.start)

    def increase_move(self):
        self.start += MOVE_INCREMENT
        for car in self.car_list:
            car.backward(self.start)
