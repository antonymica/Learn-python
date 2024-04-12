x#coding:utf-8

"""Algorithme Carre"""

def carre(cote1, cote2):
	return cote1 * cote2

cote_carre = input("Entrer la longueur du côté du carré ici : ")
cote_carre = float(cote_carre)

resultat = carre(cote_carre, cote_carre)

print("La surface du carré est {} cm²".format(resultat))