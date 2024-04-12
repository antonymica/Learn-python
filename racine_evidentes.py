#coding:utf-8

"""x = int(input("x = "))
p = x**5 + 2 * (x**4) -4 * (x**3) -3 * (x**2) + x + 3
print(p)"""

liste = [-2, 2, -1, 1, 2/3, -2/3, 2/5, -2/5, 1/3, -1/3, -1/5, 1/5, 2/15, -2/15]

for i, y in enumerate(liste):
    p2 = 30* (y**3) -7 * (y**2) -7 * y + 2
    if p2 == 0:
        print(i, ":", y)