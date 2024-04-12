#coding:utf-8

def compteCar(car, ch):
    cmp = 0
    for i in ch:
        if i == car:
            cmp += 1
    return cmp

def indexMax(liste):
    maxim = liste[0]
    for i in liste:
        if maxim <= i:
            maxim = i
    return maxim

def nomMois(n):
    mois = ["Commencer par 1", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    return mois[n]


def inverser(ch):
    rev = ""
    long = len(ch)
    while long > 0:
        rev = rev + ch[long-1]
        long -= 1
    return rev

def compteMot(ph):
    cmp = 0
    for i in ph:
        if i in [" ", "-", "'"]:
            cmp += 1
    return cmp

texte = "Je m'appelle Mica, demain c'est mon anniversaire. Est-ce que vous me donneriez un cadeau"
liste_anniv = [11, 14, 16, 18, 24, 15, 10, 8, 10, 29, 19]
nom = "Antony"

nbr_e = compteCar("e", texte)
print(f"Nombre de 'e' dans le texte : {nbr_e}")

mois_d_anniv = nomMois(1)
print(f"Mon anniv est le mois de {mois_d_anniv}")

plus_grand = indexMax(liste_anniv)
print(f"Le jour d'anniv le plus grand est {plus_grand}")

nbr_mot = compteMot(texte)
print(f"Le nombre de mot dans ce texte est {nbr_mot}")

inverse = inverser(nom)
print(f"Mon prénom inverse est {inverse}")