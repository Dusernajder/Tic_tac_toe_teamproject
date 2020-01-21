import re
import math
import os
import time
import random
from Color import Color


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


""" ----------miniMAX---------- """

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
        elif player == 2:
            move = input("O\'s move: ").upper()
        if move == "QUIT":
            exit()
        if re.fullmatch(r'[A-C][1-3]', move):
            row = spam.index(move[:1])
            col = int(move[1:]) - 1
            if board[row][col] == 0:
                return row, col


def mark(board, player, row, col):  # Misi
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


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
    if player == 1:
        print_color("\nX has won the game!", Color.GREEN)
    else:
        print_color("\nO has won the game!", Color.GREEN)


def tictactoe_game(mode = 'HUMAN-HUMAN'):
    if mode == 1:
        human_human()
    elif mode == 2:
        human_ai()
    elif mode == 3:
        ai_ai()


def ai_ai():
    board = init_board()
    player = random.randint(1, 2)

    while True:
        print_board(board)
        if player == 1:
            print('X\'s turn (AI)')
            row, col = get_ai_move(board, player)
            time.sleep(0.5)
        else:
            print('O\'s turn (AI)')
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
    player = random.randint(1, 2)

    while True:
        print_board(board)
        if player == 1:
            print('AI turn')
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


def main_menu():
    print_color("1. Human vs. Human", Color.CYAN)
    print_color("2. Human vs. AI", Color.MAGENTA)
    print_color("3. AI vs. AI", Color.CYAN)
    mode = input("Choose one of these options: ").upper()
    if mode == 'QUIT':
        print_color("Quit", Color.RED)
        exit()
    elif mode == 1 or 2 or 3:
        tictactoe_game(int(mode))


if __name__ == '__main__':
    main_menu()
