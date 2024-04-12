import random

# Caractères
lettre = "MICAEL"
nombre = "1234567890"
symboles = "()[]_/!=%*{}"
caracteres = lettre + lettre.lower() + nombre + symboles
caracteres_no_symboles = lettre + lettre.lower() + nombre 

generer_mdp = True

while generer_mdp:
    longueurmdp = int(input("Entrer la longueur du mot de passe : "))
    nombremdp = int(input("Entrer le nombre du mot de passe à générer : "))
    caracteres_speciaux_ask = str(input("Dois-je mettre des caractères speciaux?\>"))

    if caracteres_speciaux_ask == "oui" or caracteres_speciaux_ask == "o" or caracteres_speciaux_ask == "OUI" or caracteres_speciaux_ask == "O":
        for i in range(0, nombremdp):
            mdp = ""
            for i in range(0, longueurmdp):
                cmdp = random.choice(caracteres)
                mdp = mdp + cmdp
            print("Voici votre mot de passe :",mdp)
    elif caracteres_speciaux_ask == "non" or caracteres_speciaux_ask == "n" or caracteres_speciaux_ask == "NO" or caracteres_speciaux_ask == "N":
        for i in range(0, nombremdp):
            mdp = ""
            for i in range(0, longueurmdp):
                cmdp = random.choice(caracteres_no_symboles)
                mdp = mdp + cmdp
            print("Voici votre mot de passe :",mdp)
    else:
        print("ERREUR!!!")
        break
    generer_mdp = False