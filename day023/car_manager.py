from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 12


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        c = random.randint(0, 2)
        if c == 1:
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.color(random.choice(COLORS))
            self.penup()
            self.goto(300, random.randint(-230, 250))
        else:
            self.penup()
            self.hideturtle()


    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())




