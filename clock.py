#coding:utf-8

from tkinter import *
from tkinter.ttk import *
from time import strftime

app = Tk()
app.title("Clock")
app.resizable(width=False, height=False)

def tiem():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, tiem)

label = Label(app, font=("ds-digital", 50), background="black", foreground="cyan")
label.pack(anchor='center')
tiem()

mainloop()