# Snake Game
from turtle import Screen
import time
from class_snake import Snake
from class_food import Food
from class_scoreboard import Scoreboard


play = True

snake = Snake()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

food = Food()
sb = Scoreboard()

while play:
    # delay 0.1 lalu refresh screen dengan update
    screen.update()
    time.sleep(0.1)
    
    # ular bergerak
    snake.move()

    # Cek bila makan makanannya
    if food.distance(snake.kepala) < 20:
        food.muncul_acak()
        sb.scoreup()
        snake.tambah_panjang()
    
    # Cek bila kena pagar pembatas
    if snake.kepala.xcor() > 290 or snake.kepala.xcor() < -290 or snake.kepala.ycor() > 290 or snake.kepala.ycor() < -290:
        play = False
        sb.gameover()
    
    # Cek bila kena badannya sendiri?
    for segment in snake.snake_utuh:

        if segment != snake.kepala:
            
            if snake.kepala.distance(segment) < 10:
                play = False
                sb.gameover()

    # control ular
    screen.listen()
    screen.onkeypress(snake.kanan,"Right")
    screen.onkeypress(snake.kiri,"Left")
    
    

screen.exitonclick()
