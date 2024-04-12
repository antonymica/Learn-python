#coding:utf-8

list_notes = []
eleve = 0
basse = 0
som = 0
print("SAISI DES NOTES DANS UNE LISTE".center(50, "-"))
note = float(input("Entrer une note : "))
while note > 0:
    list_notes.append(note)
    print(f"Saisi : {note}")
    for i in list_notes:
        if i <= note:
            eleve = i
        if i >= note:
            basse = i
        som += i
        moyenne = som / len(list_notes)
    print(f"La plus élever : {eleve}\nLa plus basse : {basse}\nLa moyennne : {moyenne}")
    note = float(input("Entrer une note : "))

