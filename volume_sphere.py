#coding:utf-8

import math

pi = math.pi

def cube(w):
    return w*w*w

def volumesphere(r):
    return 4 * pi * cube(r) / 3

print("volume d'un sphère".center(70, "-").upper())

rayon = float(input("Entrer le rayon (cm): "))
print("Le volume est : {}cm".format(volumesphere(rayon)))