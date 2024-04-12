#coding:utf-8

import math

nombre = float(input("Entrer un nombre : "))
if nombre < 0:
    print("La racine carre de ce nombre ne peut-être calculer")
else:
    print("La racine carre de {} est : {}".format(nombre, math.sqrt(nombre)))