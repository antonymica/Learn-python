#config:utf-8
from tkinter import *
from random import randrange

def damier():
    " Dessiner dix lignes de carré avec decalage alterné "
    y = 0
    while y < 10:
        if y % 2 == 0:      #une fois sur deux , on commence la ligne
            x = 0           #de carré avec un decalage de la taille
        else:               #d'un carré
            x = 1
        carre(x*c, y*c)
        y += 1

def carre(x, y):
    " Dessiner une ligne de carré, en partant de x et y "
    i = 0
    while i < 5:
        can.create_rectangle(x, y, x+c, y+c, fill='navy')
        i += 1
        x += c*2            # espacer les carré

def cercle(x, y, r, coul):
    " Dessiner un cercle de centre (x, y) et de rayon r "
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)

def pion():
    " Dessiner un pion au hasard sur le damier "
    # tirer au hasard les coordonnées du pion
    x = c/2 + randrange(10) * c
    y = c/2 + randrange(10) * c
    cercle(x, y, c/3, 'red')

# PROGRAMME PRINCIPAL
c = 30
app = Tk()
app.title("Damier")
can = Canvas(app, width=c*10, height=c*10, bg="ivory")
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(app, text='Damier', fg="Chocolate", command=damier)
b1.pack(side=LEFT, pady=3, padx=10)
b2 = Button(app, text='Pion', fg="Chocolate", command=pion)
b2.pack(side=RIGHT, pady=3, padx=10, ipadx=8)
app.mainloop()