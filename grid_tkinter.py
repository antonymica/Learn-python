#coding:utf-8
from tkinter import *
app = Tk()
text1 = Label(app, text="Premier champ : ")
text2 = Label(app, text="Second : ")
enter1 = Entry(app)
enter2 = Entry(app)
text1.grid(row=0, sticky=E)
text2.grid(row=1, sticky=E)
enter1.grid(row=0, column=1)
enter2.grid(row=1, column=1)

app.mainloop()