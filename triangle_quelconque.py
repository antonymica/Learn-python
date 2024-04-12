#coding:utf-8

from math import sqrt

# Programme de calcul AIR et PERIMETRE d'un Triangle quelconque
bienvenu = "Entrer les côtés du triangle"
bienvenu.upper()
bienvenu = bienvenu.center(50, "~")
print(bienvenu)

a_cote = float(input("Un côté : "))
b_cote = float(input("Un côté : "))
c_cote = float(input("Un côté : "))

# Calcul du périmètre
perimetre = (a_cote + b_cote + c_cote)
# Calcul du demi-périmètre
demi_perimetre = perimetre / 2
# Calcul d'air
air = sqrt(demi_perimetre*(demi_perimetre-a_cote)*\
    (demi_perimetre-b_cote)*(demi_perimetre-c_cote))

print("L'Air de ce tringle : {}\nLe périmètre de ce triangle : {}".format(air, perimetre))



