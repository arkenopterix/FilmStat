from tkinter import *
from tkinter.messagebox import *
import json

fenetre = Tk()

def alert():
    showinfo("alerte", "Bravo!")

file = "/home/brieg/Projects/FilmStat/StatData.json"
with open(file, "r") as fi:
    jsonStr = json.loads(fi.read())

    fi.close()
jtab= []
for key, value in jsonStr.iteritems():


print(jsonStr)
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

fenetre.config(menu=menubar)

p = PanedWindow(fenetre, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

listbox = Listbox(p)
p.add(listbox )
p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
p.pack()
listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)


fenetre.mainloop()