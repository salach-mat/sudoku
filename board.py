from cell import Cell
import random


class Board:
    def __init__(self):
        self.BOARD_SIZE = 9
        self.FILL_CHANCE = 0.25
        self.squares = {}
        self.rows = []
        self._create_board()

    def _create_board(self):
        counter = 0
        square_counter = 1
        self.squares[square_counter] = []
        for i in range(self.BOARD_SIZE):
            self.squares[i + 1] = []

        for i in range(self.BOARD_SIZE):
            self.rows.append([])
            for j in range(self.BOARD_SIZE):
                cell = Cell(i, 'X')

                self.rows[i].append(cell)
                counter += 1
                self._add_cell_to_sqr(i, j, cell)

                if random.random() < self.FILL_CHANCE:
                    cell_val = random.randrange(1, 9)
                    while self._check_rows_columns(i, j, cell_val) or self._check_square(cell, cell_val):
                        cell_val = random.randrange(1, 9)
                    cell.cell_val = cell_val # change it to cover not repetition

    def _add_cell_to_sqr(self, i, j, cell):
        if i < 3 and j < 3:
            self.squares[1].append(cell)
            cell.square = 1
        elif i < 3 and j < 6:
            self.squares[2].append(cell)
            cell.square = 2
        elif i < 3 and j < 9:
            self.squares[3].append(cell)
            cell.square = 3
        elif i < 6 and j < 3:
            self.squares[4].append(cell)
            cell.square = 4
        elif i < 6 and j < 6:
            self.squares[5].append(cell)
            cell.square = 5
        elif i < 6 and j < 9:
            self.squares[6].append(cell)
            cell.square = 6
        elif i < 9 and j < 3:
            self.squares[7].append(cell)
            cell.square = 7
        elif i < 9 and j < 6:
            self.squares[8].append(cell)
            cell.square = 8
        else:
            self.squares[9].append(cell)
            cell.square = 9

    def _check_rows_columns(self, i, j, num):
        row = [elem.cell_val for elem in self.rows[i]]
        col = [elem.cell_val for elem in list(zip(*self.rows))[j]]
        return num in row or num in col

    def _check_square(self, cell, cell_val):
        return cell_val in [elem.cell_val for elem in self.squares[cell.square]]

    def draw_board(self):
        for cell_list in self.rows:
            for cell in cell_list:
                print(str(cell.cell_val) + " ", end="")
            print()
