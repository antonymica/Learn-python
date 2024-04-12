#coding:utf-8

# Trier les nombres pairs et impairs
ma_liste = [12, 23, 34, 44, 33, 0, 32, 45, 98, 93]
pair = []
impair = []

for i in ma_liste:
    if i % 2 == 0:
        pair.append(i)
    else:
        impair.append(i)

print("Pair =",pair ,"\nImpair =",impair)