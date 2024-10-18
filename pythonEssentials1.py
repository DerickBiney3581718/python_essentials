

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    hr = ('+' + '-' * 7) * 3 + '+'

    def draw_train(l, m, r):
        ws = ('|' + ' ' * 7) * 3 + '|'
        val = ('|' + ' ' * 3 + str(l) + ' ' * 3) + ('|' + ' ' * 3 +
                                                    str(m) + ' ' * 3) + ('|' + ' ' * 3 + str(r) + ' ' * 3) + '|'
        print(ws, val, ws, sep='\n')

    print(hr)
    for l, m, r in board:
        draw_train(l, m, r)
        print(hr)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    # we'll take a move and transform to position on board
    moves_list = make_list_of_free_fields(board)
    if not len(moves_list):
        print('No more turns')
        return True

    print('Your turn 0s')
    valid_move = False
    input_position = None

    while not valid_move:
        user_input = input(
            'Enter a free number between 0 and 10, neither 0 nor 10 is included: ')
        input_position = get_row(user_input), get_col(user_input)
    # check if pos is free, if not re-input
        if input_position in moves_list:
            valid_move = True
    board[input_position[0]][input_position[1]] = '0'
    # put '0' in that pos of the board
    display_board(board)

    return victory_for(board, '0')


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != '0' and board[row][col] != 'X':
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    victory_combs = [[(0, 0), (0, 1), (0, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 0), (1, 1), (2, 2)],
                     #  involving entry one
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     #  verticals
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     #  d2
                     [(2, 0), (1, 1), (0, 2)]
                     ]
    for comb in victory_combs:
        count = 0
        for tile in comb:
            if board[tile[0]][tile[1]] == sign:
                count += 1
        if count == 3:
            subject = 'Computer has' if sign == 'X' else 'You have'
            print(subject, 'won the game')
            return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    from random import randint
    moves_list = make_list_of_free_fields(board)

    if not len(moves_list):
        print('No more turns')
        return True

    print('Computer\'s turn Xs')

    valid_move = False
    input_position = None
    while not valid_move:
        user_input = randint(0, 10)
        input_position = get_row(user_input), get_col(user_input)
    # check if pos is free, if not re-input
        if input_position in moves_list:
            valid_move = True
    board[input_position[0]][input_position[1]] = 'X'
    display_board(board)
    return victory_for(board, 'X')


def get_row(user_input):
    return (int(user_input) - 1) // 3


def get_col(user_input):
    return (int(user_input) - 1) % 3


def init_game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    display_board(board)
    print('Game starts')
    game_over = False
    while not game_over:
        game_over = draw_move(board)
        if (game_over):
            break
        game_over = enter_move(board)


init_game()
