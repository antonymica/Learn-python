#coding:utf-8

def sexe(sex):
    if sex == "m" or sex == "M":
        return "Cher Monsieur"
    elif sex == "f" or sex == "F":
        return "Chère Mademoiselle"
    else:
        return "Kaiza ra"

def saisi():
    nom = input("Entrer votre nom : ")
    genre = input("Entrer votre sexe (M/F) : ")
    return (nom, genre)

nom, genre = saisi()

politesse = sexe(genre)
print(f"{politesse} {nom}")