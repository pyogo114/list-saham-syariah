# Scoreboard
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):

    kiriscore = 0
    kananscore = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.updatescore()

    def updatescore(self):
        self.write(f"{self.kiriscore} - {self.kananscore}", move=True, align=ALIGNMENT, font=FONT)
    
    def gameover(self):
        self.home()
        self.color("white")
        self.write("Game Over", move=True, align=ALIGNMENT, font=FONT)
    
    def kiriscoreup(self):
        self.clear()
        self.kiriscore += 1
        self.goto(0, 260)
        self.updatescore()
    
    def kananscoreup(self):
        self.clear()
        self.kananscore += 1
        self.goto(0, 260)
        self.updatescore()
        
