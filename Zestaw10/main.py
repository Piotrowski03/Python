import tkinter as tk  # Py3

from random import randint


def dice():
    number = randint(1, 6)
    label["text"] = str(number)


root = tk.Tk()  # Główne okno

root.title("dice roll")  # Tytuł

frame_a = tk.Frame(root, relief=tk.GROOVE, borderwidth=5)

root.resizable(width=False, height=False)  # nie można zmieniać rozmiarów okna

label = tk.Label(frame_a, text="", width=40, height=2)  # Etykieta

button = tk.Button(frame_a, text="throw the dice", width=40, height=6, bg="black", fg="white", command=dice)

label.grid()
button.grid()
frame_a.grid()

root.mainloop()  # the tkinter event loop
