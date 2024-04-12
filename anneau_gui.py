#coding:utf-8
from tkinter import *

def cercle(i):
    x1, y1 = coord[i][0], coord[i][1]
    can.create_oval(x1, y1, x1 + 100, y1 + 100, width=2, outline=coul[i])

def c1():
    cercle(0)

def c2():
    cercle(1)

def c3():
    cercle(2)

def c4():
    cercle(3)

def c5():
    cercle(4)

def tout():
    i = 0
    while i < 5:
        cercle(i)
        i += 1

def effacer():
    can.delete(ALL)

# Coordonnées x, y des 5 anneaux
coord = [[20, 30], [120, 30], [220, 30], [70, 80], [170, 80]]
# couleur des anneaux
coul = ['red', 'yellow', 'blue', 'green', 'black']

app = Tk()
app.title("Olympic")
can = Canvas(app, width=335, height=200, bg="white")
can.pack(side=TOP, padx=5, pady=5)

b1 = Button(app, text="Quitter", command=app.quit)
b1.pack(side=RIGHT, pady=3, padx=10)
b2 = Button(app, text="Effacer", command=effacer)
b2.pack(side=RIGHT)
# Dessiner les 5 anneaux grace aux bouttons
Button(app, text=1, command=c1).pack(side=LEFT, padx=5)
Button(app, text=2, command=c2).pack(side=LEFT, padx=5)
Button(app, text=3, command=c3).pack(side=LEFT, padx=5)
Button(app, text=4, command=c4).pack(side=LEFT, padx=5)
Button(app, text=5, command=c5).pack(side=LEFT, padx=5)
Button(app, text="Tout", command=tout).pack(side=LEFT, padx=5)

app.mainloop()