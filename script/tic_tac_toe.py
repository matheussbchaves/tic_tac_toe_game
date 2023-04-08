
from tkinter import *
from tkinter.ttk import *
from tkinter import font


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
    


def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == '__main__':
    main()

