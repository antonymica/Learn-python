#coding:utf-8

# Programme qui calcul la periode d'un pendule simple

from math import sqrt, pi

longueur = float(input('Donner la longueur du pendule : '))

g = 10

# Formule T = 2*pi*sqrt(l/g)
# Calucul de la periode

T = 2*pi*sqrt(longueur/g)

# Affichage
print("T = {}s".format(T))

