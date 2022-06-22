logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
play=True
print(logo)
def add(n1,n2):
    return int(n1+n2)
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def re():
    global decision,n1,n2,answer
    for i in opdict:
        print(i)
    choice=input("Enter your choice: ")
    op=opdict[choice]
    answer=op(n1,n2)
    print(f'{n1} {choice} {n2} = {answer}')
    decision=input("would you like to use this answer (yes) or  perform new calculation (new) \n to quit enter anything")

opdict={
"+":add,
"-":sub,
"*":mul,
"/":div
}
n1=float(input("Enter first number: "))
n2=float(input("Enter Second number: "))
re()
while play:
    if decision=="yes":
        n1=answer
        n2=float(input("Enter Second number: "))
        re()
    elif decision=="new":
        n1=float(input("Enter first number: "))
        n2=float(input("Enter Second number: "))
        re()
    else:
        print("GOODBYE")
        play=False
