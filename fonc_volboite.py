#coding:utf-8

def volBoite(larg=10, long=10, haut=10):
    if larg == long == haut == None:
        return -1
    else:
        return larg * long * haut

print("Volume d'une boîte".center(70, "-").upper())
largeur = float(input("Donner la largeur : "))
longueur = float(input("Donner la longueur : "))
hauteur = float(input("Donner la hauteur : "))
volume = volBoite(largeur, longueur)
print(f"Volume de cette boîte est : {volume}")
print(f"Volume de cette boîte est : {volume}")