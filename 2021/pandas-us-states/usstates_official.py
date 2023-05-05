# game usstates
import pandas
import turtle
from turtle import *

layar = turtle.Screen()
layar.title("US States Game")
gambar = "blank_states_img.gif"

layar.addshape(gambar)
turtle.shape(gambar)

state_terjawab = []

data = pandas.read_csv("50_states.csv")
l_state = data.state.to_list()

while len(state_terjawab) < 50:
    jawaban = layar.textinput(title=f"Guess the state {len(state_terjawab)}/50", 
        prompt="What's another state name?").title()
    
    if jawaban == "Exit":
        missing_state = []
        for state in l_state:
            if not state in state_terjawab:
                missing_state.append(state)
        
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_kurang.csv")
        break
    
    if jawaban in l_state:
        o_namanegara = Turtle()
        o_namanegara.hideturtle()
        o_namanegara.penup()

        baris_state = data[data.state == jawaban]
        x = float(baris_state.x)
        y = float(baris_state.y)
 
        o_namanegara.goto(x, y)
        o_namanegara.color("black")

        # data series ambil kolomnya lalu keluarkan itemnya tanpa embel embel pandas
        o_namanegara.write(baris_state.state.item())
        state_terjawab.append(jawaban)
