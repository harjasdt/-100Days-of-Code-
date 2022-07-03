from turtle import Turtle
pos = [(0, 0), (-20, 0), (-40, 0)]
dis=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]

    def create_snake(self):
        for i in pos:
            self.add_segment(i)

    def add_segment(self,i):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(i)
        self.tims.append(t)

    def extend(self):
        self.add_segment(self.tims[-1].position())

    def move(self):
        for seg_num in range(len(self.tims) - 1, 0, -1):
            new_x = self.tims[seg_num - 1].xcor()
            new_y = self.tims[seg_num - 1].ycor()
            self.tims[seg_num].goto(new_x, new_y)
        self.head.forward(dis)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)