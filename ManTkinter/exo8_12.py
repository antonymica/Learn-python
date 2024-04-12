#coding:utf-8

# ---------- ASTRES EXO 8.12 ----------- #

from tkinter import *
from math import sqrt

def distance(x1, y1, x2, y2):
    "Distance séparant les points x1,y1 et x2,y2"
    d = sqrt((x2-x1)**2 + (y2-y1)**2)           # Théorème de pythagore
    return d

def forceG(m1, m2, di):
    "Force de gravitation séexerçant entre m1, m2 pour une distance di"
    return m1*m2*6.67e-11/di**2

def avance(n, gd, hb):
    "Deplacement de l'astre n, de gauche à droite ou de haut en bas"
    global x, y, step
    # Nouvelles coordonnées :
    x[n], y[n] = x[n]+gd, y[n]+hb
    # Deplacement du dessin dans le canevas :
    can.coords(astre[n], x[n]-10, y[n]-10, x[n]+10, y[n]+10)
    # Calcul de la nouvelle interdistance
    di = distance(x[0], y[0], x[1], y[1])
    # Conversion de la distance "écran" en distance "astronomique"
    diA = di*1e9        # (1pixel -- 1million de Km)
    # Calcul de la force de gravitation correspondante
    f = forceG(m1, m2, diA)
    # Affichage des nouvelles valeurs de distance et force :
    valDis.configure(text="Distance = " +str(diA) +"Km")
    valFor.configure(text="Force = " +str(f) +"N")
    # Adaptation du "pas" de deplacement en fonction de la distance :
    step = di/10

def gauche1():
    avance(0, -step, 0)

def droite1():
    avance(0, step, 0)

def haut1():
    avance(0, 0, -step)

def bas1():
    avance(0, 0, step)

def gauche2():
    avance(1, -step, 0)

def droite2():
    avance(1, step, 0)

def haut2():
    avance(1, 0, -step)

def bas2():
    avance(1, 0, step)

# ---------- PROGRAMME PRINCIPAL ----------- #

# Masse des deux astres :
m1 = 6e24           # (Valeur de la terre, en Kg)
m2 = 6e24           #
astre = [0]*2       # Liste servant à mémoriser les références des dessins
x = [50., 350.]     # Liste des coord. X de chaque astre (à l'écran)
y = [100., 100.]    # Liste des coord. Y de chaque astre
step = 10           # "Pas" de deplacement initial


# Construction de la fenêtre :
fen = Tk()
fen.title("Gravitation universelle suivant Newton")
fen.resizable(width=False, height=False)

# libéllés :
valM1 = Label(fen, text="M1 = " +str(m1) +"Kg")
valM1.grid(row=1, column=0)
valM2 = Label(fen, text="M2 = " +str(m2) +"Kg")
valM2.grid(row=1, column=1)
valDis = Label(fen, text="Distance")
valDis.grid(row=3, column=0)
valFor = Label(fen, text='Force')
valFor.grid(row=3, column=1)

# Canevas avec le dessin des 2 astres:
can = Canvas(fen, bg="light yellow", width=400, height=200)
can.grid(row=2, column=0, columnspan=2)
astre[0] = can.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10, fill="red", width=1)
astre[1] = can.create_oval(x[1]-10, y[1]-10, x[1]+10, y[1]+10, fill="blue", width=1)

# 2 groupes de 4 boutons, chacun installé dans un cadre (frame)
fra1 = Frame(fen)
fra1.grid(row=4, column=0, sticky=W, padx=10)
Button(fra1, text="<", fg="red", command=gauche1).pack(side=LEFT)
Button(fra1, text=">", fg="red", command=droite1).pack(side=RIGHT)
Button(fra1, text="^", fg="red", command=haut1).pack(side=TOP)
Button(fra1, text="v", fg="red", command=bas1).pack(side=BOTTOM)
fra2 = Frame(fen)
fra2.grid(row=4, column=1, sticky=E, padx=10)
Button(fra2, text="<", fg="red", command=gauche2).pack(side=LEFT)
Button(fra2, text=">", fg="red", command=droite2).pack(side=RIGHT)
Button(fra2, text="^", fg="red", command=haut2).pack(side=TOP)
Button(fra2, text="v", fg="red", command=bas2).pack(side=BOTTOM)

fen.mainloop()






