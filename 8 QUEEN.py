def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    if col >= len(board):
        return True  # All queens are placed successfully

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queens(board, col + 1):
                return True  # Recursive call to place queens in the next column

            board[i][col] = 0  # Backtrack if placing a queen doesn't lead to a solution

    return False  # If no safe spot is found for the current column

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))

def eight_queens():
    board_size = 8
    board = [[0] * board_size for _ in range(board_size)]

    if solve_queens(board, 0):
        print("Solution found:")
        print_solution(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    eight_queens()
