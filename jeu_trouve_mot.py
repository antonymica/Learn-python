#coding:utf-8

# JEU : TROUVE MOI LES MOTS #
print()
print("".center(70, "-"))
print(" TROUVE MOI LES MOTS ".center(70, "*").upper())
print("".center(70, "-"))
print("Bienvenu dans le jeu".center(70, " ") .title())

jeu = True

while jeu:
    print("""
    Menu principal:
            1. Jouer
            2. Aide
            3. Quitter
    """)

    def saisi_joueur(n):
        i = 0
        while i < n:
            i += 1
            joueur = input(f"Pseudo du Joueur {i} : ")
            player.append(joueur)
            print(f"Bonjour {joueur}\n")

    theme = ["Cuisine","Salle de classe","Supermarché"]
    le_theme = ""
    lettre = 0
    player = []
    nmpj = []
    choix_menu = int(input("> "))
    choix_theme = 0
    cmp = 0

    if choix_menu == 3:
        quit()

    elif choix_menu == 2:
        print("""
        Comment jouer?
        """)

    elif choix_menu == 1:
        print("Choisir un thême :")

        for i, k in enumerate(theme):
            print(f"\t{i}. {k}")

        choix_theme = int(input("> "))

        if choix_theme == 0:
            le_theme = theme[0]
        elif choix_theme == 1:
            le_theme = theme[1]
        elif choix_theme == 2:
            le_theme = theme[2]
        else:
            print("Erreur de saisi")

        lettre = int(input("Combien de lettre : "))

        nbr_joueur = int(input("\nEntrer le nombre des joueurs: "))
        saisi_joueur(nbr_joueur)

        print("Attention, Début du jeu".center(70, " ").title().upper())

        tour = True
        while tour:
            for k, i in enumerate(player):
                print(f"\nQu'y a t-il dans {le_theme}?")
                mot = input(f"{i}: ")
                if mot == "":
                    continue
                elif len(mot) == lettre:
                    nmpj.append(k)
                elif mot == "quit":
                    tour = False
                    break
                elif len(mot) != lettre:
                    print("Nombre de lettre inexacte!")

        print("Fin du jeu".center(70, " ").upper())
        print("Résultat :")
        for k, i in enumerate(player):
            for j in nmpj:
                if k == j:
                    cmp += 1
            print(f"\t{i} a {cmp} mot(s)")
            cmp = 0
    tohizana = input("Continuer (o/n) : ")
    if tohizana in ("o", "O"):
        continue
    elif tohizana in ("n", "N"):
        jeu = False










    
