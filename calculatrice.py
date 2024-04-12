#coding:utf-8

# Les couleurs:
# Noir: #101419
# Bleu: #476C9B
# Rouge: #984447

"""
789*
456-
123+
0,/=
"""

from tkinter import *

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return
    global expression
    expression += str(touche)
    equation.set(expression)

def calculer():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("Erreur")
        equation.set("")

def effacer():
    global expression 
    expression = ""
    equation.set("")

gui = Tk()
    
# Couleur de fond
gui.configure(background="#101419")

# Titre de l'application
gui.title("Calculatrice")

# Taille de la fenêtre
gui.geometry("245x397+100+100")
gui.resizable(width=False, height=False)

# Variable pour stocker le contenu actuel
equation = StringVar()

# Boite de resultats
resulta = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height="4")
resulta.grid(columnspan=4)

# Bouttons
boutons = [7, 8, 9, "*",4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
ligne = 1
colonne = 0

for bouton in boutons:
    b = Label(gui, text=str(bouton), cursor="spider" , bg="#476C9B", fg="#FFF", height=4, width=8)
    # Rendre le texte cliquable
    b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

    b.grid(row=ligne, column=colonne)

    colonne += 1
    if colonne == 4:
        colonne = 0
        ligne += 1

b = Label(gui, text="Effacer", bg="#984447", fg="#FFF",cursor="spider", height=4, width=34)
b.bind("<Button-1>", lambda e: effacer())
b.grid(columnspan=4)


gui.mainloop()



