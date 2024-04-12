#coding:utf-8

def somme():
    entier = input("Donner un entier pour la somme : ")
    entier = int(entier)
    sum = 0
    for i in entier:
        sum += 1
    print("La somme des {} premiers nombres est {}".format(entier, sum))

somme()