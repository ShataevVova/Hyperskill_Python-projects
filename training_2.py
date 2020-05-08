#board = input('Enter cells: ')
board = '_' * 9
board_list = list(''.join(board))


# рисуем доску
def draw_board():
    print('-' * 9)
    print("|", board[0], board[1], board[2], "|")
    print("|", board[3], board[4], board[5], "|")
    print("|", board[6], board[7], board[8], "|")
    print('-' * 9)


# запрашиваем координаты хода игрока
def user_movie(player_token):
    global board
    global board_list
    ask = False
    while not ask:
        coord = input('Enter the coordinates: ').split()
        try:
            x = int(coord[0])
            y = int(coord[1])
        except:
            print('You should enter numbers!')
            continue
        if 1 <= x <= 3 and 1 <= y <= 3:
            if x == 1 and y == 1 and board_list[6] == '_':
                board_list[6] = player_token
                ask = True
            elif x == 1 and y == 2 and board_list[3] == '_':
                board_list[3] = player_token
                ask = True
            elif x == 1 and y == 3 and board_list[0] == '_':
                board_list[0] = player_token
                ask = True
            elif x == 2 and y == 1 and board_list[7] == '_':
                board_list[7] = player_token
                ask = True
            elif x == 2 and y == 2 and board_list[4] == '_':
                board_list[4] = player_token
                ask = True
            elif x == 2 and y == 3 and board_list[1] == '_':
                board_list[1] = player_token
                ask = True
            elif x == 3 and y == 1 and board_list[8] == '_':
                board_list[8] = player_token
                ask = True
            elif x == 3 and y == 2 and board_list[5] == '_':
                board_list[5] = player_token
                ask = True
            elif x == 3 and y == 3 and board_list[2] == '_':
                board_list[2] = player_token
                ask = True
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    board = ''.join(board_list)


def check():
    # win coordinates
    x_win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    y_win_coord = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
    xy_win_coord = ((0, 4, 8), (2, 4, 6))

    # different counts
    x_win_count = 0
    y_win_count = 0
    xy_win_count = 0
    space_win_count = 0
    space_count = 0  # amount space-symbols in board
    x_count = 0  # amount x-symbols in board
    o_count = 0  # amount o-symbols in board
    who_win = None
    draw = None

    for i in board:
        if i == '_':
            space_count += 1
        elif i == 'X':
            x_count += 1
        else:
            o_count += 1

    # calculated win-combinations
    for each in x_win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] != '_':
            x_win_count += 1
            # print(board[each[0]])
            who_win = (board[each[0]] + ' wins')
        elif board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] == '_':
            space_win_count += 1
    for each in y_win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] != '_':
            y_win_count += 1
            # print(board[each[0]])
            who_win = (board[each[0]] + ' wins')
        elif board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] == '_':
            space_win_count += 1
    for each in xy_win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] != '_':
            xy_win_count += 1
            who_win = board[each[0]] + ' wins'
        elif board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] == '_':
            space_win_count += 1

    # check conditions
    if x_win_count == 1 or y_win_count == 1 or xy_win_count == 1 and space_win_count == 0:
        return who_win
        # print(who_win, 'winsssss')
  #  elif x_win_count == 0 and y_win_count == 0 and x_count ==  o_count and space_count != 0:
  #      print("Game not finished")
    elif x_win_count == 0 and y_win_count == 0 and xy_win_count == 0 and space_count == 0:
        return 'Draw'
        #print("Draw")
  #  elif (x_win_count == 1 and y_win_count == 1 and xy_win_count == 0) or ((x_count > o_count or x_count < o_count) and space_count != 0):
  #      print("Impossible")


def main():
    counter = 0
    win = False
    while not win:
        draw_board()
        if counter % 2 == 0:
            user_movie('X')
        else:
            user_movie('O')
        counter += 1
        if counter > 4:
            if check():
                win = True
                break
        # if counter == 9:
        #     print('Draw')
        #     break

    draw_board()
    print(check())


main()
