import re
import math
import os
import time
import random
from Image import image
from Color import Color


def init_board():  # Misi
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


""" ###### Additional Methods ###### """


def clear():
    """Clears the screen."""

    os.system('clear')


""" ###### miniMAX ###### """  # Tibi


def evaluate(board: list):
    """Evaluates moves, returns a score, based on positions."""

    ai = 1

    for i in range(3):
        # Horizontal
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:  # |
            return 10 if board[i][0] == ai else -10

    for i in range(3):
        #  Vertical
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:  # --
            return 10 if board[0][i] == ai else -10

    # Diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:  #  \
        return 10 if board[0][0] == ai else -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:  # /
        return 10 if board[0][2] == ai else -10

    return 0


def minimax(board: list, depth: int, isMaximizing: bool):
    """ Minimax algorithm, or at least something like that. """

    # If Maximizer has won the game
    score = evaluate(board)
    if score == 10:
        return score
    # If Minimizer has won the game
    elif score == -10:
        return score
    # If there are no moves left
    if is_full(board):
        return 0

    # Maximizer's move
    if isMaximizing:
        player = 1
        best_score = -math.inf
        # Iterate through board
        for i in range(3):
            for j in range(3):
                # Check if cell empty
                if board[i][j] == 0:
                    board[i][j] = player
                    foo = minimax(board, depth + 1, not isMaximizing)
                    board[i][j] = 0
                    best_score = max(best_score, foo)

        return best_score

    # Minimizer's move
    else:
        player = 2
        best_score = math.inf
        # Iterate through board
        for i in range(3):
            for j in range(3):
                # Check if cell empty
                if board[i][j] == 0:
                    board[i][j] = player
                    foo = minimax(board, depth + 1, not isMaximizing)
                    board[i][j] = 0
                    best_score = min(best_score, foo)

        return best_score


""" ###### Movement (AI too), Mark ###### """


def get_ai_move(board, player):  # Tibi
    """Returns the coordinates of a valid move for player on board."""

    ai = 1
    best_value = -math.inf
    best_move = {
        'row': -1,
        'col': -1
    }
    # Iterate through board
    for i in range(3):
        for j in range(3):
            # Check if empty cell
            if board[i][j] == 0:
                board[i][j] = ai
                value = minimax(board, 0,  False)
                board[i][j] = 0
                # If current value bigger than best_value, assign value to best_value
                if value > best_value:
                    best_move['row'] = i
                    best_move['col'] = j
                    best_value = value

    return best_move['row'], best_move['col']


def get_move(board: list, player: int):  # Tibi
    """Returns the coordinates of a valid move for player on board."""

    spam = ['A', 'B', 'C']

    player_name = 'X' if player == 1 else 'O'
    move = input("\n{}\'s move: ".format(player_name)).upper()

    if move == "QUIT":
        print_color("\nQuit", Color.RED)
        exit()

    if re.fullmatch(r'[A-C][1-3]', move):
        row = spam.index(move[:1])
        col = int(move[1:]) - 1
        if board[row][col] == 0:
            return row, col

    print_color("Wrong input!", Color.RED)

    return get_move(board, player)


def mark(board, player, row, col):  # Misi
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


""" ###### Boolean Checks ###### """


def has_won(board, player):  # Misi
    """Returns True if player has won the game."""
    for i in range(3):
        # Vertical
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        # Horizontal
        elif board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # Diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_full(board):  # Tibi
    """Returns True if board is full."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


""" ###### Print Stuff ######"""


def print_board(board):  # Tibi
    """Prints a 3-by-3 board on the screen with borders."""

    temp_board = [['.', '.', '.'] for i in range(3)]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                temp_board[i][j] = 'X'
            elif board[i][j] == 2:
                temp_board[i][j] = 'O'

    print("   1   2   3")
    print("A  {} | {} | {}".format(temp_board[0][0], temp_board[0][1], temp_board[0][2]))
    print("  ---+---+---")
    print("B  {} | {} | {}".format(temp_board[1][0], temp_board[1][1], temp_board[1][2]))
    print("  ---+---+---")
    print("C  {} | {} | {}".format(temp_board[2][0], temp_board[2][1], temp_board[2][2]))


def print_result(player):  # Misi
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if player == 0:
        print_color("\nThe game is a tie!", Color.YELLOW)
    elif player == 1:
        print_color("\nX has won the game!", Color.GREEN)
    elif player == 2:
        print_color("\nO has won the game!", Color.GREEN)


def print_color(word, color):
    """Prints colored word"""

    print(color(word) + Color.RESET(''))


""" ###### Game Modes ######"""


def ai_ai():
    board = init_board()
    player = random.randint(1, 2)

    while True:
        print_board(board)

        if player == 1:
            print_color('X\'s turn (AI)\n', Color.BLUE)
            row, col = get_ai_move(board, player)
            time.sleep(0.5)
        else:
            print_color('O\'s turn (AI)\n', Color.RED)
            row, col = get_ai_move(board, player)
            time.sleep(0.5)

        mark(board, player, row, col)
        clear()

        if has_won(board, player):
            print_board(board)
            print_result(player)
            break
        elif is_full(board):
            print_board(board)
            print_result(0)
            break

        player = 2 if player == 1 else 1


def human_ai():
    board = init_board()
    player = 1  # This is the only way it works, don't change this

    while True:
        print_board(board)

        if player == 1:
            print_color('AI turn\n', Color.BLUE)
            row, col = get_ai_move(board, player)
            time.sleep(0.5)
        else:
            row, col = get_move(board, player)

        mark(board, player, row, col)
        clear()

        if has_won(board, player):
            print_board(board)
            print_result(player)
            break
        elif is_full(board):
            print_board(board)
            print_result(0)
            break

        player = 2 if player == 1 else 1


def human_human():
    board = init_board()
    player = random.randint(1, 2)

    while True:

        print_board(board)
        row, col = get_move(board, player)
        mark(board, player, row, col)

        if has_won(board, player):
            print_result(player)
            break
        elif is_full(board):
            print_result(0)
            break

        clear()
        player = 2 if player == 1 else 1

    print_board(board)


""" ###### Main Stuff ###### """


def tictactoe_game(mode = 'HUMAN-HUMAN'):
    if mode == 1:
        human_human()
    elif mode == 2:
        human_ai()
    elif mode == 3:
        ai_ai()


def main_menu():
    """Select playmode"""

    print_color("\n1. Human vs. Human", Color.YELLOW)
    print_color("2. Human vs. AI", Color.MAGENTA)
    print_color("3. AI vs. AI", Color.GREEN)
    print(image)

    mode = input("Choose one of these options: ").upper()

    if mode == 'QUIT':
        print_color("Quit", Color.RED)
        exit()
    elif mode == 1 or 2 or 3:
        tictactoe_game(int(mode))


if __name__ == '__main__':
    main_menu()
