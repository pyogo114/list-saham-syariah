# Paddle Pong
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,player_n):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        
        if player_n == 1:
            self.posisi_player1()
        else:
            self.posisi_player2()
    
    def posisi_player1(self):
        self.goto(350,0)
    
    def posisi_player2(self):
        self.goto(-350,0)

    def keatas(self):
        if self.ycor() <= 220:
            self.goto(self.xcor(), self.ycor() + 20)
    
    def kebawah(self):
        if self.ycor() >= -220:
            self.goto(self.xcor(), self.ycor() - 20)
    