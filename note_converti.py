#coding:utf-8

stop = False
a = "Appréciation"
print("Ecrire '101' pour arrêté".title())
while not stop:
    note = float(input("Entrer une note : "))
    if note == 101:
        stop = False

    if 100 > note >= 80:
        print(f"{a} A")
    elif 80 > note >= 60:
        print(f"{a} B")
    elif 60 > note >= 50:
        print(f"{a} C")
    elif 50 > note >= 40:
        print(f"{a} D")
    elif 40 > note >= 0:
        print(f"{a} E")
    else:
        break