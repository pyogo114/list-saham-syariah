# Class Snake
from turtle import Turtle

class Snake:
    
    perut_awal = [(0, 0), (-20, 0), (-40, 0)]
    snake_utuh = []
        
    def __init__(self):
        self.create()
        self.kepala = self.snake_utuh[0] # kepala ular
    
    def create(self):
        for sq_segmen in self.perut_awal:
            self.perut(sq_segmen)
            
    
    def perut(self,posisi):
        self.sq = Turtle("square")
        self.sq.penup()
        self.sq.color("white")
        self.sq.goto(posisi)
        self.snake_utuh.append(self.sq)
    
    def tambah_panjang(self):
        self.perut(self.snake_utuh[-1].position())

    def move(self, n = 20):
        """Mengerakkan snake dengan pergerakkan tiap n pixel"""
        # Berjalannya snake dari bagian ekornya. Ekor 3 ke 2, ekor 2 ke 1, ekor 1 kita gerakkan.
        for sq_segmen in range (len(self.snake_utuh) - 1, 0, -1):
            xpos = self.snake_utuh[sq_segmen-1].xcor()
            ypos = self.snake_utuh[sq_segmen-1].ycor()
            self.snake_utuh[sq_segmen].goto(xpos, ypos)
        
        self.kepala.forward(n)
    
    def kanan(self):
        self.kepala.right(90)

    def kiri(self):
        self.kepala.left(90)
    