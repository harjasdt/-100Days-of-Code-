from turtle import Turtle, Screen
import random
t=Turtle()
t.speed(0)
Screen().colormode(255)
t.up()
t.right(90)
t.forward(200)
t.left(90)
t.backward(250)
right_side=[11 ,31, 51, 71, 91]
left_side=[21,41, 61, 81]
for i in range(0,101):
    if i in right_side:
        t.left(90)
        t.forward(50)
        t.left(90)
        t.dot(20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    if i in left_side:
        t.right(90)
        t.forward(50)
        t.right(90)
        t.dot(20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    t.forward(50)
    t.down()
    t.dot(20,(random.randint(0,255), random.randint(0,255),random.randint(0,255)))
    t.up()


Screen().exitonclick()