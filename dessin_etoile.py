#coding:utf-8

from dessins_tortue import *

print("C'est un programme qui fait appelle à un module pour dessiner une étoile")

up()
x = -300
y = 50
goto(x, y)

i = 0
long = 20

while i < 5:
    down()
    etoile5(long, 'blue')
    up()
    x += 50
    goto(x, y)
    i += 1
    long += 5
k = 0
while k < 5:
    down()
    etoile5(long, 'blue')
    up()
    x += 50
    goto(x, y)
    k += 1
    long -= 5
input()