from logo import logo
from board_manager import print_board, is_winner

print(logo)
print_board(list(range(1,10)))

game_is_on = True
xo = ["X", "O"] * 4 + ["X"]
while game_is_on:
    cnt = 0
    board = [" "] * 9
    for sign in xo:
        print(f"\n{sign} player turn.")
        correct_input = False
        while not correct_input:
            try:
                position = int(input("Choose the number of position: ")) - 1
            except ValueError:
                print("Please enter Integer.")
            else:
                try:
                    if board[position] == " ":
                        board[position] = sign
                        cnt += 1
                        correct_input = True
                    else:
                        print("That position already filled. Try another position.")
                except IndexError:
                    print("Please enter 1 ~ 9 number")
        print_board(board)
        if is_winner(board):
            print(f"\nThe Winner is {sign}")
            break

    if cnt == 9:
        print("\nDraw")

    if input("\nTry again?(Type 'y' to another game): ") != "y":
        game_is_on = False
