#coding:utf-8


mois = input("Donner le numero du mois (1--12) : ")
mois = int(mois)

if mois in [3,5]:
    print("PRINTEMPS")
elif mois in [6,8]:
    print("ETE")
elif mois in [9,11]:
    print("AUTOMNE")
else:
    print("HIVER")
