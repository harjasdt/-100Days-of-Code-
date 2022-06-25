import random
def game(c):
    while c!=0:
        inp=int(input(f'guess the number {c} chances remaining'))
        if inp>ans:
            print("GO LOWER")
        elif inp<ans:
            print("GO HIGHER")
        if inp==ans:
            print("YOU WIN")
            break
        c-=1
    if c==0:
        print("YOU LOST") 
        print(f"THE ANSWER WAS {ans} ")
ans=random.randint(0,100)
chioce=input("Select mode Easy OR Hard").lower()
if chioce=="easy":
    game(10)
elif chioce=="hard":
    game(5)
else:
    print("WRONG CHOICE!!! PAY ATTENTION")