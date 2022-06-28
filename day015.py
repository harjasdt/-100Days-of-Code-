from operator import truediv
from pickle import TRUE


menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report():
    print(f'WATER: {resources["water"]}')
    print(f'MILK: {resources["milk"]}')
    print(f'COFFEE: {resources["coffee"]}')
    print(f'MONEY: {profit}')

def payment(pro,price):
    global profit
    quarter=int(input("ENTER QUARTER"))
    dimes=int(input("ENTER DIMES"))
    nickel=int(input("ENTER NICKEL"))
    pennies=int(input("ENTER PENNIES"))
    total=(quarter*0.25)+(dimes*0.10)+(nickel*0.05)+(pennies*0.01)
    total=round(total,2)
    if total==price:
        print("PAYMENT DONE")
        print("THANKYOU FOR YOUR ORDER!!!")
        profit+=price
        return TRUE
    elif total>price:
        change=total-price
        print(f'HERE IS YOUR CHANGE: ${change}')
        print("THANKYOU FOR YOUR ORDER!!!")
        profit+=price
        return True
    else:
        print("INSUFFICIENT PAYMENT !!!")
        print(f'HERE IS YOUR REFUND: ${total}')
        return False

def check(pro):
    c1=menu[pro]["ingredients"]["water"]<=resources["water"]
    if pro!="espresso":
        c2=menu[pro]["ingredients"]["milk"]<=resources["milk"]
    else:
        c2=True
    c3=menu[pro]["ingredients"]["coffee"]<=resources["coffee"]

    if c1 and c2 and c3:
        print("MAKE YOUR PAYMENT")
        print(f'COST: {menu[pro]["cost"]}')
        status=payment(pro,menu[pro]["cost"])
        if status:
            resources["water"]-=menu[pro]["ingredients"]["water"]
            if pro!="espresso":
                resources["milk"]-=menu[pro]["ingredients"]["milk"]
            resources["coffee"]-=menu[pro]["ingredients"]["coffee"]
        
    else:
        print("NOT ENOUGH RESOURCES")
play=True



while play:
    user=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user=="off":
        play=False
    elif user=="report":
        report()
    elif user=="espresso" or user=="latte" or user =="cappuccino":
        check(user)
    else:
        print("WTF BRO!!! DEKH KE TYPE KARO")
