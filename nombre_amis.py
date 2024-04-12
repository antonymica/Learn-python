#coding:utf-8

# Auteur de cette Algorithm : Claude Monteil
# Version : 1.0 - 04-2016

#Variable
max = int()                     # Borne sup
n = int(); m = int()            # Couples
sommeDivsN = int()
sommeDivsM = int()
listeDivsN = str()
listeDivsM = str()
diviser = int()

print("Recherche de couple de nombre amis".upper().center(50, "-"))

# 1. Saisi du nombre max
max = int(input("Borne maximale de recherche : "))

# 2. Chercher et afficher les couples d'amis inf à cette nombre
for n in range(2, max):
    # 2.1. calculer la somme des diviseurs de n
    sommeDivsN = 1
    listeDivsN = 1
    for diviser in range(2, n//2+1):
        if m % diviser == 0:
            sommeDivsN = sommeDivsN + diviser
            listeDivsN = listeDivsN+"+"+str(diviser)
    # 2.2 tester si n peut être amis avec m
    for m in range(n+1, max+1):
        sommeDivsM = 1
        listeDivsM = 1
        for diviser in range(2, m//2+1):
            if m % diviser == 0:
                sommeDivsM = sommeDivsM + diviser
                listeDivsM = listeDivsM+"+"+str(diviser)

            if (m == sommeDivsN) and (n == sommeDivsM):
                print((n, "et", m, "sont amis :"))
                print(" ", n,"=", listeDivsM, "qui sont les diviseurs de",m)
                print(" ", m,"=", listeDivsN, "qui sont les diviseurs de",n)
