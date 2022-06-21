'''
AUTOMATIC HURDLE DETECTOR
go to this link
http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def right():
    turn_left()
    turn_left()
    turn_left()
def check():
    turn_left()
    move()
    right()
def jump():
    c=0
    while wall_in_front():
        check()
        c+=1
    move()
    right()
    while c>0:
        move()
        c-=1
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()

'''
'''
MAZE SOLVER
link>
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def r():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
while not at_goal():
    if right_is_clear():
        r()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''
