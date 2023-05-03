
def print_board(board):
    """ The function prints the board in present view """
    for i in range(3):
        print(f"  {board[3*i]}  |  {board[3*i+1]}  |  {board[3*i+2]}  ")
        if i != 2:
            print("------------------")


def check_win(board):
    """ The function checks if a player wins the game"""
    for i in range(3):
        # column check
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return True

        # Row check
        elif board[3*i] == board[3*i+1] == board[3*i+2] and board[3*i] != " ":
            return True

        # Diagonals check
        elif (board[0] == board[4] == board[8] and board[0] != " ") or \
                (board[2] == board[4] == board[6] and board[2] != " "):

            return True


def play_game():
    """ The function initiates and runs the game till game_on = True """
    players = ["PLAYER 1", "PLAYER 2"]
    symbols = ["X", "0"]
    # initializing the board
    board = [" "]*9
    current_player = 0

    game_on = True
    while game_on:
        print_board(board)
        # Ask user to select a move
        move = int(input(f"{players[current_player]} ({symbols[current_player]}) Enter (1-9):  ")) - 1

        # check if a position is empty
        if board[move] == " ":
            board[move] = symbols[current_player]

            # check if the current player wins
            if check_win(board):
                print(f"{players[current_player]} wins! 🥳")
                play_again = input("Play Again? (y/n):  ").lower()
                if play_again == "n":
                    game_on = False
                else:
                    # reset board if new game
                    board = [" "]*9

            # or check if it's a tie
            elif " " not in board:
                print_board(board)
                print("It's a Tie ⊜")
                play_again = input("Play Again? (y/n):  ").lower()
                if play_again == "n":
                    game_on = False
                else:
                    # reset board if new game
                    board = [" "] * 9

            # if neither win nor draw, pass to next player
            else:
                current_player = (current_player + 1) % 2

        else:
            print("The position is already taken. Try Again")


play_game()
