#coding:utf-8

"""
Convertion dégrés en radians

Rappel : un angle de 1 radian est un angle qui correspond 
à une portion de circonférence de longueur égale à celle du rayon.
Puisque la circonférence vaut 2 pi R, un angle de 1 radian correspond
à 360° / 2 pi , ou encore à 180° / pi
"""

# Angle fourni au départ en dégrés, minute, secondes :
deg, mi, sec = 32, 13, 49

# Conversion des secondes en une fraction de minute :
fm = sec / 60

# Convertion des minutes en une fraction de dégré :
fd = (mi + fm) / 60

# Valeur de l'angle en dégrés "décimalisés" :
ang = deg + fd

# Valeur de pi :
pi = 3.141592653559

# Valeur d'un radian en dégrés :
rad = 180 / pi

# Conversion de l'angle en radian :
arad = ang / rad

# Affichage :
print(deg,"°",mi, "'",sec,'" =', arad, "radian(s)")