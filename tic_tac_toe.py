
from tkinter import *
from tkinter.ttk import *
from tkinter import font


class TicTacToeBoard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self._cells = {}
        self._draw_board_display()
        self._draw_grid()

    def _draw_board_display(self):
        display_frame = Frame(self)
        display_frame.pack(fill=X)
        self.display = Label(display_frame,
                             text='Ready?',
                             font=font.Font(size=28, weight='bold'))
        self.display.pack()

    def _draw_grid(self):
        grid_frame = Frame(self)
        grid_frame.pack()

        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            for col in range(3):
                button = Button(grid_frame,
                                text='',
                                #font=font.Font(size=36, weight='bold'),
                                #fg='black',
                                width=3)
                                #height=2,
                                #highlightbackground='lightblue')
                
                self._cells[button] = (row, col)
                button.grid(row=row,
                            column=col,
                            padx=5,
                            pady=5,
                            sticky='nsew')


def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == '__main__':
    main()

