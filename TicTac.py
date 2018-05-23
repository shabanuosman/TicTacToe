"""
Tic-Tac Game:

Two player game. 
There are two seeds "X" and "O" available fo the players.
Simple Non-Graphic game.

"""
import numpy as np


class TicTac(object):
    EMPTY = 0
    CROSS = 1
    NOUGHT = 2

    STATE_PLAYING = 0
    STATE_DRAWN = 1
    PLAYER_CROSS_WON = 2
    PLAYER_NOUGHT_WON = 3
    ROWS = 3
    COLUMNS = 3

    def __init__(self):
        self.current_column = 0
        self.current_row = 0
        self.current_player = TicTac.CROSS
        self.current_state = 1
        self.board = np.zeros((3, 3))

    def start_game(self):
        print("Game Started, Lets Play")
        self.current_state = TicTac.STATE_PLAYING
        while self.current_state == TicTac.STATE_PLAYING:
            self.make_a_move()
            self.update_game_status()
            self.print_board()
            if self.current_state == TicTac.PLAYER_CROSS_WON:
                print("'X' won !!!!, Bye")
            elif self.current_state == TicTac.PLAYER_NOUGHT_WON:
                print("'O' won !!!!, Bye")
            elif self.current_state == TicTac.STATE_DRAWN:
                print(" Its a draw !!!!, Bye")
            self.current_player = TicTac.NOUGHT if self.current_player == TicTac.CROSS else TicTac.CROSS

    def make_a_move(self):
        is_invalid_input = True
        player_name = "X" if self.current_player == TicTac.CROSS else "O"
        while is_invalid_input:
            row = input("Player " + player_name + ",Please enter your move (row[1-3] column[1-3]): ") - 1
            column = input() - 1

            if 0 <= row < TicTac.ROWS and 0 <= column < TicTac.COLUMNS:
                self.current_row = row
                self.current_column = column
                self.board[self.current_row][self.current_column] = self.current_player
                is_invalid_input = False
            else:
                is_invalid_input = True
                print("This move at (" + (row + 1) + "," + (column + 1)
                      + ") is not valid. Try again...")

    def update_game_status(self):
        if self.is_match_won(self.current_player, self.current_row, self.current_column):
            self.current_state = TicTac.PLAYER_CROSS_WON if self.current_player == TicTac.CROSS else TicTac.PLAYER_NOUGHT_WON
        elif self.is_match_drawn():
            self.current_state = TicTac.STATE_DRAWN

    def is_match_drawn(self):
        for row in range(0, TicTac.ROWS):
            for column in range(0, TicTac.COLUMNS):
                if self.board[row][column] == 0:
                    return False

        return True

    def is_match_won(self, current_player_seed, current_row, current_column):
        return (self.rows_matched(current_player_seed, current_row)
                or self.columns_matched(current_column, current_player_seed)
                or self.diagonal_matched(current_column, current_player_seed, current_row)
                or self.opp_diagonal_matched(current_column, current_player_seed, current_row));

    def opp_diagonal_matched(self, current_column, current_player_seed, current_row):
        return current_row + current_column == 2 and self.board[0][2] == current_player_seed and self.board[1][
                                                                                                     1] == current_player_seed and \
               self.board[2][0] == current_player_seed

    def diagonal_matched(self, current_column, current_player_seed, current_row):
        return current_row == current_column and self.board[0][0] == current_player_seed and self.board[1][
                                                                                                 1] == current_player_seed and \
               self.board[2][2] == current_player_seed

    def columns_matched(self, current_column, current_player_seed):
        return self.board[0][current_column] == current_player_seed and self.board[1][
                                                                            current_column] == current_player_seed and \
               self.board[2][current_column] == current_player_seed

    def rows_matched(self, current_player_seed, current_row):
        return self.board[current_row][0] == current_player_seed and self.board[current_row][
                                                                         1] == current_player_seed and \
               self.board[current_row][2] == current_player_seed

    def print_board(self):
        for row in range(0, TicTac.ROWS):
            for column in range(0, TicTac.COLUMNS):
                self.print_cell(self.board[row][column])
                if column != TicTac.COLUMNS - 1:
                    print("|"),

            print
            if row != TicTac.COLUMNS:
                print("-----------")

        print

    def print_cell(self, content):

        if content == 0:
            print("  "),
        elif content == TicTac.NOUGHT:
            print(" O "),
        else:
            print(" X "),


def main():
    tic_tac_game = TicTac()
    tic_tac_game.start_game()


if __name__ == "__main__":
    main()
