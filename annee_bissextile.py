#coding:utf-8

print("ANNEE BISSEXTILE OU PAS".center(50, "-"))
annee = int(input("Enter l'année : "))

if (annee % 4):
    print(f"Cette année {annee} n'est pas bissextile")
elif annee % 100 == 0:
    print(f"Cette année {annee} n'est pas bissextile")
    if annee % 400 == 0:
        print(f"Cette année {annee} est bissextile")
else:
    print(f"Cette année {annee} est bissextile")
