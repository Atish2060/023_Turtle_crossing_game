import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.player_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move()
    screen.update()
    for car1 in car.car_list:
        if player.distance(car1) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() == 290:
        player.finish_line()
        car.increase_move()
        score.inc_level()

screen.exitonclick()
