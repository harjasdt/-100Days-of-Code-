
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
clear = lambda: os.system('cls')

dict={}
play=True
print(logo)
print("Welcome to Blind Auction")
def take():
    global ask
    name=input("What is your name: ")
    bid=int(input("What is your Bid: $"))
    dict[name]=bid
    ask=input("Are there any more bidders?yes or no")

def result():
    win=0
    for i in dict:
        if dict[i]>win:
            win=dict[i]
            name=i
    print(f'Heighest bid was {win} made by {name}')
take()
while play:
    if ask=="yes":
        clear()
        take()
    else:
        play=False
        clear()
        result()
