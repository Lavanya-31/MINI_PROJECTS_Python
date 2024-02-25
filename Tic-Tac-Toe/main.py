def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    if any(all(cell == player for cell in row) for row in board):
        return True

    # Check columns
    if any(all(board[row][col] == player for row in range(3)) for col in range(3)):
        return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    # Check if the board is full
    return all(' ' not in row for row in board)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == "__main__":
    play_game()

