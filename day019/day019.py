from turtle import Turtle,Screen
import random
s=Screen()
s.setup(width=500, height=400)
colors=["red", "green","blue" ,"pink", "yellow", "purple"]
tim=[]
y=175
play=True

for i in range(0,6):
    tim.append(Turtle(shape="turtle"))
    tim[i].color(colors[i])
    tim[i].up()
    y-=50
    tim[i].goto(x=-230,y=y)

user=s.textinput(title="Hello!!", prompt="Which turtle will win the race?Enter color:")

while play:
    for t in tim:
        if t.xcor()>220:
            play=False
            print(f'Winner:>{t.pencolor()}')
            if t.pencolor()==user:
                print("YOU WIN")
            else:
                print("BETTER LUCK NEXT TIME")
            break
        dis=random.randint(0,10)
        t.forward(dis)

s.exitonclick()