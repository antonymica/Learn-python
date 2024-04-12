#coding:utf-8

"""
Un petit programme simple en python qui affiche le suite de fibonacci, 
c-à-d une suite de nombre dont chaque terme est egal à la somme des deux précédent
"""

a, b, i = 1., 2., 1                     # a et b sevrent au calcul des termes successifs
									  # i pour l'iteration
print(b)							  # on affiche le premier terme
while i < 50:						  # affichage de 15 terme au total
	a, b, i = b, a*b, i+1
	print(i ,":", b, type(b))