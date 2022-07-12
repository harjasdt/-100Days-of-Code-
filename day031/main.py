from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#_-----------------------------flip


def flip():
    global timer
    win.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=img2)
    canvas.itemconfig(txt1, text="English", fill="white")
    canvas.itemconfig(txt2, text=final["English"], fill="white")

#_________________------------------------------importing data from csv and updating cards
try:
    df=pandas.read_csv("data/new.csv")
except:
    df = pandas.read_csv("data/french_words.csv")
finally:
    initial_dic=df.to_dict(orient="records")
    final=random.choice(initial_dic)


def wrong():
    global final, timer
    final=random.choice(initial_dic)
    canvas.itemconfig(canvas_image, image=img1)
    canvas.itemconfig(txt1, text="French", fill="black")
    canvas.itemconfig(txt2, text=final["French"], fill="black")
    timer=win.after(3000, flip)


def correct():
    global final
    initial_dic.remove(final)
    data=pandas.DataFrame(initial_dic)
    data.to_csv("data/new.csv")
    new_dic = data.to_dict(orient="records")
    final = random.choice(new_dic)
    wrong()

#_----------------------------------------------UI SETUP
win=Tk()
win.title("FLASH  CARDS")
win.config(pady=50, padx=50)

canvas=Canvas(height=530, width=800)
img1=PhotoImage(file="images/card_front.png")
img2=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 265, image= img1)

txt1=canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
txt2=canvas.create_text(400, 263, text=final["French"], font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

img_correct=PhotoImage(file="images/right.png")
b1=Button(image=img_correct, highlightthickness=0, command=correct)
b1.grid(row=2, column=1)

img_wrong=PhotoImage(file="images/wrong.png")
b2=Button(image=img_wrong, highlightthickness=0 , command=wrong)
b2.grid(row=2, column=2)


timer=win.after(3000, flip)



win.mainloop()