from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
mark=" "
main=None
# ---------------------------- TIMER RESET ------------------------------- # 
def ress():
    global reps, main,mark
    main=window.after_cancel(main)
    reps = 0
    l1.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    mark = " "
    l2.config(text=mark)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def startcount():
    global reps
    reps+=1
    if reps%8 ==0 :
        countdown(LONG_BREAK_MIN * 60)
        l1.config(text="LONG BREAK", fg=PINK)
    elif reps % 2 ==0:
        countdown(SHORT_BREAK_MIN * 60)
        l1.config(text="SHORT BREAK", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        l1.config(text="WORK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min= math.floor(count/60)
    sec = count % 60

    if sec<10:
        sec="0"+str(sec)
    canvas.itemconfig(timer_text, text=f'{min}:{sec}')

    if count>0:
        global main
        main=window.after(1000, countdown, count-1)
    else:
        global mark
        startcount()
        work=math.floor(reps%2)
        for _ in range(work):
            mark += "|"
            l2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("WORK CLOCK")
window.config(width=220, height=232)
window.config(pady=90, padx=100, bg=YELLOW)

l1=Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
l1.grid(row=0, column=1)

canvas=Canvas(height=230, width=224,bg=YELLOW ,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato)
timer_text=canvas.create_text(100, 130,text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


b1=Button(text="Start", command=startcount)
b1.grid(row=2, column=0)

b2=Button(text="Reset", command=ress)
b2.grid(row=2, column=2)

l2=Label(text="|",fg=GREEN, bg=YELLOW)
l2.grid(row=3, column=1)

window.mainloop()