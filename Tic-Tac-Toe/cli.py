# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_board_size, board_full, game_ended, get_winner


if __name__ == '__main__':
    board = make_empty_board()
    size = board_full(board)
    winner = None
    turn = 'O'
    while not game_ended(board):
        print("TODO: take a turn!")
        user_in = input("Player " + turn + ", place your piece: ")
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
    winner = get_winner(board, get_board_size(board))
    if winner is not None:
        print('Game ended! Player %s won!' % winner)
    else:
        print('There was a tie. No one won.')