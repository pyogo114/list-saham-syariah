# Class Food
from turtle import Turtle
from random import randint

class Food(Turtle):
    
    x = 0
    y = 0

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.muncul_acak()

    def muncul_acak(self):
        x = randint(-270,270)
        y = randint( -270, 270)
        self.goto(x, y)


