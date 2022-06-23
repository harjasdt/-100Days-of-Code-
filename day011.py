import random
import os
clear = lambda: os.system('cls')
def add_card(lis):
    lis.append(random.choice(deck))

def total(lis):
    sum=0;
    for i in lis:
        sum=sum+i
    return sum

deck=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
play=True
while play:
    choice=input("Do you want to play a game of Blackjack? Type 'y' or' n': ")
    your_card=[]
    comp_card=[]
    add_card(your_card)
    add_card(comp_card)
    comp_score=0
    if choice=="y":
        while choice=="y":
            if choice=="y":
                clear()
                add_card(your_card)
                if comp_score<17:
                    add_card(comp_card)
                your_score=total(your_card)
                comp_score=total(comp_card)
                if your_score>21:
                    clear()
                    print(f'Your final hand: {your_card}, Final score: {your_score} ')
                    print(f'Computers final hand: {comp_card}, Final score: {comp_score} ')
                    print("YOU WENT OVER.YOU LOSE")
                    break
                else:
                    clear()
                    print(f'Your Cards: {your_card} , Score: {your_score}')
                    print(f'Computers First Card: {comp_card[0]}')
                choice=input("Type 'y' to get another card or 'n' to pass: ")
                if choice=="n":
                    clear()
                    print(f'Your final hand: {your_card}, Final score: {your_score} ')
                    print(f'Computers final hand: {comp_card}, Final score: {comp_score} ')
                    your_diff=21-your_score
                    comp_diff=21-comp_score
                    if your_score==comp_score:
                        print("DRAW")
                    elif your_diff<comp_diff:
                        print("YOU WIN")
                    else:
                        print("YOU LOSE")
                elif choice=="y":
                    continue
                else:
                    print("YOU MISSED!!!PAY ATTENTION")
                    break
    elif choice=="n":
        play=False
        print("THANKYOU")
    else:
        print("YOU MISSED!!!PAY ATTENTION")
        break
