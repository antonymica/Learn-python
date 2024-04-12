#coding:utf-8
from tkinter import *
from math import *

def evaluer(event):
    chaine.config(text="Résultat = " + str(eval(entrer.get())))

# PROGRAMME PRINCIPAL
app = Tk()
app.title("Calculatrice")
app.geometry("230x50+600+200")
entrer = Entry(app, font="Times")
entrer.bind("<Return>", evaluer)
chaine = Label(app)
entrer.pack()
chaine.pack()
app.mainloop()