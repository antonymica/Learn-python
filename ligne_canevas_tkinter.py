#config:utf-8

from tkinter import *
from random import randrange

# Définir les fonctions
def draw_line():
    "Tracer une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_rectangle(x1, y1, x2, y2, width=5, fill=coul)
    "Modification des coordonnée de chaque ligne suivante"
    y2, y1 = y2+10, y1-10

def draw_lin2():
    "Tracer une ligne horizontale et verticale"
    global z1, z2, w1, w2, h1, h2, f1, f2
    can1.create_line(z1, z2, w1, w2, h1, h2, f1, f2, width=5, fill='red')

def change_color():
    "Changement aléatoire des couleurs tracés"
    global coul
    pal = ["yellow", "cyan", "orange", "maroon", "crimson", "green", "brown"]
    c = randrange(8)
    coul = pal[c]


# PROGRAMME PRINCIPAL

# Les variables svt seront utilisées de manière global:
x1, y1, x2, y2 = 0, 390, 390, 0
z1, z2, w1, w2, h1, h2, f1, f2 = 250, 200, 0, 200, 200, 200, 200, 0
coul = 'blue'

# Création du widget principal
fen1 = Tk()
# Création des widgets "esclaves"
can1 = Canvas(fen1, bg='dark gray', width=500, height=500)
can1.pack(side=LEFT)
bout1 = Button(fen1, text="Quitter", fg="black", command=fen1.destroy)
bout1.pack(side=BOTTOM)
bout2 = Button(fen1, text='Tracer une ligne', command=draw_line)
bout2.pack()
bout3 = Button(fen1, text='Autre couleur', command=change_color)
bout3.pack()
bout4 = Button(fen1, text='Viseur', command=draw_lin2)
bout4.pack()

fen1.mainloop()      # Démarage de receptonneu d'évenement
#fen1.destroy()       # Destruction (fermeture) de le fenetre