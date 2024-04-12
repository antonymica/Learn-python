#coding:utf-8

# Le nombre de secondes est fourni au depart :
# (un grand nombre s'impose !)
nsd = int(input("Donner le nombre de second : "))

# Nombre de second dans une journée :
nspj = 3600 * 24

# Nombre de second dans un an (soit 365 jours - 
# on ne tiendra pas compte des années bissextilles) :
nspa = nspj * 365

# Nombre de secondes dans un mois (en admettant
# pour chaque mois une durée identique de 30 jours) :
nspm = nspj * 30


# Nombre d'année contenues dans la durée fournie :
na = nsd // nspa			# division "entière"
nsr = nsd % nspa			# n. de sec restantes

# Nombre de mois restants :
nmo = nsr // nspm
nsr = nsr % nspm

# Nombre de jours restants :
nj = nsr // nspj
nsr = nsr % nspj

# Nombre d'heures restants :
nh = nsr // 3600
nsr = nsr % 3600

# Nombre de minutes restants :
nmi = nsr // 60
nsr = nsr % 60

print("Nombre de secondes à convertir :", nsd)
print("Cette durée correspond à", na, "années de 365 jours, plus")
print(nmo, "mois de 30 jours,", end=" ")
print(nj, "jours,",end=" ")
print(nh, "heurs,",end=" ")
print(nmi, "minutes,",end=" ")
print(nsr,"secondes.")
