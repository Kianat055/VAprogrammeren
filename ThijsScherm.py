import tkinter as tk
from tkinter import messagebox
import random

# Hier wordt de titel en de grootte van het schermpje.
class Raadspel:
    def __init__(self, master):
        self.master = master
        self.master.title("Raadspel")
        self.master.geometry("300x150")
        # Hier wordt een willekeurig getal gegenereerd 

        self.geheim_nummer = random.randint(1, 10)
        self.raad_label = tk.Label(self.master, text="Voer je gok in:")
        self.raad_label.pack()

        self.raad_entry = tk.Entry(self.master)
        self.raad_entry.pack()

        self.submit_button = tk.Button(self.master, text="Indienen", command=self.controleer_gok)
        self.submit_button.pack()

    def controleer_gok(self):
        gok = int(self.raad_entry.get())

        if gok == self.geheim_nummer:
            messagebox.showinfo("Gefeliciteerd!", "Je hebt het goed geraden!")
            self.master.destroy()
        elif gok < self.geheim_nummer:
            messagebox.showinfo("Incorrect", "Probeer een hoger nummer!")
        else:
            messagebox.showinfo("Incorrect", "Probeer een lager nummer!")

def main():
    root = tk.Tk()
    spel = Raadspel(root)
    root.mainloop()

if __name__ == "__main__":
    main()
