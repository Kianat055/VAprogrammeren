import tkinter as tk
import subprocess

# Functies om de verschillende spellen te openen
def galgje():
    subprocess.Popen(["python", "Silscherm.py"])

def getalraadspel():
    subprocess.Popen(["python", "ThijsScherm.py"])

def dobbelspel():
    subprocess.Popen(["python", "KianaScherm.py"])

def reistijd():
    subprocess.Popen(["python", "MarijnScherm.py"])

# Hoofdmenu functie
def main_menu():
    # Sluit alle openstaande frames
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Hoofdmenu", font=("Helvetica", 16)).pack(pady=20)
    
    tk.Button(root, text="Galgje", command=galgje, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Getal raden", command=getalraadspel, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Dobbelspel", command=dobbelspel, width=20, height=2).pack(pady=10)
    tk.Button(root, text="reistijd berekenen", command=reistijd, width=20, height=2).pack(pady=10)
# Setup hoofdvenster
root = tk.Tk()
root.title("Spelletjes Menu")
root.geometry("400x400")

# Open het hoofdmenu bij het starten
main_menu()

# Start de Tkinter event loop
root.mainloop()
