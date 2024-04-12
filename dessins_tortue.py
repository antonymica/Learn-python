#coding:utf-8

from turtle import *
from math import pi

def carre(taille, couleur):
    "Voici un fonction qui dessine un carré de taille et couleur détérminer"
    color(couleur)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c += 1


def triangle(taille, couleur):
    "Voici une fonction qui dessine un triangle équilatéral"
    color(couleur)
    c = 0
    while c < 3:
        forward(taille)
        right(120)
        c += 1

def etoile5(taille, couleur):
    "Ceci est une fonction qui dessine une étoile"
    color(couleur)
    c = 0
    while c < 5:
        forward(taille)
        right(145)
        c += 1

def etoile6(taille, couleur):
    "Ceci est une fonction qui dessine une étoile à 6 branches"
    color(couleur)
    c = 0
    while c < 6:
        forward(taille)
        left(60)
        forward(taille)
        right(120)
        c += 1
