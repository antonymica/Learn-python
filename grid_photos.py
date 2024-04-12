#coding:utf-8
from tkinter import *

# Création de la fenêtre
app = Tk()

# Création des Labels et Entry
txt1 = Label(app, text="Premier Champ : ")
txt2 = Label(app, text="Deuxième Champ : ")
txt3 = Label(app, text="Troisième Champ : ")
enter1 = Entry(app)
enter2 = Entry(app)
enter3 = Entry(app)

# Création d'un widget 'Canvas' contenant une image bitmap .gif (Il faut voir PIL ,une bibliothèque de python dans www.pythonware.com/products/pil/ , pour les autres formats
can1 = Canvas(app, width=160, height=160, bg="#eee")
photo = PhotoImage(file='0.gif')
item = can1.create_image(80, 80, image=photo)

# Mise en page à l'aide de la méthode grid
txt1.grid(row=1, sticky=E)
txt2.grid(row=2, sticky=E)
txt3.grid(row=3, sticky=E)
enter1.grid(row=1, column=2)
enter2.grid(row=2, column=2)
enter3.grid(row=3, column=2)
can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)

# Demarage
app.mainloop()


