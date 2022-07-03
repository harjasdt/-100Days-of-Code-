from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.dis_y = 10
        self.dis_x = 10

    def move(self):
        if self.ycor() > 280:
            self.dis_y = self.dis_y * -1
        elif self.ycor() < -280:
            self.dis_y = self.dis_y * -1
        self.goto(x=self.xcor()+self.dis_x, y=self.ycor()+self.dis_y)

    def bouncex(self):
        self.dis_x = self.dis_x * -1

    def reset(self):
        self.goto(x=0, y=0)
        self.bouncex()
