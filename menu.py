import tkinter as tk
from tkinter import messagebox

# Functies voor de spelletjes
def open_game_1():
    messagebox.showinfo("Spel 1", "Dit is Spel 1")

def open_game_2():
    messagebox.showinfo("Spel 2", "Dit is Spel 2")

def open_game_3():
    messagebox.showinfo("Spel 3", "Dit is Spel 3")

# Hoofdmenu functie
def main_menu():
    # Sluit alle openstaande frames
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Hoofdmenu", font=("Helvetica", 16)).pack(pady=20)
    
    tk.Button(root, text="Spel 1", command=open_game_1, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Spel 2", command=open_game_2, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Spel 3", command=open_game_3, width=20, height=2).pack(pady=10)

# Setup hoofdvenster
root = tk.Tk()
root.title("Spelletjes Menu")
root.geometry("300x300")

# Open het hoofdmenu bij het starten
main_menu()

# Start de Tkinter event loop
root.mainloop()
