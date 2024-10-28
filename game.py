#to initialize the board
column_row_lis = [" " for _ in range(9)]

#create a function to print the board
def print_board():
    print()
    print(f"| {column_row_lis[0]} | {column_row_lis[1]} | {column_row_lis[2]} |")
    print(f"| {column_row_lis[3]} | {column_row_lis[4]} | {column_row_lis[5]} |")
    print(f"| {column_row_lis[6]} | {column_row_lis[7]} | {column_row_lis[8]} |")
    print()

#function to check for a win
def is_victory():
    if column_row_lis[0] == column_row_lis[1] == column_row_lis[2] or \
        column_row_lis[3] == column_row_lis[4] == column_row_lis[5] or \
        column_row_lis[6] == column_row_lis[7] == column_row_lis[8] or \
        column_row_lis[0] == column_row_lis[3] == column_row_lis[6] or \
        column_row_lis[1] == column_row_lis[4] == column_row_lis[7] or \
        column_row_lis[2] == column_row_lis[5] == column_row_lis[8] or \
        column_row_lis[0] == column_row_lis[4] == column_row_lis[8] or \
        column_row_lis[2] == column_row_lis[4] == column_row_lis[6]:
        return True
    else:
        return False

#function to play the game
def play_game():
    icon_1 = "X"
    icon_2 = "O"
    player = 1

    while True:
        print_board()
        print(f"Your turn player {player}")
        choice = int(input("Enter your choice (0 - 9): "))
        if column_row_lis[choice - 1] == " " and player == 1:
                column_row_lis[choice - 1] = icon_1
                if is_victory():
                    print_board()
                    print(f"Player {player} wins!")
                player =  2
        elif column_row_lis[choice - 1] == " " and player == 2:
                column_row_lis[choice - 1] = icon_2
                if is_victory():
                    print_board()
                    print(f"Player {player} wins!")
                player =  1
        else:
            print("Invalid move. Try again.")

        # Check for a tie
        if " " not in column_row_lis:
            print_board()
            print("It's a tie!")
            break

play_game() 