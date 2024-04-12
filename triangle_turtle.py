#coding:utf-8

import turtle

def equilateral(couleur):
    turtle.color(couleur)
    turtle.forward(150)
    turtle.left(120)

turtle.screensize(400, 500, "brown")

i = 1

while i < 15:
    equilateral("yellow")
    equilateral("blue")
    equilateral("orange")
    turtle.up()
    turtle.forward(-50)
    turtle.down()
    i += 1
