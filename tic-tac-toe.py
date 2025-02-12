import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def get_computer_move(board):
    for player in ["O", "X"]:
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board, player):
                        board[row][col] = " "
                        return row, col
                    board[row][col] = " "
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(available_moves)

def tic_tac_toe():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        print("Welcome to Tic-Tac-Toe!")
        print_board(board)
        
        for turn in range(9):
            if turn % 2 == 0:
                print("Your Turn (X)")
                row, col = get_player_move(board)
                board[row][col] = "X"
            else:
                print("Computer's Turn (O)")
                row, col = get_computer_move(board)
                board[row][col] = "O"
            
            print_board(board)
            
            if check_winner(board, "X"):
                print("Congratulations! You win!")
                break
            elif check_winner(board, "O"):
                print("Computer wins! Better luck next time.")
                break
        else:
            print("It's a tie!")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

tic_tac_toe()
