#coding:utf-8

nbc = input("Combien de photocopie voulez-vous faire?\n")
nbc = int(nbc)

P1 = 2
P2 = 1.5
P3 = 1

if nbc <= 10:
    montant = nbc * P1
elif nbc <= 30:
    montant = P1 * 10 + P2 * (nbc - 10)
else:
    montant = P1 * 10 + P2 * 20 + P3 * (nbc - 30)

print("Vous devez payer {} ariary".format(montant))