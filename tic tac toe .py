def print_board(board):
    for row in range(len(board)):
        print(" | ".join(board[row]))
        if row < len(board) - 1:
            print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. The cell is already occupied or out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")

if __name__ == "__main__":
    play_tic_tac_toe()
