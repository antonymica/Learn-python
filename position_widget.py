#coding:utf-8

import tkinter
# création et parametrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x400")
app.title("Positionnement widget")

# Widgets...
"""
# mainframe = tkinter.Frame(app, width=300, height=200, borderwidth=1)

mainframe = tkinter.LabelFrame(app, text="Titre du cadre")
mainframe.pack()

btn = tkinter.Button(mainframe, text="BIENVENUE") # Soloina mainframe le app raha toa ka atao ao anatiny le btn
btn.pack()
"""
label = tkinter.Label(app, text="Un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app, text="BIENVENUE")
"""
Propriété de pack() : side=" " / top, bottom, left, right / ex: side="top"
                      expand= bool / 1 ou 0 /
                      fill=" " / y ou x  ou both/ # Remplir
                      padx= int # Marge exterieur
                      ipad(x ou y)= int # Marge interieur

label.pack(padx=100, pady=50)
ent.pack(side="left", fill="y")
btn.pack(expand=1, padx=100, ipady=50, ipadx=50)

Propriété de grid() : row= int
                      column= int
                      columnpan= int
                      rowspan= int
                      padx= int # Marge exterieur
                      ipad(x ou y)= int # Marge interieur
                      sticky   # Orientation coordonnée / n: nord; s:sud; w:ouest; e: est /

label.grid(row=0, column=0, rowspan=2)
ent.grid(pady=20, ipadx=20)
btn.grid(sticky="se")

Propriété de place() : x= int  # Coodonnée de pixel de l'ecran
                       y= int
                       relx ou rely # Coordonnée relative
"""

btn.pack()

# IL NE FAUT PAS LES UTILISERS ENSEMBLE (grid, pack, place)

# Boucle principal
app.mainloop()