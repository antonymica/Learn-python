#coding:utf-8

from math import sqrt

print("\n\nRESOLUTION EQUATION DANS IR\n\nForme ax²+bx+c=0\n")

a = float(input("Entrer a : "))
b = float(input("Entrer b : "))
c = float(input("Entrer c : "))

if a == 0:
	print("\n\nL'équation est du 1er dégré:\n")
	if b == 0:
		if c == 0:
			print("Solution IR.\n")
		else:
			print("Pas de solution!\n")
	else:
		solution = -c / b
		print("Solution : S=({})\n".format(solution))
else:
	print("\n\nL'équation est du 2nd dégré:\n")
	delta = b*b - 4*a*c
	if delta > 0:
		print("On a deux solution distinct: x1 et x2")
		x1 = (-b - sqrt(delta))/2*a
		x2 = (-b + sqrt(delta))/2*a
		print("Solution : S=({},{})\n".format(x1, x2))	
	elif delta == 0:
		solution = -b / 2*a
		print("Solution : S=({})\n".format(solution))
	else:
		print("Pas de solution!\n")
