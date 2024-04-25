import tkinter as tk
from tkinter import messagebox
import random

class Galgje:
    def __init__(self, master):
        self.master = master
        self.master.title("Galgje")
        
        self.word_list = ["vuileaal", "hoi", "eentweekzegnee", "yippiejajee", "omg", "eyo", "WESTSIDE", "paling", "fakka", "caca"]
        self.word = random.choice(self.word_list)
        self.guesses = []

        self.create_widgets()
        self.draw_word()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.canvas.create_line(50, 350, 200, 350) # base
        self.canvas.create_line(125, 350, 125, 100) # stand
        self.canvas.create_line(125, 100, 250, 100) # beam
        self.canvas.create_line(250, 100, 250, 150) # rope

        self.word_label = tk.Label(self.master, text="Word: ")
        self.word_label.pack()

        self.guess_label = tk.Label(self.master, text="Guesses: ")
        self.guess_label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

    def draw_word(self):
        display_word = ""
        for letter in self.word:
            if letter in self.guesses:
                display_word += letter
            else:
                display_word += "_"
            display_word += " "
        self.word_label.config(text="Word: " + display_word)

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Guess", "Please enter a single alphabetical character.")
            return
        if guess in self.guesses:
            messagebox.showinfo("Already Guessed", "You've already guessed that letter.")
            return
        self.guesses.append(guess)
        self.draw_word()
        if set(self.word) <= set(self.guesses):
            messagebox.showinfo("Congratulations", f"You've guessed the word '{self.word}'!")
        elif len(set(self.guesses).difference(set(self.word))) >= 6:
            self.canvas.create_oval(230, 150, 270, 190, width=2) # head
            self.canvas.create_line(250, 190, 250, 270) # body
            self.canvas.create_line(250, 220, 220, 250) # left arm
            self.canvas.create_line(250, 220, 280, 250) # right arm
            self.canvas.create_line(250, 270, 220, 300) # left leg
            self.canvas.create_line(250, 270, 280, 300) # right leg
            messagebox.showinfo("Game Over", f"Sorry, you've run out of guesses. The word was '{self.word}'.")
        
    def restart_game(self):
        self.word = random.choice(self.word_list)
        self.guesses = []
        self.canvas.delete("all")
        self.canvas.create_line(50, 350, 200, 350) # base
        self.canvas.create_line(125, 350, 125, 100) # stand
        self.canvas.create_line(125, 100, 250, 100) # beam
        self.canvas.create_line(250, 100, 250, 150) # rope
        self.draw_word()

root = tk.Tk()
game = Galgje(root)
root.mainloop()
