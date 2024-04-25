import tkinter as tk
import random

# Functie om de dobbelsteen te rollen en de bijbehorende spelregel te tonen
def roll_dice():
    # Genereer een willekeurig getal tussen 1 en 6 voor de dobbelsteen
    number = random.randint(1, 6)
    
    # Update het label met het nieuwe getal
    result_label.config(text=f"Dice: {number}")
    
    # Toon de bijbehorende spelregel
    show_rule(number)

# Functie om de bijbehorende spelregel te tonen
def show_rule(number):
    rules = {
        1: "Je moet een dansje doen.",
        2: "Je moet een liedje zingen.",
        3: "Drop een griddy",
        4: "sla een beurt over!",
        5: "Doe een aap na.",
        6: "Je mag nog een keer gooien!"
    }
    
    rule_label.config(text=rules[number])

# Maak een hoofdvenster
window = tk.Tk()
window.title("Dobbelspel")

# Maak een label voor het weergeven van het dobbelsteenresultaat
result_label = tk.Label(window, text="Dobbelsteen: ")
result_label.pack(pady=10)

# Maak een label voor het weergeven van de bijbehorende spelregel
rule_label = tk.Label(window, text="")
rule_label.pack(pady=5)

# Maak een knop om de dobbelsteen te rollen
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=5)

# Voer de hoofdlus uit
window.mainloop()
