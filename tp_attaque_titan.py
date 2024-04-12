#coding:utf-8

# J'importe un module le "random" pour choisir des hasards

import random

def saisi_joueur(n):
    nom = input(f"Entrer le pseudo du joueur {n} : ")
    return nom


joueur1 = ""
joueur1_hp = 250

joueur2 = ""
joueur2_hp = 250

random_attack = True
random_dammage = 0

# Commencer le jeu
print("attaque des titans".center(50, "-").upper())
joueur1 = saisi_joueur(1)
print(f"Bienvenue dans le jeu {joueur1}, vous avez {joueur1_hp} HP.")
joueur2 = saisi_joueur(2)
print(f"Bienvenue dans le jeu {joueur2}, vous avez {joueur2_hp} HP.")
print("Pressez 'ENTER' pour commencer le jeu")
# Boucle pour attaquer
input()
i = 0
while i < 2:
    i += 1
    random_attack = random.randint(0, 1)
    random_attack = bool(random_attack)
    random_dammage = random.randint(0, 100)

    print(f"{joueur1}={joueur1_hp}\t{joueur2}={joueur2_hp}")
    print(f"Attaque de {joueur1}...")

    if random_attack:
        # Attaque réussi
        print(f"Attaque réussi, avec dégat: {random_dammage}")
        joueur2_hp -= random_dammage
        print(f"{joueur2} perd {random_dammage} HP")
    else:
        # Attaque échouer
        print(f"Attaque échoué, pas de dégat.")
    input()

    random_attack = random.randint(0, 1)
    random_attack = bool(random_attack)
    random_dammage = random.randint(0, 100)

    print(f"{joueur1}={joueur1_hp}\t{joueur2}={joueur2_hp}")
    print(f"Attaque de {joueur2}...")

    if random_attack:
        # Attaque réussi
        print(f"Attaque réussi, avec dégat: {random_dammage}")
        joueur1_hp -= random_dammage
        print(f"{joueur1} perd {random_dammage} HP")
    else:
        # Attaque échouer
        print(f"Attaque échoué, pas de dégat.")
    input()

# Fin du combat
print("fin du combat".capitalize())
print(f"{joueur1} à {joueur1_hp} HP")
print(f"{joueur2} à {joueur2_hp} HP")

if joueur1_hp < joueur2_hp:
    print(f"{joueur2} a gagné le combat.")
else:
    print(f"{joueur1} a gagné le combat.")
