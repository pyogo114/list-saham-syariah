# Turtle

from turtle import Turtle,Screen

timmy = Turtle()
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


timmy.left(90)

for _ in range(4):
    for _ in range(10):
        timmy.pendown()
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
    
    timmy.left(90)
