import re
import math
from Color import Color
import os


def init_board():  # Misi
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


""" Additional methods """


def clear():
    """Clears the screen."""
    os.system('clear')


def print_color(word, color):
    '''Prints colored word'''
    print(color(word) + Color.RESET(''))


""" ----------miniMAX---------- """  #  Tibi

scores = {
    1: 1,  # X
    2: -1,  # O
    0: 0  # .
}


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    bestScore = -math.inf
    row, col = None, None
    for i in range(3):
        for j in range(3):
            # Is the spot available?
            if board[i][j] == 0:
                board[i][j] = player
                score = minimax(board, 0, player, False)
                board[i][j] = 0
                if score > bestScore:
                    bestScore = score
                    row, col = i, j
    return row, col


def minimax(board, depth, player, isMaximizing):
    """ Minimax algorithm, or at least something like that. """
    if has_won(board, player):
        return scores[player]

    if isMaximizing:
        player = 1
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    score = minimax(board, depth + 1, player, False)
                    board[i][j] = 0
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        player = 2
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    score = minimax(board, depth + 1, player, True)
                    board[i][j] = 0
                    bestScore = min(score, bestScore)
        return bestScore


""" ----------miniMAX---------- """


def get_move(board, player):  # Tibi
    """Returns the coordinates of a valid move for player on board."""
    spam = ['A', 'B', 'C']
    while True:
        if player == 1:
            move = input("X\'s move: ").upper()
        else:
            move = input("O\'s move: ").upper()
        if re.fullmatch(r'[A-C][1-3]', move):
            row = spam.index(move[:1])
            col = int(move[1:]) - 1
            if board[row][col] == 0:
                return row, col


def mark(board, player, row, col):  # Misi
    """Marks the element at row & col on the board for player."""
    board[row][col] = player
    pass


def has_won(board, player, row, col):  # Misi
    """Returns True if player has won the game."""
    if :
        return True
    else:
        return False


def is_full(board):  # Tibi
    """Returns True if board is full."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


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


def print_result(winner):  # Misi
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player = 1

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while True:
        print_board(board)
        row, col = get_move(board, 1)
        mark(board, player, row, col)

    player = 2 if player == 1 else 1
    print_result(winner)


def ai_human():
    board = init_board()
    player = 1
    while True:
        print_board(board)
        if player == 2:
            row, col = get_ai_move()
        else:
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


def human_human():
    board = init_board()
    player = 1
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


def main_menu():
    print_color("1. Human vs. Human", Color.CYAN)
    print_color("2. Human vs. AI", Color.MAGENTA)
    print_color("3. AI vs. AI", Color.CYAN)
    mode = input("Choose one of these options: ").upper()
    if mode == 'QUIT':
        print_color("Quit", Color.RED)
        exit()
    elif mode == 1 or 2:
        tictactoe_game(int(mode))


if __name__ == '__main__':
    main_menu()
