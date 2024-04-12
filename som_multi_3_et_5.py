#coding:utf-8

borne = input("Entrer la borne séparé par un virgule svp : ")
borne = list(eval(borne))

if borne[0] > borne[1]:
    echange = borne[0]
    borne[0] = borne[1]
    borne[1] = echange
resultat = 0
resultat2 = 0
for i in range(borne[0], borne[1], 1):
    if (i % 3 == 0) and (i % 5 == 0):
        resultat += i
    if (i % 3 == 0) or (i % 5 == 0):
        resultat2 += i

print(f"La somme de multiple de 3 et 5 \
        \ndans l'intervalle [{borne[0]};{borne[1]}] est {resultat}")

print(f"La somme de multiple de 3 ou 5 \
        \ndans l'intervalle [{borne[0]};{borne[1]}] est {resultat2}")