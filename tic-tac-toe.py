import re


def init_board():       # Misi
    """Returns an empty 3-by-3 board (with zeros)."""
    board = []
    return board


def get_move(board, player):        # Tibi
    """Returns the coordinates of a valid move for player on board."""
    spam = ['A', 'B', 'C']
    while True:
        if player == 1:
            data = input("X's Move").upper()
        else:
            data = input("0's Move").upper()
        if re.fullmatch(r"[A-C][1-3]"):
            row = spam.index(data[0])
            col = int(data[1]) - 1
            if board[row][col] == 0:
                return row, col
        print("Wrong input!")


def get_ai_move(board, player):         # Tibi
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):      # Misi
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):         # Misi
    """Returns True if player has won the game."""
    return False


def is_full(board):     # Tibi
    """Returns True if board is full."""
    return False


def print_board(board):         # Tibi
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):           # Misi
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
