#coding:utf-8

liste = []
cmp = 0
nbr = 0
vita = 2

entrer = True
while entrer:
    n = int(input("Entrer un nombre et termine par 0 : "))
    if n == 0:
        entrer = False
    liste.append(n)

print(liste)

while liste:
    for i in liste:
        liste.remove(i)
        for j in liste:
            if j == i:
                cmp += 1
                nb = i
        if cmp > vita:
            nbr = nb

print(f"Le nombre d'occurence de {nbr} est superieur.")


