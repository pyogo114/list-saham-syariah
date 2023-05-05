# Snake Game
from sqlite3 import SQLITE_SAVEPOINT
from turtle import Turtle,Screen
import time

n = 0
move = True

perut_awal = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

sc = Screen()
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.tracer(0)

for sq_segmen in perut_awal:
    sq = Turtle("square")
    sq.penup()
    sq.color("white")
    sq.goto(sq_segmen)
    snakes.append(sq)

def kanan():
    snakes[0].right(90)
def kiri():
    snakes[0].left(90)


while move:
    sc.update()
    time.sleep(0.1)

    for sq_segmen in range (len(snakes) - 1, 0, -1):
        xpos = snakes[sq_segmen-1].xcor()
        ypos = snakes[sq_segmen-1].ycor()
        snakes[sq_segmen].goto(xpos, ypos)
    
    snakes[0].forward(20)
    sc.listen()
    sc.onkeypress(kanan,"Right")
    sc.onkeypress(kiri,"Left")
    
    


    





    

sc.exitonclick()
