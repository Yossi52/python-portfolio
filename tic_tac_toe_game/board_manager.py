def print_board(l:list):
    print(f" {l[0]} | {l[1]} | {l[2]}\n"
          f"-----------\n"
          f" {l[3]} | {l[4]} | {l[5]}\n"
          f"-----------\n"
          f" {l[6]} | {l[7]} | {l[8]}")

def is_winner(board):
    if board[0] != " " and board[0] == board[1] and board[1] == board[2]:
        return True
    elif board[3] != " " and board[3] == board[4] and board[4] == board[5]:
        return True
    elif board[6] != " " and board[6] == board[7] and board[7] == board[8]:
        return True
    elif board[0] != " " and board[0] == board[3] and board[3] == board[6]:
        return True
    elif board[1] != " " and board[1] == board[4] and board[4] == board[7]:
        return True
    elif board[2] != " " and board[2] == board[5] and board[5] == board[8]:
        return True
    elif board[0] != " " and board[0] == board[4] and board[4] == board[8]:
        return True
    elif board[2] != " " and board[2] == board[4] and board[4] == board[6]:
        return True
    else:
        return False