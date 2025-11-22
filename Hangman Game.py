import tkinter as tk
from tkinter import messagebox
import random

class ModernHangman:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Hangman")
        self.root.geometry("800x650")
        self.root.configure(bg="#2C3E50") # Dark Slate Blue background

        # Word List
        self.word_list = [
            "PYTHON", "INTERFACE", "COMPUTER", "ALGORITHM", "DATABASE", 
            "VARIABLE", "COMPILE", "FUNCTION", "KEYBOARD", "MONITOR"
        ]
        
        # Game Variables
        self.chosen_word = ""
        self.guessed_letters = set()
        self.lives = 6
        self.buttons = {} # To store button references
        
        # Setup the Interface
        self.setup_ui()
        
        # Start the first game
        self.start_new_game()

    def setup_ui(self):
        # 1. Title Header
        tk.Label(self.root, text="HANGMAN", font=("Helvetica", 28, "bold"), 
                 bg="#2C3E50", fg="#ECF0F1").pack(pady=15)

        # 2. Canvas for Drawing the Gallows/Stick Figure
        self.canvas = tk.Canvas(self.root, width=300, height=250, bg="#34495E", highlightthickness=0)
        self.canvas.pack(pady=10)

        # 3. The Hidden Word Display (e.g., _ _ A _ _)
        self.word_display = tk.Label(self.root, text="", font=("Consolas", 32, "bold"), 
                                     bg="#2C3E50", fg="#F1C40F") # Yellow text
        self.word_display.pack(pady=20)

        # 4. Keyboard Container Frame
        self.keyboard_frame = tk.Frame(self.root, bg="#2C3E50")
        self.keyboard_frame.pack(pady=10, padx=10)

        # 5. Restart Button
        self.reset_btn = tk.Button(self.root, text="NEW GAME", command=self.start_new_game,
                                   font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", 
                                   padx=20, pady=5, borderwidth=0, cursor="hand2")
        self.reset_btn.pack(pady=20)

    def create_keyboard(self):
        # Clear existing buttons
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        row = 0
        col = 0
        self.buttons = {}

        for letter in letters:
            # Create a button for each letter
            btn = tk.Button(self.keyboard_frame, text=letter, font=("Arial", 12, "bold"), 
                            width=4, height=2, bg="#ECF0F1", fg="#2C3E50",
                            activebackground="#BDC3C7",
                            command=lambda l=letter: self.handle_guess(l))
            
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons[letter] = btn
            
            # Grid logic (9 buttons per row)
            col += 1
            if col > 8: 
                col = 0
                row += 1

    def draw_hangman(self):
        """Draws the stick figure step-by-step based on lives remaining."""
        if self.lives == 6:
            self.canvas.delete("all")
            # Draw Gallows
            self.canvas.create_line(50, 230, 250, 230, width=4, fill="white") # Base
            self.canvas.create_line(100, 230, 100, 40, width=4, fill="white") # Pole
            self.canvas.create_line(100, 40, 200, 40, width=4, fill="white")  # Top
            self.canvas.create_line(200, 40, 200, 70, width=4, fill="white")  # Rope

        # Draw body parts progressively
        if self.lives < 6: # Head
            self.canvas.create_oval(180, 70, 220, 110, width=3, outline="white")
        if self.lives < 5: # Torso
            self.canvas.create_line(200, 110, 200, 170, width=3, fill="white")
        if self.lives < 4: # Left Arm
            self.canvas.create_line(200, 130, 170, 160, width=3, fill="white")
        if self.lives < 3: # Right Arm
            self.canvas.create_line(200, 130, 230, 160, width=3, fill="white")
        if self.lives < 2: # Left Leg
            self.canvas.create_line(200, 170, 170, 210, width=3, fill="white")
        if self.lives < 1: # Right Leg
            self.canvas.create_line(200, 170, 230, 210, width=3, fill="white")

    def start_new_game(self):
        """Resets the game state."""
        self.lives = 6
        self.chosen_word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        
        self.create_keyboard() # Re-enable buttons
        self.draw_hangman()    # Clear canvas
        self.update_word_display()
        self.canvas.configure(bg="#34495E") # Reset background color

    def update_word_display(self):
        """Updates the _ _ A _ _ text."""
        display = [letter if letter in self.guessed_letters else "_" for letter in self.chosen_word]
        self.word_display.config(text=" ".join(display))
        
        if "_" not in display:
            self.game_over(won=True)

    def handle_guess(self, letter):
        """Processes a button click."""
        self.guessed_letters.add(letter)
        btn = self.buttons[letter]

        if letter in self.chosen_word:
            # Correct Guess -> Turn Green
            btn.config(bg="#27AE60", fg="white", state="disabled") 
            self.update_word_display()
        else:
            # Wrong Guess -> Turn Red & Lose Life
            self.lives -= 1
            btn.config(bg="#C0392B", fg="white", state="disabled") 
            self.draw_hangman()
            
            if self.lives == 0:
                self.game_over(won=False)

    def game_over(self, won):
        """Handles the end of the game."""
        # Disable all remaining buttons
        for btn in self.buttons.values():
            btn.config(state="disabled")

        if won:
            self.canvas.configure(bg="#27AE60") # Green background
            messagebox.showinfo("VICTORY", f"You won! The word was {self.chosen_word}")
        else:
            self.canvas.configure(bg="#C0392B") # Red background
            # Reveal the word
            self.word_display.config(text=" ".join(list(self.chosen_word))) 
            messagebox.showerror("GAME OVER", f"You ran out of lives! The word was {self.chosen_word}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernHangman(root)
    root.mainloop()