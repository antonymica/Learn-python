#coding:utf-8
# -------------- PASSAGE PIETONS ET FEUX DE CIRCULATION ----------------- #
from tkinter import *

# Création du fenêtre principal
fen = Tk()
fen.title("Passage Pietons")

# Creation du canevas
can = Canvas(fen, width=400, height=400, bg='white')
can.pack(side=TOP, padx=3, pady=3)
# Création du bouton 'Changer' dans fen
Button(fen, text='Change').pack(side=RIGHT, ipady=3, ipadx=3, padx=15, pady=3)

# Création du rectangle gris foncé et les deux cotes
rect = Canvas(can, width=200, height=400, bg="darkgray")
rect.grid(row=1, column=1)
cote1 = Canvas(can, width=100, height=400, bg='white')
cote1.grid(row=1, column=0, padx=0)
cote2 = Canvas(can, width=100, height=400, bg='white')
cote2.grid(row=1, column=2, padx=0)

# Création de la voie clouté



# Boucle de demarage
fen.mainloop()