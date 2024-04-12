#coding:utf-8

from dessins_tortue import *

up()                    # relever le crayon
goto(-250, 50)          # reculer en haut à gauche

# Dessiner dix carrés rouges, alignés :
i = 0

taille = 25

while i < 5:
    down()              # abaisser le crayon
    carre(taille, 'red', 30)    # tracer un carré
    up()                # relever le crayon
    forward(50+i+i)         # avancer + loin
    down()
    triangle(taille, 'yellow', 30)
    up()
    forward(50+i+i)
    down()
    etoile5(taille, 'black')
    up()
    forward(50+i+i)
    i += 1
    taille += 5
a = input()             # attendre