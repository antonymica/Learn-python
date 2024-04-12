#coding:utf-8
from tkinter import *
from random import randint

# Fonction principal pour les déplacement
def deplacement(gd, hd):
    global x1, y1, x2, y2, distance
    x1, y1, x2, y2 = x1+gd, y1+hd, x2+gd, y2+hd
    can1.coords(terre, x1, y1, x1+40, y1+40)
    can1.coords(lune, x2, y2, x2+15, y2+15)

    separation = randint(-2, 2)
    distance = distance + separation
    gravitation = (6.67 * 10**-11) * (mlune*mterre) / (distance**2)


def coord(event):
    can1.coords(terre, event.x1, event.y1, event.x1 + 40, event.y1 + 40)
    can1.coords(lune, event.x2, event.y2, event.x2 + 15, event.y2 + 15)

# Fonctions des deplacements
def gauche():
    deplacement(-10, 0)

def droite():
    deplacement(10, 0)

def haut():
    deplacement(0, -10)

def bas():
    deplacement(0, 10)



# ----------Programma principal----------- #

x1, y1, x2, y2 = 10, 10, 50, 50         # Position initiale
distance = 40
mlune = 1500
mterre = mlune * 20


# Création de la fenêtre
app = Tk()
app.title("Astres en mouvement")

# Création des contenues du fenêtre

# Canevas
can1 = Canvas(app, width=400, height=400, bg="brown")
terre = can1.create_oval(x1, y1, x1+40, y1+40, width=2, fill='Blue')
lune = can1.create_oval(x2, y2, x2+15, y2+15, width=2, fill='white')
can1.bind("<Button-1>", coord)
can1.pack(side=LEFT)

# Boutton
Button(app, text="Quitter", command=app.quit).pack(side=BOTTOM)
Button(app, text="Gauche", command=gauche).pack()
Button(app, text="Droite", command=droite).pack()
Button(app, text="Haut", command=haut).pack()
Button(app, text="Bas", command=bas).pack()

# Les données :
Dist = Label(app)
Masse = Label(app)
Grave = Label(app)

Dist.pack(side=TOP)
Masse.pack(side=TOP)
Grave.pack(side=TOP)

# Démarage
app.mainloop()