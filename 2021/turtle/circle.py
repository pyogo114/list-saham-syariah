# Turtle

from turtle import Turtle
from random import randint,choice

timmy = Turtle()

colours = ["CornflowerBlue","Red", "DarkOrchid", "IndianRed","YellowGreen", "DeepSkyBlue","Violet","HotPink", "LightSeaGreen","wheat","MediumPurple", "Gold"]
to_direction = [0,90,180,270]
# Segisembilan (nanogon)
#for _ in range(9):
#    timmy.forward(100)
#    timmy.right(40)

def polygon(n):
    
    timmy.pensize(5)
    timmy.speed(8)
        
    timmy.color(choice(colours))
    
    timmy.circle(50)
        
    timmy.setheading(n)
            

n=0
for key in range(1, 36):
    n += 10
    polygon(n)
