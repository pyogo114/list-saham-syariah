# Coffee Machine OOP
from coffemenu import *

class CoffeeResources:
    water = 0
    milk = 0
    coffee = 0

    def setResources(self, w, m, c):
        self.water = w
        self.milk = m
        self.coffee = c
    
    def deductEspresso(self):
        self.water -= 50
        self.milk -= 0
        self.coffee -= 18

    def deductLatte(self):
        self.water -= 200
        self.milk -= 150
        self.coffee -= 24
    
    def deductCappuccino(self):
        self.water -= 250
        self.milk -= 100
        self.coffee -= 24
    
    def report(self):
        print(f"Water : {self.water} Milk : {self.milk} Coffee : {self.coffee}")
    
    def checkEspresso(self):
        if self.water > 50:
            if self.coffee > 18:
                return True
            else:
                print(err_report["NotEnoughCoffee"])
        else:
            print(err_report["NotEnoughWater"])


class CoffeePayment:
    cents = 0.0
    t_cents = 0.0 #temprorary cents
    espresso_price = 1.5
    latte_price = 2.5
    cappucino_price = 3.0

    def report(self):
        print(f"Cash : {self.cents}")

    def is_sufficient(self, t):

        self.t_cents += 0.25 * int(input("How many quaters? "))
        self.t_cents += 0.10 * int(input("How many dimes? "))
        self.t_cents += 0.05 * int(input("How many nickels? "))
        self.t_cents += 0.01 * int(input("How many pennies? "))
        
        if t == "espresso":
            if self.t_cents >= self.espresso_price:
                self.cents += self.espresso_price
                print(f"Here is your charge ${round(self.t_cents - self.espresso_price, 2)}")
                self.t_cents = 0.0
                print("Enjoy!")
                return True
            else:
                return print(err_report["NotEnoughCash"])

class CoffeMachine:
    on = True
    cr = CoffeeResources()
    cp = CoffeePayment()
    
    def __init__(self):    
        self.cr.setResources(300, 200, 100)
    
    def start(self):
        print(logo)

        while self.on:
            ELC = input("What would you like? (espresso/latte/cappuccino): ")

            if ELC == 'espresso':
                err_id = self.cr.checkEspresso()
                if err_id == True:
                    self.cp.is_sufficient(ELC)
                    self.cr.deductEspresso()
            
            elif ELC == 'report':
                err_id = self.cr.report()
                self.cp.report()

            elif ELC == 'off':
                self.on = False


mesin = CoffeMachine()
mesin.start()


    
            


