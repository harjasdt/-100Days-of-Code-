from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("yellow")
        self.penup()
        self.goto(x=0, y=260)
        self.score=0

    def inc(self):
        self.score+=1
        self.clear()
        self.write(f'SCORE: {self.score}', move=False, align="center", font=('Arial', 19, 'normal'))

