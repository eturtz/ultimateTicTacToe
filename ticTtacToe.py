import tkinter as tk
from tkinter import messagebox

# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

# Initialize the current player
current_player = "X"

# Create buttons for the Tic Tac Toe grid (defined globally)
buttons = []

# Function to handle a button click
def handle_click(button_index):
    global current_player

    # Check if the button has already been clicked
    if board[button_index] == " ":
        # Update the button text with the current player's symbol (X or O)
        buttons[button_index].config(text=current_player)
        board[button_index] = current_player

        # Check for a win
        if check_win(current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Function to check for a win
def check_win(player):
    # Check rows, columns, and diagonals
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)

# Function to start the game
def start_game():
    # Create the main window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Create buttons for the Tic Tac Toe grid
    buttons = []
    for i in range(9):
        button = tk.Button(root, text=" ", font=("Helvetica", 24), width=5, height=2, command=lambda i=i: handle_click(i))
        buttons.append(button)
        row = i // 3
        col = i % 3
        button.grid(row=row, column=col)

    # Create a reset button
    reset_button = tk.Button(root, text="Reset", font=("Helvetica", 16), command=reset_game)
    reset_button.grid(row=3, column=1)

    root.mainloop()

# Main function to start the game

