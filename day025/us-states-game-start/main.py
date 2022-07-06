import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
l=data["state"]
list = l.to_list()
print(list)
correct_guess=0
while correct_guess<50:
    ans = screen.textinput(title=f'{correct_guess}/50', prompt="Guess a state")
    if ans.title() in list:
        list.remove(ans.title())
        correct_guess+=1
        cor = data[data["state"] == ans.title()]
        x=int(cor["x"])
        y=int(cor["y"])
        t1=turtle.Turtle()
        t1.penup()
        t1.hideturtle()
        t1.goto(x, y)
        t1.write(ans.title(), align="center", font=("Courier", 9, "normal"))
    elif ans.title() == "Exit":
        dict={
            "missed":list
        }
        df=pandas.DataFrame(dict)
        df.to_csv("missed-states")
        break