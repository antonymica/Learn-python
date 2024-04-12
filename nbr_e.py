#coding:utf-8

chaine = input("Entrer une phrase :\n>")
compte = 0
for i in chaine:
    if i == "e":
        compte += 1
print("Le nombre de 'e' dans cette phrase est :", compte)