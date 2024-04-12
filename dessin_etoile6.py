#coding:utf-8
import random

print("Dessin étoile 6".center(70, "-").upper())

from dessins_tortue import *

up()
x = -100
y = 340
goto(x, y)
down()

taille = 10
couleur = ["orange", "yellow", "blue", "red", "crimson", "black"]
i = 0
while i < 12:
    down()
    etoile6(taille, random.choice(couleur))
    up()
    forward(100)
    down()
    carre(taille, random.choice(couleur))
    up()
    forward(70)
    right(30+i)
    i += 1
    taille = random.randint(10, 20)
input()