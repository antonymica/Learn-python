#coding:utf-8

print("peut-etre un triangle".upper().center(50, "-"))
a = float(input("Entrer un nombre : "))
b = float(input("Entrer un autre nombre : "))
c = float(input("Entrer encore un nombre : "))

if (a or b or c) < 0:
    print("Il y a des nombres négatifs")
    quit()

if a != b != c:
    print("C'est un triangle quelconque")
if ((a == b) != c) or ((a == c) != b) or ((b == c) != a):
    print("C'est un triangle isocéle peut-être aussi rectangle")
if (a**a==b**b+c**c) or (b**b==a**a+c**c) or (c**c==b**b+a**a):
    print("C'est un triangle rectangle")
if a == b == c:
    print("C'est triangle équilateral")