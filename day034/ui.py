import tkinter
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")


class Interface:

    def __init__(self, qb: QuizBrain):
        self.quiz= qb
        self.window=Tk()
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label=Label(text=f"SCORE: 0/10",bg=THEME_COLOR,fg="white")
        self.label.grid(row=0,column=1)

        self.canvas=tkinter.Canvas(width=300, height=250, bg="WHITE")
        self.text=self.canvas.create_text(150,125,width=280,text="ques",fill=THEME_COLOR,font=FONT)
        self.canvas.grid(row=1,column=0,columnspan=3,pady=50)

        p1=PhotoImage(file="images/true.png")
        self.btn1=Button(image=p1, command=self.btick)
        self.btn1.grid(row=2,column=0)

        p2=PhotoImage(file="images/false.png")
        self.btn2 = Button(image=p2, command=self.bwrong)
        self.btn2.grid(row=2, column=2)

        self.next()
        self.window.mainloop()

    def next(self):
        if self.quiz.still_has_questions():
            t=self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=t)
        else:
            self.canvas.itemconfig(self.text,text=f"YOU HAVE REACHED THE END")
            self.btn1.config(state="disabled")
            self.btn2.config(state="disabled")
    def btick(self):
        self.quiz.check_answer("True")
        self.next()
        self.sc()

    def bwrong(self):
        self.quiz.check_answer("False")
        self.next()
        self.sc()

    def sc(self):
        self.label.config(text=self.quiz.showscore())





