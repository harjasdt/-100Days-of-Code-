import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#player
user = Player()

#making cars
cars = []

#level
level=Scoreboard()
#activate keyboard
screen.listen()
screen.onkey(user.up, "Up")
number=10
game_is_on = True
counter=1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter % 6 == 0:
        for i in range(0, number):
            c = CarManager()
            cars.append(c)


    #moving the cars
    for i in cars:
        i.move()

    #updating score
    if user.ycor() > 250:
        level.level_up()
        user.start()
        number+=5
    #over game
    for i in cars:
        if user.distance(i) < 15:
            level.game_end()
            game_is_on = False

    counter+=0.5

screen.exitonclick()