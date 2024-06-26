import tkinter as tk

# Deze functie berekent de reistijd op basis van de ingevoerde afstand en snelheid
def calculate_time():
    try:
        # Haal de ingevoerde afstand op uit het invoerveld en converteer het naar een float (decimaal getal)
        distance = float(distance_entry.get())
        # Haal de ingevoerde snelheid op uit het invoerveld en converteer het naar een float
        speed = float(speed_entry.get())
        # Bereken de reistijd door de afstand te delen door de snelheid
        time = distance / speed
        # Update de tekst van het label om de geschatte reistijd weer te geven
        result_label.config(text=f"Geschatte reistijd: {time:.2f} uur")
    except ValueError:
        # Als er een ValueError optreedt (bijvoorbeeld als de invoer geen numerieke waarde is),
        # update dan de tekst van het label om de gebruiker te informeren om numerieke waarden in te voeren
        result_label.config(text="Voer numerieke waarden in voor afstand en snelheid!")

# Maak het hoofdvenster aan
root = tk.Tk()
# Geef het hoofdvenster een titel
root.title("Reistijd Calculator")

# Functie voor validatie van de invoer, zodat alleen numerieke waarden kunnen worden ingevoerd
def validate_input(new_value):
    if new_value == "":
        return True
    try:
        float(new_value)
        return True
    except ValueError:
        return False

# Registreer de validatiefunctie bij Tkinter
validate = root.register(validate_input)

# Maak invoervelden voor de afstand en snelheid met labels
distance_label = tk.Label(root, text="Afstand (km):")
distance_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
# Voeg validatie toe aan het invoerveld voor afstand
distance_entry = tk.Entry(root, validate="key", validatecommand=(validate, "%P"))
distance_entry.grid(row=0, column=1, padx=10, pady=5)

speed_label = tk.Label(root, text="Snelheid (km/u):")
speed_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
# Voeg validatie toe aan het invoerveld voor snelheid
speed_entry = tk.Entry(root, validate="key", validatecommand=(validate, "%P"))
speed_entry.grid(row=1, column=1, padx=10, pady=5)

# Maak een knop om de berekening te starten en koppel deze aan de calculate_time-functie
calculate_button = tk.Button(root, text="Bereken", command=calculate_time)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Maak een label waarin de resultaten worden weergegeven
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Start de hoofdloop van het venster
root.mainloop()
