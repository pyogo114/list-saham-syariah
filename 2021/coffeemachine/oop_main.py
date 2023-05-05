# Mencoba lecture 16

from class_menu import Menu
from class_coffeemaker import CoffeeMaker
from class_moneymachine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

play = True

while play:
    drink = input(f"What would you like? {menu.get_items()}")
    if drink == 'off':
        play = False
    
    elif drink == 'report':
        coffee.report()
        money.report()
    
    else: 
        drink = menu.find_drink(drink)

        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)



