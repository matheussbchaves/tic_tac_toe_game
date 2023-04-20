
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from typing import NamedTuple
from itertools import cycle



class TicTacToeBoard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.geometry(self._center_window())
        self.resizable(False, False)
        self._cells = {}
        self._draw_board_display()
        self._draw_grid()

    def _draw_board_display(self):
        display_frame = Frame(self)
        self.display = Label(display_frame,
                             text='Ready?',
                             font=font.Font(size=20, weight='bold'))
        display_frame.pack()
        self.display.pack()

    def _draw_grid(self):
        grid_frame = Frame(self)

        for row in range(3):
            for col in range(3):
                button = Button(grid_frame,
                                text='',
                                #font=font.Font(size=36, weight='bold'),
                                #fg='black',
                                width=3,
                                #height=2,
                                #highlightbackground='lightblue'
                                )
                
                self._cells[button] = (row, col)
                button.grid(row=row,
                            column=col,
                            ipadx=25,
                            ipady=25,
                            sticky='nsew')
        
        grid_frame.pack()
                
    def _center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_width = int(screen_width / 2 - 300 / 2)
        center_height = int(screen_height / 2 - 300 / 2)

        return f'300x300+{center_width}+{center_height}'
    
class TicTacToeGame:
    def __init__(self, board_size = 3):
        self.board_size = board_size
        self._players = cycle([Player('X', 'red'), Player('O', 'blue')])
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [[Move(row, col) for row in range(self.board_size)] for col in range(self.board_size)]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        row_combo = [[(move.row, move.col) for move in row] for row in self._current_moves]
        col_combo = [[(move.row, move.col) for move in col] for col in self._current_moves]
        diag_combo = [[(move.row, move.col) for move in diag] for diag in self._get_diagonals()]

        return row_combo + col_combo + diag_combo

    def _get_diagonals(self):
        diagonals = [[self._current_moves[i][i] for i in range(self.board_size)],
                    [self._current_moves[i][self.board_size - 1 - i] for i in range(self.board_size)]]
        
        return diagonals
    
    def _validate_move(self, move):
        empty_tile = self._current_moves[move.row][move.col].symbol == ''
        has_winner = self._has_winner
        return empty_tile and not has_winner
        
    def process_move(self, move):
        self._current_moves[move.row][move.col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[i][j] for i, j in combo)
            win = (len(results) == 1) and ('' not in results)
            if win:
                self._has_winner = True
                self.winner_combo = combo
                break
        
    def tied_game(self):
        board = (move.label for row in self._current_moves for move in row)
        return not self._has_winner and all(board)
    
    def toggle_player(self):
        self.current_player = next(self._players)
        
class Player(NamedTuple):
    symbol: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    symbol: str = ''


def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == '__main__':
    main()
