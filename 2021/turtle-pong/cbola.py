# Class Bola
from turtle import Turtle
import random

KECEPATAN_BOLA = 15

class Bola(Turtle):

    sudut_start = [10, 20, 30, 150, 160, 170, 190, 200, 210, 330, 340, 350]
    
    pos_dari = []   #posisi DARI sebelum menyentuh garis
    pos_tembok = []   #posisi KE setelah menyentuh garis
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.home()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.start()
    
    def start(self):
        self.setheading(random.choice(self.sudut_start))
    
    def move(self):
        self.forward(KECEPATAN_BOLA)
    
    def resetbola(self):
        self.home()
        self.start()
        self.move()
    
    def set_pos_dari(self, x, y):
        self.pos_dari = [x , y]
    
    def get_pos_dari(self):
        return self.pos_dari
    
    def set_pos_ke(self, x, y):
        self.pos_tembok = [x , y]
    
    def get_pos_ke(self):
        return self.pos_tembok
    
    def memantul_tembok(self):
        sudut = self.towards(int(self.pos_dari[0]), int(self.pos_dari[1]))
        self.forward(0)

        # tembok bawah
        if sudut > 0 and sudut < 90:
            if sudut > 85:  # biar gak mandek memantul 90 derajat
                sudut -= 10
            sudut = 180 - sudut
        elif sudut >=90 and sudut < 180:
            if sudut < 100:
                sudut += 10
            sudut = 180 - sudut
        
        # tembok atas
        elif sudut >= 180 and sudut <= 270:
            if sudut > 260:
                sudut -= 10
            sudut = 360 - (sudut - 180)
        else:
            if sudut < 280:
                sudut += 10
            sudut = 180 + (360 - sudut)
            
        self.setheading(sudut)
        self.forward(KECEPATAN_BOLA)
    
    def memantul_paddle(self):
        sudut = self.towards(int(self.pos_dari[0]), int(self.pos_dari[1]))
        self.forward(0)

        # paddle kanan
        if sudut >=90 and sudut < 180: #k2
            sudut = 270 - (sudut - 90)

        elif sudut > 180 and sudut <= 270: #k3
            sudut = 90 + (270 - sudut)
        
        # paddle kiri
        elif sudut < 90 and sudut > 0: #k1
            sudut = 270 + (90 - sudut)
        
        elif sudut < 360 and sudut > 270: #k4
            sudut = 90 - (sudut - 270)
            
        self.setheading(sudut)
        self.forward(KECEPATAN_BOLA)




    
