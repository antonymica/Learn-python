#coding:utf-8

chaine = input("Entrer une phrase :\n>")
long = len(chaine)
i = 0
while i < long:
    print("{}*".format(chaine[i]), end="")
    i += 1