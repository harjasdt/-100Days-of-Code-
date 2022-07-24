from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox

import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    ans = []
    for i in range(0, 9):
        ans.append(random.choice(letters))
    for i in range(0, 4):
        ans.append(random.choice(symbols))
    for i in range(0, 6):
        ans.append(random.choice(numbers))
    random.shuffle(ans)
    passw=""
    passw="".join(ans)
    user3.delete(0, "end")
    user3.insert(0,passw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def addition() :
    new_data = {
        user1.get() : {
            "email": user2.get(),
            "password" :user3.get(),
        },
    }
    if user1.get()=="" or user2.get()=="" or user3.get()=="":
        messagebox.showerror(title="OOPS!!!", message="DO NOT LEAVE ANY FIELD EMPTY")
    else:
        try:
            with open("data.json", "r") as data:
                # loading existing data
                x = json.load(data)

                # updating data
                x.update(new_data)
            with open("data.json", "w") as data:
                # adding data
                json.dump(x, data, indent=4)
                user1.delete(0, "end")
                user3.delete(0, "end")
        except :
            with open("data.json", "w") as data:
                # adding data
                json.dump(new_data, data, indent=4)
                user1.delete(0, "end")
                user3.delete(0, "end")



def search():
    try:
        with open("data.json", "r") as data:
            # loading existing data
            x = json.load(data)
            found=False
            for key in x:
                if key.lower()==user1.get().lower():
                    messagebox.showinfo(title=f'{key}', message=f'{x[key]}')
                    found=TRUE
            if not found:
                messagebox.showerror(title="OOPS!!!", message="No ENTRIES FOUND")
    except JSONDecodeError:
        messagebox.showerror(title="OOPS!!!", message="0 ENTRIES PRESENT")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)
canvas=Canvas(height=200, width=200)
pic=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)

l1=Label(text="Website")
l1.grid(row=1, column=0)

user1=Entry()
user1.grid(row=1, column=1)
user1.focus()

bf=Button(text="Search", command=search)
bf.grid(row=1, column=2)

l2=Label(text="Email/username")
l2.grid(row=2, column=0)

user2=Entry(width=30)
user2.grid(row=2, column=1, columnspan=2)
user2.insert(0, "s@mail")

l3=Label(text="Password")
l3.grid(row=3, column=0)

user3=Entry(width=21)
user3.grid(row=3,column=1)

b1=Button(text="Generate Password", command=gen)
b1.grid(row=3, column=2)

b2=Button(text="Add", width=36, command=addition)
b2.grid(row=4, column=1, columnspan=2)
window.mainloop()
