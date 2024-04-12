#coding:utf-8

# Liste des mois avec les jours qui conviennent
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
nbr_mois = len(t1)
i = 0
while i < nbr_mois:
    i += 1
    t3.append(t2[i-1])
    t3.append(t1[i-1])

print(t3)

for k in t2:
    print(k, end=" ")