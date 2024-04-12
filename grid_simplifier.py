#coding:utf-8
from tkinter import *

app = Tk()

# Création de labels
Label(app, text="Premier Champ").grid(sticky=E)
Label(app, text="Deuxième Champ").grid(sticky=E)
Label(app, text="Troisième Champ").grid(sticky=E)
entr1 = Entry(app)
entr2 = Entry(app)
entr3 = Entry(app)

entr1.grid(row=0, column=1)
entr2.grid(row=1, column=1)
entr3.grid(row=2, column=1)


check = Checkbutton(app, text="Case à cocher, pour voir")
check.grid(columnspan=2)

# Création du Canvas pour mettre l'image bitmap
can1 = Canvas(app, width=160, height=160, bg='white')
photo = PhotoImage(file='0.gif')
can1.create_image(80, 80, image=photo)
can1.grid(row=0, column=2, rowspan=4, pady=5, padx=10)

# demarage
app.mainloop()