import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("450x200")

        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12), padding=5)
        style.configure('TButton', font=('Arial', 12), padding=5, background='lightblue')
        style.configure('TEntry', font=('Arial', 12), padding=5)

        style.map("TButton", background=[('active', '!disabled', 'blue')],
                            foreground=[('active', 'white')])

        self.random_number = random.randint(1, 1000)
        self.attempts = 0

        ttk.Label(root, text="Enter your guess (1-1000):").grid(column=0, row=0, padx=10, pady=10)
        self.entry_guess = ttk.Entry(root)
        self.entry_guess.grid(column=1, row=0, padx=10, pady=10)

        self.guess_button = ttk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.result = tk.StringVar()
        ttk.Label(root, textvariable=self.result).grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < self.random_number:
                if self.random_number - guess <= 20:
                    self.result.set("Closer but still low! Try again.")
                else:
                    self.result.set("Too low! Try again.")
            elif guess > self.random_number:
                if guess - self.random_number <= 20:
                    self.result.set("Closer but still high! Try again.")
                else:
                    self.result.set("Too high! Try again.")
            else:
                self.result.set(f"Congratulations! You've guessed the number in {self.attempts} attempts.")
                self.guess_button.config(state=tk.DISABLED)
                messagebox.showinfo("Guessing Game", f"Well done! The number was {self.random_number}.\nAttempts: {self.attempts}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
