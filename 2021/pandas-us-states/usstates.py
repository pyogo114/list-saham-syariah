# game usstates
import pandas
import turtle
from turtle import *

layar = turtle.Screen()
layar.title("US States Game")
gambar = "blank_states_img.gif"

layar.addshape(gambar)
turtle.shape(gambar)

score = 0

state_terjawab = []

data = pandas.read_csv("50_states.csv")

# Mengambil kolom state dari keseluruhan tabel
all_state = data.state


game = True

while game:

    jawaban = layar.textinput(title="Gues the state " + str(score) + "/50", prompt="What's another state name?")
    jawaban = jawaban.title()
    #print(jawaban)
    #print(f"allstate {all_state}")
    
    if jawaban == "Exit":
        state_tidak_terjawab = []
        
        i=0
        for _ in range(len(all_state)):

            if not all_state[i] in state_terjawab:
                state_tidak_terjawab.append(all_state[i])
            
            i += 1

        #print(f"states tidak terjawab = {state_tidak_terjawab}")
        
        d_state_tidak_terjawab = {
            "State" : state_tidak_terjawab            
        }

        tabel = pandas.DataFrame(d_state_tidak_terjawab)
        tabel.to_csv("states_tidak_terjawab.csv")
        print(tabel)

        game = False
        exit()

    

    ketemu = data[data["state"] == jawaban]
  
    # Cari jawaban, bila ketemu maka tampilkan
    if len(ketemu) > 0:
        o_namanegara = Turtle()
        o_namanegara.hideturtle()
        o_namanegara.penup()

        namanegara = data.loc[data['state']== jawaban,'state'].values[0]
        x = data.loc[data['state']== jawaban,'x'].values[0]
        y = data.loc[data['state']== jawaban,'y'].values[0]
    
        o_namanegara.goto(x, y)
        o_namanegara.color("black")
        o_namanegara.write(namanegara)
        state_terjawab.append(namanegara)
        score += 1

    



#layar.exitonclick()
turtle.mainloop()


