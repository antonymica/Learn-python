#coding:utf-8

# Convertion en m/s et km/h le miles/h
vitesse_miles = int(input("Enter votre vitesse en miles/heure : "))

#heure en second
hes = 3600

# miles en mètre
v_metre = vitesse_miles * 1609

# mètre en kilomètre
v_kilo = v_metre / 1000

# calcul de vitesse en m/s
vmps = v_metre / hes

print("Convertion : {} miles/h = {} m/s = {} km/h".format(vitesse_miles, vmps, v_kilo))