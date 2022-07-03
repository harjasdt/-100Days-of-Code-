import time
from score import Score
from paddle import Paddle
from ball import Ball
from turtle import Turtle, Screen

#setting up the screen
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
#paddle 1
p1=Paddle(350,0)
p2=Paddle(-350, 0)
#paddle1 keys
screen.listen()
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.upp, "w")
screen.onkey(p2.downp, "s")
#ball
play=True
b=Ball()
score=Score()
while play:
    time.sleep(0.1)
    screen.update()
    b.move()
    #paddle detection
    if b.distance(p1) <50 and b.xcor() >330 or b.distance(p2) <50 and b.xcor() < -330:
        b.bouncex()

    #right paddle miss
    if b.xcor() >360:
        b.reset()
        score.left()
    # left paddle miss
    if b.xcor() < -360:
        b.reset()
        score.right()
screen.exitonclick()