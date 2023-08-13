def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    return all(all(square != '' for square in row) for row in board)

def game():
    board = [['' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    
    while True:
        print_board(board)
        player = players[current_player]
        move = input(f"Player {player}, enter your move (row col): ")
        
        try:
            row, col = map(int, move.split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                board[row][col] = player
                if check_win(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif check_tie(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                current_player = 1 - current_player  # Switch player
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Use format: row col")

game()