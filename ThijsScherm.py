import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hey! Wat is jouw naam?")

entry = tk.Entry(fg="blue", bg="white", width=50)
greeting.pack()
entry.pack()

window.mainloop()
