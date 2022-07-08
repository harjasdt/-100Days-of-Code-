from tkinter import *
window=Tk()
window.minsize(height=200, width=300)
window.title("Miles to Km")
window.config(padx=100, pady=30)

def click():
    ans=int(user.get()) * 1.6
    l3.config(text=ans)


user = Entry(width=5)
user.grid(row=0, column=1)

l1=Label(text="Miles")
l1.grid(row=0, column=2)

l2=Label(text="is equal to ")
l2.grid(row=1, column=0)

l3=Label(text="_")
l3.grid(row=1, column=1)

l4=Label(text="Km")
l4.grid(row=1, column=2)

button = Button(text="Convert", command=click)
button.grid(row=2, column=1)


window.mainloop()