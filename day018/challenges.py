from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.color("red")
#square-------------------------------------
# i=0
# while i < 4:
#     t.forward(100)
#     t.right(90)
#     i+=1

#different shapes with different colors--------------------
# colors = ["green", "brown","red","yellow","blue","pink","purple","cyan","orange","black]
# for n in range(3, 11):
#     angle = 360/n
#     t.color(random.choice(colors))
#     while n != 0:
#         t.forward(100)
#         t.right(angle)
#         n -= 1

#random walk -------------------\\
# Screen().colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     rc=(r,g,b)
#     return rc
#
# direction = [1, 2, 3, 4]
# t.pensize(8)
# t.speed(0)
# for i in range(0,200):
#     if random.choice(direction) == 1:
#         t.forward(20)
#     elif random.choice(direction) == 2:
#         t.backward(20)
#     elif random.choice(direction) == 3:
#         t.right(90)
#         t.forward(20)
#     elif random.choice(direction) == 4:
#         t.left(90)
#         t.forward(20)
#     t.color(random_color())

#spirograph
t.speed(0)
Screen().colormode(255)
for i in range(0,360):
    t.setheading(i)
    t.circle(100)
    t.color(random.randint(0,255), random.randint(0,255),random.randint(0,255))
Screen().exitonclick()