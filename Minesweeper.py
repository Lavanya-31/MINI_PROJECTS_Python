import random

def create_board(rows, cols, num_mines):
    
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    for _ in range(num_mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == 'X':
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = 'X'

    return board

def print_board(board, reveal_all=False):
    rows, cols = len(board), len(board[0])
    print("  ", end="")
    for col in range(cols):
        print(col, end=" ")
    print("\n")

    for row in range(rows):
        print(row, end=" ")
        for col in range(cols):
            if not reveal_all and board[row][col] != 'X':
                print('.', end=" ")
            else:
                print(board[row][col], end=" ")
        print()

def count_adjacent_mines(board, row, col):
    rows, cols = len(board), len(board[0])
    count = 0

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if board[i][j] == 'X':
                count += 1

    return count

def reveal_cell(board, revealed, row, col):
    rows, cols = len(board), len(board[0])

    if not (0 <= row < rows and 0 <= col < cols) or revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 'X':
        return  
    if board[row][col] == ' ':
        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                reveal_cell(board, revealed, i, j)

def play_minesweeper(rows, cols, num_mines):
    board = create_board(rows, cols, num_mines)
    revealed = [[False] * cols for _ in range(rows)]

    while True:
        print_board(revealed)
        row = int(input("Enter row (0-{}): ".format(rows - 1)))
        col = int(input("Enter col (0-{}): ".format(cols - 1)))

        if (0 <= row < rows) and (0 <= col < cols) and not revealed[row][col]:
            reveal_cell(board, revealed, row, col)

            if board[row][col] == 'X':
                print("Game Over! You hit a mine.")
                print_board(board, reveal_all=True)
                break

            if all(board[i][j] != ' ' or revealed[i][j] for i in range(rows) for j in range(cols)):
                print("Congratulations! You won.")
                print_board(board, reveal_all=True)
                break
        else:
            print("Invalid input. Please enter valid row and col.")

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    num_mines = int(input("Enter the number of mines: "))

    play_minesweeper(rows, cols, num_mines)
