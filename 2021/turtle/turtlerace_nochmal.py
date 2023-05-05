# test nochmal

from turtle import Turtle,Screen
from random import randint

sc = Screen()
sc.setup(width=1000, height=500)
warna_user = sc.textinput("Pilih jagoanmu","Masukan warna kura kura jagoanmu dalam english : ")

lomba = False
play = True

if warna_user:
    lomba = True

pelangi = ["Red","Yellow","Green", "Orange","Blue","Black","Violet"]
n = 0
juara = 0
keranjang_kurakura = []
urutan_pemenang = []

for warna in range(0, 7):
    frank = Turtle(shape="turtle")
    frank.penup()
    frank.color(pelangi[warna])
    frank.goto(x = -480, y = -200 + n)
    n += 50

    keranjang_kurakura.append(frank)

while lomba:

    for kurakura in keranjang_kurakura:
    
        if kurakura.xcor() > 480 and kurakura.xcor() < 500:
            warna_pemenang = kurakura.pencolor()
            urutan_pemenang.append(warna_pemenang)
            kurakura.setx(600)            
            
        else:
            kurakura.forward(randint(0, 4))
        
    if len(urutan_pemenang) == 3:
        lomba = False

print(f"Juara 1 : {urutan_pemenang[0]}, juara 2 : {urutan_pemenang[1]}, juara 3 : {urutan_pemenang[2]}")

sc.exitonclick()