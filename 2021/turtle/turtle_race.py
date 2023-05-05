# Setir turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 1000, height = 400)

turtle_color = ["Red", "Orange", "Yellow", "Blue", "Green", "Violet"]

turtle_jagoan = screen.textinput(title="Pilih jagoanmu", prompt="Pilih warna jagoanmu? ")

n = 0

keranjang_turtle = []

for key in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[key])
    new_turtle.penup()
    new_turtle.goto(-480, -130+n )
    n += 50
    keranjang_turtle.append(new_turtle)
   
play = False

if turtle_jagoan:
    play = True

while play:
    for kurakura in keranjang_turtle:
        langkah = randint(0,5)
        kurakura.forward(langkah)

        if kurakura.xcor() >= 480:
            
            play = False
            warna_pemenang = kurakura.pencolor()

            if warna_pemenang == turtle_jagoan:

                print(f"Yes, kura kura {warna_pemenang} jagoanmu menang.")
            
            else:

                print(f"Pemenangnya adalah kura kura {warna_pemenang}")


screen.exitonclick()