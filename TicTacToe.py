board=[" " for x in range(9)]

def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player ", number)
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")
def is_victory(icon):
    # Check rows
    if (board[0] == board[1] == board[2] == icon) or \
       (board[3] == board[4] == board[5] == icon) or \
       (board[6] == board[7] == board[8] == icon):
        return True
    # Check columns
    elif (board[0] == board[3] == board[6] == icon) or \
         (board[1] == board[4] == board[7] == icon) or \
         (board[2] == board[5] == board[8] == icon):
        return True
    # Check diagonals
    elif (board[0] == board[4] == board[8] == icon) or \
         (board[2] == board[4] == board[6] == icon):
        return True
    else:
        return False
    
def is_draw():
    if " " not in board:
        return True
    else:
        return False
    
while True:
    print_board()
    player_move("X")
    if is_victory("X"):
        print("Player 1 wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    print_board()
    player_move("O")
    if is_victory("O"):
        print("Player 2 wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

