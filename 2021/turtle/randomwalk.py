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
    
    timmy.pensize(10)
    timmy.speed(8)
    
    for _ in range(n):
        
        timmy.color(choice(colours))
    
        timmy.forward(20)
        
        timmy.setheading(choice(to_direction))        


for key in range(30):
    polygon(key)
