import collections
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
def ces(r,text,direc):
    print(f'Plain text: {text}')
    new=collections.deque(alphabet)
    if direc=="encode":
        new.rotate(-r)
    else:
        new.rotate(r)
    index=[]
    code=[]
    for i in text:
        if i not in alphabet:
            index.append(i)
        else:
            a=alphabet.index(i)
            index.append(a)
    for i in index:
        if i not in range(0,30):
            code.append(i)
        else:
            a=new[i]
            code.append(a)
    print("Encrypted text: ",end="")
    for i in code:
        print(i,sep="",end="")
    print("")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

play=True
print(logo)
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and end to quit:\n").lower()
    if direction=="encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ces(shift,text,direction)
    elif direction=="decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ces(shift,text,direction)
    elif direction=="end":
        play=False
        print("GOODBYE")
    else:
        print("NOT A VALID CHOICE")
