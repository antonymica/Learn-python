#coding:utf-8

# Programme qui boucle l'entrer d'un valeur et affiche ces valeur
mes_nombre = []
valeur = True
while valeur:
    ni = input("Veuillez entrer une valeur : ")
    if ni == "":
        print("Vous n'avez rien saisi!")
        valeur = False
    else:
        mes_nombre.append(ni)

for i in mes_nombre:
    print(i, end="|")

