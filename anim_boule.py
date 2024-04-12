#coding:utf-8
from tkinter import *

# Fonction principal pour les déplacement
def deplacement(gd, hd):
    global x1, y1
    x1, y1 = x1+gd, y1+hd
    can1.coords(boule,x1, y1, x1+30, y1+30)

# Fonctions des deplacements
def gauche():
    deplacement(-10, 0)

def droite():
    deplacement(10, 0)

def haut():
    deplacement(0, -10)

def bas():
    deplacement(0, 10)


# -----------Programme principal------------- #

x1, y1 = 10, 10

# Création fenêtre
app = Tk()
app.title("Animation Boule")

# Création d'un 'Canvas'
can1 = Canvas(app, width=300, height=300, bg='yellow')
boule = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
can1.pack(side=LEFT)

Button(app, text='Quitter', command=app.quit).pack(side=BOTTOM)
Button(app, text="Gauche", command=gauche).pack()
Button(app, text="Droite", command=droite).pack()
Button(app, text="Haut", command=haut).pack()
Button(app, text="Bas", command=bas).pack()

# Demarage
app.mainloop()