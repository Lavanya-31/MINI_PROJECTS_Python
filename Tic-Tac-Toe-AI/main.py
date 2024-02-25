import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    return any(all(cell == player for cell in row) for row in board) \
        or any(all(board[row][col] == player for row in range(3)) for col in range(3)) \
        or all(board[i][i] == player for i in range(3)) \
        or all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    # Check if the board is full
    return all(cell != ' ' for row in board for cell in row)

def available_moves(board):
    # Return a list of available moves
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    # Minimax algorithm for computer move
    if check_winner(board, 'X'):
        return -10 + depth, None
    elif check_winner(board, 'O'):
        return 10 - depth, None
    elif is_board_full(board):
        return 0, None

    if maximizing_player:
        max_eval, best_move = float('-inf'), None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval, _ = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            if eval > max_eval:
                max_eval, best_move = eval, move
        return max_eval, best_move
    else:
        min_eval, best_move = float('inf'), None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval, _ = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            if eval < min_eval:
                min_eval, best_move = eval, move
        return min_eval, best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not check_winner(board, 'X') and not check_winner(board, 'O') and not is_board_full(board):
        player_move = None
        while player_move not in available_moves(board):
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            player_move = (row, col)
        board[player_move[0]][player_move[1]] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        _, ai_move = minimax(board, 0, True)
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
