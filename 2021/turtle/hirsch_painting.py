# Hirsch dot painting

from turtle import Turtle
from random import choice
import turtle


franklin = Turtle()

def hirsch():

    # Pallet color
    colours = [ (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
    n = 0
    franklin.speed(2)
    franklin.penup()
    franklin.hideturtle()
    
    turtle.colormode(255)

    for _ in range(10):

        franklin.setposition(-250,-250 + n)

        for _ in range(10):
            franklin.dot(20,choice(colours))
            franklin.forward(50)
        
        n += 50
            

hirsch()
turtle.Screen().exitonclick()

