# Turtle

from turtle import Turtle
from random import randint

timmy = Turtle()

# Segisembilan (nanogon)
#for _ in range(9):
#    timmy.forward(100)
#    timmy.right(40)

def polygon(n):
    sudut = 360 / n
    
    r = randint(1,100) / 100
    g = randint(1,100) / 100
    b = randint(1,100) / 100

    timmy.color(r,g,b)
    timmy.pensize(10)
    
    for _ in range(n):
        timmy.forward(80)
        timmy.right(sudut)


for key in range(3,12):
    polygon(key)
