# Class Snake
from turtle import Turtle

class Snake:
    
    perut_awal = [(0, 0), (-20, 0), (-40, 0)]
    snake_utuh = []
    
    def __init__(self):
        for sq_segmen in self.perut_awal:
            self.sq = Turtle("square")
            self.sq.penup()
            self.sq.color("white")
            self.sq.goto(sq_segmen)
            self.snake_utuh.append(self.sq)
    
    def move(self, n):
        """Mengerakkan snake dengan pergerakkan tiap n pixel"""
        # Berjalannya snake dari bagian ekornya. Ekor 3 ke 2, ekor 2 ke 1, ekor 1 kita gerakkan.
        for sq_segmen in range (len(self.snake_utuh) - 1, 0, -1):
            xpos = self.snake_utuh[sq_segmen-1].xcor()
            ypos = self.snake_utuh[sq_segmen-1].ycor()
            self.snake_utuh[sq_segmen].goto(xpos, ypos)
        
        self.snake_utuh[0].forward(n)
    
    def kanan(self):
        self.snake_utuh[0].right(90)

    def kiri(self):
        self.snake_utuh[0].left(90)