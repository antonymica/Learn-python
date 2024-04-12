#coding:utf-8

# -------- CONVERSION EXO 8-16 --------- #

from tkinter import *

def convFar(event):
    "Valeur de cette temperature, exprimée en dégrés Fahrenheit"
    tF = eval(champTC.get())
    varTF.set(str(tF*1.8+32))

def convCel(event):
    "Valeur de cette temperature en dégré Celsius"
    tC = eval(champTF.get())
    varTC.set(str((tC-32)/1.8))

fen = Tk()
fen.title('Fahrenheit/Celsius')

Label(fen, text='Temp. Celsius :').grid(row=0, column=0)
# "Variable tkinter" assossier au champ d'entrer. Cet "objet-variable"
# assure l'interface entre TCL et Python (voir notes, page 165) :
varTC = StringVar()
champTC = Entry(fen, textvariable=varTC)
champTC.bind("<Return>", convFar)
champTC.grid(row=0, column=1)
# Initialisation du contenude la variable tkinter :
varTC.set("100.0")

Label(fen, text='Temp. Fahrenheit :').grid(row=1, column=0)
varTF = StringVar()
champTF = Entry(fen, textvariable=varTF)
champTF.bind("<Return>", convCel)
champTF.grid(row=1, column=1)
varTF.set("212.0")

fen.mainloop()