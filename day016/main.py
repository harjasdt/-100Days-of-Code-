from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm=CoffeeMaker()
mm=MoneyMachine()
menu=Menu()
play=True
while play:
    user=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user=="off":
        play=False
    elif user=="report":
        cm.report()
        mm.report()
    elif user=="espresso" or user=="latte" or user =="cappuccino":
        drink=menu.find_drink(user)
        made=cm.is_resource_sufficient(drink)
        if made:
            if mm.make_payment(drink.cost):
                print("HIIII")
                cm.make_coffee(drink)
    else:
        print("WTF BRO!!! DEKH KE TYPE KARO")

# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
#
# is_on = True
#
# while is_on:
#     choice = user=input("What would you like? (espresso/latte/cappuccino):").lower()
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#           coffee_maker.make_coffee(drink)
