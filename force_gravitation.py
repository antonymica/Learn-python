#coding:utf-8

print("le force de gravitation".center(50, "-").upper())

masse = 10000
distance = 0.05

F = 0

F = (6.67 * (10**-11)) * (masse*masse) / (distance*distance)
print("La Force de gravitation est de : {}N".format(F))