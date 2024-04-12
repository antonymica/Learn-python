#coding:utf-8

# Fonction pour convertion de temperature en fahrenheit
"""def conv():
    celcius = float(temp.get())
    fahrenheit = celcius * 1.8 + 32
    far.setvar(str(fahrenheit))"""

from tkinter import *

# Fenetre principale
app = Tk()
app.title("Température en Fahrenheit")

# Les deux sections Canvas
can1 = Canvas(app, width=100, height=50, bg="gray", border=20)
temp = Entry(can1, validate=int)
can1.pack(side=RIGHT)
temp.pack()


can2 = Canvas(app, width=100, height=50, bg="gray", border=20)
far = Entry(can2)
can2.pack(side=LEFT)
far.pack()
# Boutton
Button(app, text="Convert").pack(side=BOTTOM)

celcius = float(temp.get())
fahrenheit = celcius * 1.8 + 32
far.setvar(str(fahrenheit))

# Demarage
app.mainloop()