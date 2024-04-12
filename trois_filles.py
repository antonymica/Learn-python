#coding:utf-8

produit = 36
moitier = 36 // 2

age1 = []
age2 = []
age3 = []

for i in range(1, moitier, 1):
    for j in range(1, moitier, 1):
        for k in range(1, moitier, 1):
            if (i*j*k) == 36:
                age1.append(i)
                age2.append(j)
                age3.append(k)

for i in age1:
    print(f"Age1 : {i} ", end="|")
print()
for i in age2:
    print(f"Age2 : {i} ", end="|")
print()
for i in age3:
    print(f"Age3 : {i} ", end="|")