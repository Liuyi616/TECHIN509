import re


MAX_BOARD_SIZE = 9


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def print_board(board):
    print('\n')
    for coord in sorted(board.keys()):
        x, y = coord
        if y == 0 and x != 0:           # if is new row
            print('\n' + '-' * 2* len(board))

        val = board[coord]
        if val is not None:
            print("  %s  |" % (val), end="")
        else:
            print("(%1d,%1d)|" % (coord), end="")
    print('\n')


def get_board_size(board):
    size = 0
    for items in board:
        for eachItem in items:
            if eachItem is not None:
                size += 1
    return size


def board_full(board):
    if get_board_size(board) == MAX_BOARD_SIZE:
        return True
    else:
        return False


def has_won(board, size, player):
    for n in range(size):
        rows = [board[(x, y)] for x, y in sorted(board.keys()) if n is x]
        cols = [board[(x, y)] for x, y in sorted(board.keys()) if n is y]
        diagonals = [board[(x, y)] for x, y in sorted(board.keys()) if x is y]
        if rows.count(player) is size or cols.count(player) is size or diagonals.count(player) is size:
            return True
    return False


def get_winner(board):
    if has_won(board, get_board_size(board), 'X'):
        return 'X'
    elif has_won(board, get_board_size(board), 'O'):
        return 'O'
    elif board_full(board):
        return None


def valid_move(user_in):
    user_in = user_in.strip()
    matches = re.match(r"[0-9]+\s*,\s*[0-9]+", user_in)
    if matches is not None:
        return tuple(map(int, user_in.split(',')))
    else:
        return False


def place_piece(board, coord, player):
    if coord in board.keys() and board[coord] is None:
        board[coord] = player
        return True
    else:
        return False


def game_ended(board):
    return board_full(board) or has_won(board, get_board_size(board), 'X') or has_won(board, get_board_size(board), 'O')


def other_player(player):
    if player == 'X':
        return "O"
    elif player == 'O':
        return 'X'