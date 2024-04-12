#coding:utf-8

D = float()
n = int()
a = int()
borne = [1234, 1235]
i = 1232
j = 0
print("Commence...")
while i < 10000000:
    i += 1
    a = i
    while j < 10:
        j += 1
        n = j
        D = a / (2**n)
        if borne[0] < D < borne[1]:
            print(f"Le nombre est : {D}")
print("Terminer...")