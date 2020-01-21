import re
import math


def init_board ():  # Misi
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    return board


""" ----------miniMAX---------- """

scores = {
    1: 1,  # X
    2: -1,  # O
    0: 0  # .
}


def get_ai_move ( board, player ):
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


def minimax ( board, depth, player, isMaximizing ):
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


def get_move ( board, player ):  # Tibi
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


def get_ai_move ( board, player ):  # Tibi
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark ( board, player, row, col ):  # Misi
    """Marks the element at row & col on the board for player."""
    pass


def has_won ( board, player ):  # Misi
    """Returns True if player has won the game."""
    return False


def is_full ( board ):  # Tibi
    """Returns True if board is full."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def print_board ( board ):  # Tibi
    """Prints a 3-by-3 board on the screen with borders."""
    print("   1   2   3")
    print("A  {} | {} | {}".format(board[0][0], board[0][1], board[0][2]))
    print("  ---+---+---")
    print("B  {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
    print("  ---+---+---")
    print("B  {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))


def print_result ( winner ):  # Misi
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game ( mode = 'HUMAN-HUMAN' ):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu ():
    print("Welcome to our Tic tac toe game!")
    usrIn = input("Press 1 to start a game, press 2 to game settings, press 3 to exit. ")
    if usrIn == "3":
        print("Exiting game!")
        exit()
    else:
        print("test")

    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
