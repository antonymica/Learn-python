#coding:utf-8

# Convertion de second en heure, en minute et en second

second = int(input("Enter le nombre de second à convertir : "))
heure = minute = mois = jours = annee = 0

if second < 60:
	print("Ca fait : {}an(s) {}mois {}jours {}h:{}min:{}s".format(annee, mois, jours, heure, minute, second))
else:
	while second > 60:
		minute = second // 60
		second %= 60
		if minute >= 60:
			heure = minute // 60
			minute %= 60

			if heure >= 24:
				jours = heure // 24
				heure %= 24

				if jours >= 30:
					mois = jours // 30
					jours %= 30

					if mois >= 12:
						annee = mois // 12
						mois %= 12
					else:
						break
				else:
					break
			else:
				break
		else:
			break
print("Ca fait : {}an,{}mois,{}jours_{}h:{}min:{}s".format(annee, mois, jours, heure, minute, second))


