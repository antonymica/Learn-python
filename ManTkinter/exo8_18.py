#coding:utf-8

# --------- COURBE DE LISSAJOUS --------- #

from tkinter import *
from math import sin, cos
from time import sleep

def move():
    global ang, x, y
    # On mémorise les coordonnées precédentes avant de calculer les nouvelles :
    xp, yp = x, y
    # Rotation d'un angle de 0.1 radian
    ang = ang + .1
    # Sinus et Cosinus de cet angle -- coord. d'un point du cercle trigo
    # x, y = sin(ang), cos(ang)
    # Variante déterminant une courbe de Lissajous avec f1/f2 = 2/3 :
    x, y = sin(2*ang), cos(3*ang)
    # mise à l'echelle (120 = rayon du cercle, (150,150) = centre de canevas)
    x, y = x*120+150, y*120+150
    can.coords(balle, x-10, y-10, x+10, y+10)
    can.create_line(xp, yp, x, y, fill="blue")      # trace la trajectoire

# ----------- PROGRAMME PRINCIPAL ------------ #

ang, x, y = 0., 150., 270.
fen = Tk()
fen.title("Courbes de Lissajous")
can = Canvas(fen, width=300, height=300, bg="white")
can.pack()
balle = can.create_oval(x-10, y-10, x+10, y+10, fill="red")
Button(fen, text="Go", command=move).pack()
fen.mainloop()




