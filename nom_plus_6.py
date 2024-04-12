#coding:utf-8

# Triage des Noms plus de 6 caractéres
noms = ["Jean", "Micael", "Antonie", "Brigitte", "Sonia", "Tiana", "Jean-Pierre", "Sandra"]

plus = []
moin = []

for i in noms:
    if len(i) >= 6:
        plus.append(i)
    else:
        moin.append(i)

print("Plus de 6 sont : {}\nMoins de 6 sont : {}".format(plus, moin))