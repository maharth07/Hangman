# Hangman Game 

A simple, graphical Hangman game built with Python.

## 📋 Requirements
* **Python 3.x** (Tkinter is included with Python by default).

## 🚀 How to Run
1.  Save the code as `hangman.py`.
2.  Open your terminal or command prompt.
3.  Run the command:
    ```bash
    python hangman.py
    ```

## 🕹️ How to Play
* **Goal:** Guess the hidden word (Tech/Computer theme).
* **Controls:** Click the letters on the screen to make a guess.
* **Rules:**
    * **Green:** Correct guess.
    * **Red:** Wrong guess (you lose a life).
    * You have **6 lives** before the stick figure is fully drawn and the game ends.

## ✏️ Customization
To change the words, edit the `word_list` inside the code:
```python
self.word_list = ["YOUR", "WORDS", "HERE"]
