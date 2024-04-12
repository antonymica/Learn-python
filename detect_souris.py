#coding:utf-8
from tkinter import *
from random import *

def cercle(x, y, r=15, coul='black'):
    " Tracer un cercle de centre au coordonnée (x,y), de rayon r et de couleur coul"
    cadre.create_oval(x-r, y-r, x+r, y+r, outline=coul)

def pointeur(event):
    couleur = ['red', 'blue', 'orange', 'purple', 'crimson', 'green', 'chocolate', 'brown']
    color = choice(couleur)
    chaine.config(text = "Clic détécté en X =" + str(event.x) + ", Y =" + str(event.y))
    cercle(event.x, event.y, coul=color)

app = Tk()
app.title("Au Clic")
app.geometry("250x400+600+200")
cadre = Canvas(app, width=250, height=350, bg="light yellow")
cadre.bind("<Button-1>", pointeur)  # <Button-1> : clic gauche, <Button-3> : clic droit, <Button-2> : clic roulette, <Button> : les trois
cadre.pack()
chaine = Label(app)
chaine.pack()
mainloop()