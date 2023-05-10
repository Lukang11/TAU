import numpy as np
import random

def generate_board(rows, cols):
    board = np.zeros((rows, cols), dtype=str)
    return board

def place_start_and_stop(board):
    rows, cols = board.shape
    start_row = random.randint(0, rows - 1)
    start_col = random.choice([0, cols - 1])
    stop_row = random.randint(0, rows - 1)
    stop_col = random.choice([0, cols - 1])
    while stop_row == start_row and stop_col == start_col:
        stop_row = random.randint(0, rows - 1)
        stop_col = random.choice([0, cols - 1])
    board[start_row, start_col] = 'A'
    board[stop_row, stop_col] = 'B'
    return board, (start_row, start_col), (stop_row, stop_col)

def place_obstacles(board, num_obstacles):
    rows, cols = board.shape
    obstacles_placed = 0
    while obstacles_placed < num_obstacles:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row, col] == 'A' or board[row, col] == 'B':
            continue
        board[row, col] = 'X'
        obstacles_placed += 1
    return board

def place_player(board, player_pos):
    board[player_pos[0], player_pos[1]] = 'P'
    return board

def display_board(board):
    rows, cols = board.shape
    for row in range(rows):
        for col in range(cols):
            print(board[row, col], end=' ')
        print()
    print()

def move_player(board, player_pos, move):
    rows, cols = board.shape
    row, col = player_pos

    if move == 'up':
        if row > 0 and board[row - 1, col] != 'X':
            board[row, col] = ' '
            board[row - 1, col] = 'P'
            return (row - 1, col)
    elif move == 'down':
        if row < rows - 1 and board[row + 1, col] != 'X':
            board[row, col] = ' '
            board[row + 1, col] = 'P'
            return (row + 1, col)
    elif move == 'left':
        if col > 0 and board[row, col - 1] != 'X':
            board[row, col] = ' '
            board[row, col - 1] = 'P'
            return (row, col - 1)
    elif move == 'right':
        if col < cols - 1 and board[row, col + 1] != 'X':
            board[row, col] = ' '
            board[row, col + 1] = 'P'
            return (row, col + 1)

    return player_pos

def generate_game(rows, cols, num_obstacles):
    board = generate_board(rows, cols)
    board, start_pos, stop_pos = place_start_and_stop(board)
    board = place_obstacles(board, num_obstacles)
    player_pos = start_pos

    while player_pos != stop_pos:
        display_board(board)
        direction = input("Podaj kierunek ruchu (up/down/left/right): ")
        player_pos = move_player(board, player_pos, direction)

    display_board(board)
    print("Gratulacje! Dotarłeś do celu.")

rows = 8
cols = 8
num_obstacles = 10

generate_game(rows, cols, num_obstacles)

