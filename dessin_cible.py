#coding:utf-8

""" C'EST UN ALGORITHME QUI DESSINE DEUX FIGURE : UNE CIBLE ET UN CLOONE """
from tkinter import *

def cercle(x, y, r, coul='black'):
    " Tracer un cercle de centre au coordonnée (x,y), de rayon r et de couleur coul"
    can.create_oval(x-r, y-r, x+r, y+r, outline=coul)


def fig1():
    " Tracer la figure en forme de cible "
    # On efface tout ce qu'il y a sur le canvas
    can.delete(ALL)
    # Tracer les deux lignes centrale verticale et horizontale
    can.create_line(100, 0, 100, 200, fill='blue')
    can.create_line(0, 100, 200, 100, fill='blue')
    # Tracer les cercles
    rayon = 15
    while rayon < 100:
        cercle(100, 100, rayon)
        rayon += 15

def fig2():
    " Ceci dessine la figure de cette face de cloune "
    # On efface tout ce qu'il y a sur le canvas
    can.delete(ALL)
    # Il faut d'abord lister les cercles
    cc = [[100, 100, 80, 'red'],    # visage
          [70, 70, 15, 'blue'],     # yeux
          [130, 70, 15, 'blue'],
          [70, 70, 5, 'black'],
          [130, 70, 5, 'black'],
          [44, 115, 20, 'red'],     # joues
          [156, 115, 20, 'red'],
          [100, 95, 15, 'purple'],  # nez
          [100, 145, 30, 'purple'],
          ]
    # on trace touds les cercles à l'aide d'une boucle
    i = 0
    while i < len(cc):
        ch = cc[i]
        cercle(ch[0], ch[1], ch[2], ch[3])
        i += 1

# PROGRAMME PRINCIPAL
app = Tk()
app.title("Dessin")
app.geometry("230x250+600+200")
can = Canvas(app, width=200, height=200, bg="ivory")
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(app, text="Figure1", fg="crimson", command=fig1)
b1.pack(side=LEFT, pady=3, padx=3, ipady=3, ipadx=3)
b1 = Button(app, text="Figure1", fg="crimson", command=fig2)
b1.pack(side=RIGHT, pady=3, padx=3, ipady=3, ipadx=3)
app.mainloop()