# Scoreboard
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.updatescore()

    def updatescore(self):
        self.write(f"Skor {self.score}", move=True, align=ALIGNMENT, font=FONT)
    
    def gameover(self):
        self.home()
        self.color("white")
        self.write("Game Over", move=True, align=ALIGNMENT, font=FONT)
    
    def scoreup(self):
        self.clear()
        self.score += 1
        self.goto(0, 260)
        self.updatescore()
        
