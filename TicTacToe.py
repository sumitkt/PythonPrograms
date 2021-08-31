#Global variable
game_is_on=True
current_player='X'
winner=None

board=['_' for i in range(0,9)]

def display_board():
    print(board[0] + "|" +board[1] + "|" + board[2])
    print(board[3] + "|" +board[4] + "|" + board[5])
    print(board[6] + "|" +board[7] + "|" + board[8])



def play_game():
    #display_board()

    while game_is_on:
        display_board()
        print(f"your turn {current_player}")
        enter_at_index(current_player)
        check_winner()
        flip_player()

    print(f"winner is {winner}")


def check_winner():
    global winner
    global game_is_on
    if board[0]=='X' and board[1]=='X' and board[2]=='X':
        winner=board[0]
        game_is_on = False
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        winner=board[3]
        game_is_on = False
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        winner=board[6]
        game_is_on = False
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        winner=board[0]
        game_is_on = False
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        winner=board[1]
        game_is_on = False
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        winner=board[2]
        game_is_on = False
    elif board[2] == '0' and board[5] == '0' and board[8] == '0':
        winner = board[2]
        game_is_on = False
    elif board[1] == '0' and board[4] == '0' and board[7] == '0':
        winner=board[1]
        game_is_on = False
    elif board[0] == '0' and board[3] == '0' and board[6] == '0':
        winner=board[0]
        game_is_on = False
    elif board[6] == '0' and board[7] == '0' and board[8] == '0':
        winner=board[6]
        game_is_on = False
    elif board[3] == '0' and board[4] == '0' and board[5] == '0':
        winner=board[3]
        game_is_on = False
    elif board[0]=='0' and board[1]=='0' and board[2]=='0':
        winner=board[0]
        game_is_on = False
    elif board[0]=='X' and board[4]=='X' and board[8]=='X':
        winner=board[0]
        game_is_on = False
    elif board[2]=='X' and board[4]=='X' and board[6]=='X':
        winner=board[2]
        game_is_on = False
    elif board[0]=='0' and board[4]=='0' and board[8]=='0':
        winner=board[0]
        game_is_on = False
    elif board[2]=='0' and board[4]=='0' and board[6]=='0':
        winner=board[2]
        game_is_on = False
    elif winner==None and '_' not in board:
        game_is_on=False
    else :
        game_is_on=True

    return






def enter_at_index(current_player):
    position=int(input("enter the box number:"))-1
    if board[position]=='_':
        board[position]=current_player
    else:
        print(f"Sorry you can't overwrite ")
        print(f"Try again  {current_player}")
        enter_at_index(current_player)
    return


def flip_player():
    #print(current_player)
    global current_player
    if current_player =='X':
        #print(True)
        current_player='0'
    else:
        current_player='X'

    #print(current_player)
    return


play_game()