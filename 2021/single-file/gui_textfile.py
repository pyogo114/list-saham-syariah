import tkinter
from datetime import datetime

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)



def button_clicked():
    #print("Button Clicked!")
    txt = input.get()

    mylabel = tkinter.Label(text=txt, font=("Arial",24, "bold"))
    mylabel.pack()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()

#mylabel2 = tkinter.Label(text="Ini label GUI2", font=("Arial",24, "bold"))
#mylabel2.pack(expand=1)

window.mainloop()
