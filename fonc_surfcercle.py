#coding:utf-8

from math import pi

def surfCercle(r):
    air = pi * r * r
    return air

print("surface d'un cercle".center(70, "-"))
rayon = float(input("Entrer le rayon du cercle (en m) : "))
surface = surfCercle(rayon)
print(f"La surface de ce cercle est : {surface} m²")