# Pong Games
from turtle import Screen
from cpaddle import Paddle
from cbola import Bola
from cscoreboard import Scoreboard
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.tracer(0)

b = Bola()

score = Scoreboard()

pkanan = Paddle(1)
pkiri = Paddle(2)

play = True

while play:

    # update screen
    s.update()

    # tahan play selama 0.1 detik
    time.sleep(.1)

    # bola kena tembok
    if (b.ycor() >= 230 and b.ycor() <= 250) or (b.ycor() <= -230 and b.ycor() >= -250):
        b.set_pos_dari(b.xcor(), b.ycor())
    
    if b.ycor() >= 280 or b.ycor() <= -280:
        b.memantul_tembok()
    
    # bola kena paddle
    if (b.xcor() >= 310 and b.xcor() <= 330) or (b.xcor() <= -310 and b.xcor() >= -330):
        b.set_pos_dari(b.xcor(), b.ycor())
    
    if b.distance(pkanan) < 30 or b.distance(pkiri) < 30:
        b.memantul_paddle()

    if b.xcor() > 390: 
        score.kiriscoreup()
        b.resetbola()

    if b.xcor() < -390:
        score.kananscoreup()
        b.resetbola()
    
    # bola bergerak
    b.move()

    # control paddlekanan
    s.listen()

    # Control player 1
    s.onkeypress(pkanan.keatas,"Up")
    s.onkeypress(pkanan.kebawah,"Down")

    # Control player 2
    s.onkeypress(pkiri.keatas,"w")
    s.onkeypress(pkiri.kebawah,"x")
    

s.exitonclick()