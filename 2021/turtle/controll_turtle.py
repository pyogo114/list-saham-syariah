# Setir turtle
from turtle import Turtle, Screen
from random import choice

franklin = Turtle()

def maju():
    franklin.forward(10)

def kanan():
    new_heading = franklin.heading()-10
    franklin.setheading(new_heading)

def kiri():
    new_heading = franklin.heading()+10
    franklin.setheading(new_heading)

def mundur():
    franklin.backward(10)

def clear():
    franklin.clear()
    franklin.penup()
    franklin.home()
    franklin.pendown()

 


screen = Screen()
screen.listen()
screen.onkeypress(maju,"Up")
screen.onkeypress(kanan,"Right")
screen.onkeypress(kiri,"Left")
screen.onkeypress(mundur,"Down")
screen.onkeypress(clear,"c")
screen.exitonclick()