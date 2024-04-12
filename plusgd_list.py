#coding:utf-8

# Programme qui affiche le plus grand dans une liste

liste = [12, 34, 1, 98, 84, 34, 5]
pgd = liste[0]
ppt = liste[0]

for i in liste:
    if i < ppt:
        ppt = i
    elif i > pgd:
        pgd = i
    else:
        pass

print("Plus grand : {} \t Plus petit : {}".format(pgd, ppt))