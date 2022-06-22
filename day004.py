import random
comp=["Rock","Paper","Scissor"]
c=random.randint(0,2)

p=int(input("Enter your choice: \n 1:Rock \n 2:Paper \n 3:Scissor \n"))
print("Computer choice: " + comp[c])
c+=1
if c==p:
    print("Draw")
elif c==1 and p==2:
    print("You win")
elif c==1 and p==3:
    print("Computer Wins")
elif c==2 and p==3:
    print("You win")
elif c==2 and p==1:
    print("Computer Wins")
elif c==3 and p==1:
    print("Computer Wins")
elif c==3 and p==2:
    print("Computer Wins")
else:
    print("code error")
