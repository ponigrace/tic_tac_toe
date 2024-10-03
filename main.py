from art import art
from random import choice
from operator import itemgetter
from os import system
import re

PLAYERS = {
    "player_x": {
            "mark": "X",
            "score": 0,
        },
    "player_o": {
            "mark": "O",
            "score": 0,
        },
}


def print_grid(grid):
    filled_grid = f"""
  {grid[0]}  |  {grid[1]}  |  {grid[2]}  
_____|_____|_____   
  {grid[3]}  |  {grid[4]}  |  {grid[5]}
_____|_____|_____
  {grid[6]}  |  {grid[7]}  |  {grid[8]}
     |     |               
"""
    print(filled_grid)


def game():
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    game_over = is_game_over(grid)
    while len(moves) > 0 and not game_over:
        print(f"Remaining moves: {moves}")
        while True:
            try:
                cell_num = int(input(f"{current_player}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if cell_num in moves:
            grid[cell_num - 1] = PLAYERS[current_player]["mark"]
            moves.remove(cell_num)
            print_grid(grid)
            change_player()
        else:
            print("The number you entered is not one of the cells. Or the cell is already filled out.\n")

        game_over = is_game_over(grid)

    if not game_over:
        print("It's a draw 😎")


def change_player():
    global current_player
    if current_player == "player_x":
        current_player = "player_o"
    else:
        current_player = "player_x"


def is_game_over(grid):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for sequence in winning_combinations:
        if check_winner(sequence, grid, "player_x"):
            print("player_x has won 🤩!")
            PLAYERS["player_x"]["score"] += 1
            return True
        elif check_winner(sequence, grid, "player_o"):
            print("player_o has won 😍!")
            PLAYERS["player_o"]["score"] += 1
            return True

    return False


def check_winner(sequence, grid, player):
    regex = "\\b([a-zA-Z])\\1\\1+\\b"
    p = re.compile(regex)

    tictactoe = "".join(itemgetter(*sequence)(grid))

    if tictactoe is None:
        return False

    return re.search(p, tictactoe) and PLAYERS[player]["mark"] in tictactoe


while input("Do you want to play TicTacToe? Type 'y' or 'n': ").lower() == "y":
    system('cls')
    print(art)
    print("Directions: Each cell is numbered. Enter the number of the cell that you want to mark.\n")
    current_player = choice(list(PLAYERS.keys()))
    game()

score_board = f"""
    +----------------+
    |     SCORES     |
    +----------------+
    | player_x: {PLAYERS["player_x"]["score"]}    |
    | player_o: {PLAYERS["player_o"]["score"]}    |
    +----------------+
    """

print(score_board)
