from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.goto(x=x, y=y)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(x=350, y=self.ycor() + 30)

    def down(self):
        self.goto(x=350, y=self.ycor() - 30)

    def upp(self):
        self.goto(x=-350, y=self.ycor() + 30)

    def downp(self):
        self.goto(x=-350, y=self.ycor() - 30)
