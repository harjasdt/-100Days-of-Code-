print('''
    //   ) )
   //              ___          ___         / ___
  //  ____       //___) )     //___) )     //\ \
 //    / /      //           //           //  \ \
((____/ /      ((____       ((____       //    \ \   ''')
print("Welcome to Treasure island \nYour mission is to find the Treasure")
x=input("Left or Right")
if (x=="Left" or x=='left'):
    x=input("swim or wait")
    if(x=="Swim" or x=='swim'):
        x=input("Which door: Red,Blue or Yellow")
        if(x=="Red" or x=='red'):
            print("Game Over")
        elif(x=="Yellow" or x=='yellow'):
            print("Treasure Found")
        elif(x=="Blue" or x=='blue'):
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
