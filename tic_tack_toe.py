import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg="#fffbe0")
root.resizable(False, False)  # Prevent resizing

board = [" " for _ in range(9)]
buttons = []
game_mode = None
current_player = "X"

colors = {
    "X": "#ff595e",
    "O": "#1982c4",
    "bg": "#fffbe0",
    "btn": "#ffd6a5",
    "hover": "#ffadad",
    "title": "#6a4c93"
}

def is_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_draw():
    return " " not in board

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(player):
    max_player = "O"
    other_player = "X" if player == "O" else "O"

    if is_winner(other_player):
        return {"position": None, "score": 1 * (len(available_moves()) + 1) if other_player == max_player else -1 * (len(available_moves()) + 1)}
    elif is_draw():
        return {"position": None, "score": 0}

    best = {"position": None, "score": -math.inf if player == max_player else math.inf}

    for move in available_moves():
        board[move] = player
        sim_score = minimax(other_player)
        board[move] = " "
        sim_score["position"] = move

        if player == max_player:
            if sim_score["score"] > best["score"]:
                best = sim_score
        else:
            if sim_score["score"] < best["score"]:
                best = sim_score

    return best

def end_game(winner=None):
    if winner:
        messagebox.showinfo("Game Over", f"{winner} wins! 🎉")
    else:
        messagebox.showinfo("Game Over", "It's a draw!")
    root.quit()

def handle_click(i):
    global current_player
    if board[i] == " ":
        board[i] = current_player
        buttons[i]["text"] = current_player
        buttons[i]["fg"] = colors[current_player]
        buttons[i]["state"] = "disabled"
        buttons[i].config(bg="#fff")
        if is_winner(current_player):
            end_game(current_player)
        elif is_draw():
            end_game()
        else:
            if game_mode == "AI":
                if current_player == "X":
                    current_player = "O"
                    ai_move = minimax("O")["position"]
                    handle_click(ai_move)
                    current_player = "X"
            else:
                current_player = "O" if current_player == "X" else "X"

def on_enter(e):
    i = buttons.index(e.widget)
    if board[i] == " ":
        e.widget.config(bg=colors["hover"])

def on_leave(e):
    i = buttons.index(e.widget)
    if board[i] == " ":
        e.widget.config(bg=colors["btn"])

def create_board():
    title_label = tk.Label(root, text="Tic-Tac-Toe Game 🎮", font=("Comic Sans MS", 24, "bold"),
                           fg=colors["title"], bg=colors["bg"])
    title_label.pack(pady=10)

    frame = tk.Frame(root, bg=colors["bg"])
    frame.pack()

    for i in range(9):
        btn = tk.Button(frame, text=" ", font=("Comic Sans MS", 36, "bold"),
                        bg=colors["btn"], width=5, height=2,
                        command=lambda i=i: handle_click(i))
        btn.grid(row=i//3, column=i%3, padx=5, pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        buttons.append(btn)

def start_game(mode):
    global game_mode
    game_mode = mode
    mode_frame.destroy()
    create_board()

# 🎮 Mode selection screen
mode_frame = tk.Frame(root, bg=colors["bg"])
mode_frame.pack(pady=60)

title = tk.Label(mode_frame, text="Choose Game Mode", font=("Comic Sans MS", 26, "bold"),
                 fg=colors["title"], bg=colors["bg"])
title.pack(pady=15)

btn_1v1 = tk.Button(mode_frame, text="1v1 (Two Players)", font=("Comic Sans MS", 18),
                    bg="#b5ead7", width=20, command=lambda: start_game("1v1"))
btn_1v1.pack(pady=10)

btn_ai = tk.Button(mode_frame, text="Play vs AI 🤖", font=("Comic Sans MS", 18),
                   bg="#caffbf", width=20, command=lambda: start_game("AI"))
btn_ai.pack(pady=10)

root.mainloop()
