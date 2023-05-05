# Coffee Maker

from coffemenu import *


def check_resources(taste):
    """Check if all resources sufficient for a cup of espresso, latte or cappuccino."""

    if resources["water"] >= MENU[taste]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[taste]["ingredients"]["coffee"]:
            if taste == "latte" or taste == "cappuccino":
                if resources["milk"] >= MENU[taste]["ingredients"]["milk"]:
                    return True
                else:
                    return "NotEnoughMilk"
            else:
                return True
        else:
            return "NotEnoughCoffee"
    else:
        return "NotEnoughWater"


def check_transaction(taste):

    quarters = int(input("How many quaters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    
    cents =  quarters * 25 + dimes * 10 + nickels * 5 + pennies
    
    if cents >= MENU[taste]["cost"] * 100:
        return (cents - MENU[taste]["cost"] * 100) / 100
    else:
        return "NotEnoughCash"

def make_coffee(taste):
    resources["cash"] += MENU[taste]["cost"]

    resources["water"] -= MENU[taste]["ingredients"]["water"]
    resources["coffee"] -= MENU[taste]["ingredients"]["coffee"]
    
    if taste == "latte" or taste == "cappuccino":
        resources["milk"] -= MENU[taste]["ingredients"]["milk"]


# ===============================================================#    

print(logo)

on = True

while on:

    ELC = input("What would you like? (espresso/latte/cappuccino): ")

    if ELC == 'espresso' or ELC == 'latte' or ELC == 'cappuccino':
        #Check resources
        err_id = check_resources(ELC)
        
        if err_id == True:
            
            #Check Transaction
            err_id = check_transaction(ELC)
            if err_id != "NotEnoughCash":

                #Transaction
                print(f"Here is your ${err_id} in charge.")
                #Make Coffe
                make_coffee(ELC)
                #Enjoy
                print(f"Here is your {ELC}. Enjoy!")

            else:
                print(err_report["NotEnoughCash"])
            
        else: 
            print(err_report[err_id])
        

    elif ELC == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['cash']}")

    elif ELC == 'off':
        on = False
