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
        1: "Je mag een stap vooruit zetten.",
        2: "Je mag twee stappen vooruit zetten.",
        3: "Doe een dansje!",
        4: "Je bent een geluksvogel, sla een beurt over!",
        5: "Wissel van plaats met een andere speler.",
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
