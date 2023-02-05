import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = None
    if player_choice == computer_choice:
        result = 'Tie'
    elif player_choice == 'rock' and computer_choice == 'scissors':
        result = 'You win!'
    elif player_choice == 'paper' and computer_choice == 'rock':
        result = 'You win!'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        result = 'You win!'
    else:
        result = 'You lose!'
    messagebox.showinfo('Result', f'You chose {player_choice}.\nComputer chose {computer_choice}.\n\n{result}')

root = tk.Tk()
root.title('Rock-Paper-Scissors')

frame = tk.Frame(root)
frame.pack(pady=20)

rock_button = tk.Button(frame, text='Rock', command=lambda: play_game('rock'))
rock_button.pack(side='left', padx=10)

paper_button = tk.Button(frame, text='Paper', command=lambda: play_game('paper'))
paper_button.pack(side='left', padx=10)

scissors_button = tk.Button(frame, text='Scissors', command=lambda: play_game('scissors'))
scissors_button.pack(side='left', padx=10)

root.mainloop()