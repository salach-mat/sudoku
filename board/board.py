import math
import random

from board.board_parts.cell import Cell
from board.board_parts.square import Square
from board.board_parts.row import Row
from board.board_parts.column import Column


class Board:
    def __init__(self, board_size):
        self._BOARD_SIZE = board_size
        self._SQRT_BOARD_SIZE = int(math.sqrt(self._BOARD_SIZE))
        self._FILL_BLANK_CHANCE = 0.7
        self._squares = []
        self._rows = []
        self._cols = []
        self._possible_vals = {x + 1 for x in range(self._BOARD_SIZE)}
        self._create_board()

    def _create_board(self):
        self._init_cols_rows_squares()
        self._fill_diagonal()
        while not self._fill_remaining():
            self._clear_board()
            self._fill_diagonal()
        self._erase_part_of_the_board()

    def _clear_board(self):
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                self._rows[i].cells[j].cell_val = 0

    def _fill_diagonal(self):
        for i in range(0, self._BOARD_SIZE, self._SQRT_BOARD_SIZE):
            self._fill_box(i, i)

    def _fill_box(self, row, col):
        for i in range(self._SQRT_BOARD_SIZE):
            for j in range(self._SQRT_BOARD_SIZE):
                square_num = int(self._define_which_square(row + i, col + j)) - 1
                cell = self._rows[row + i].cells[col + j]
                cell.determine_not_possible_values()
                cell_poss_vals = self._possible_vals - cell.not_possible_vals
                cell_poss_vals = [*cell_poss_vals]
                cell_val = random.choice(cell_poss_vals)
                while not self._check_if_can_be_placed(row + i, col + j, square_num, cell_val):
                    cell_val = random.choice(cell_poss_vals)
                cell.cell_val = cell_val

    def _fill_remaining(self):
        start_row, start_col = 0, self._SQRT_BOARD_SIZE
        return self._fill_remaining_recur(start_row, start_col)

    def _fill_remaining_recur(self, row, col):
        if row == self._BOARD_SIZE - 1 and col == self._BOARD_SIZE:
            return True

        if col == col == self._BOARD_SIZE:
            row, col = row + 1, 0

        square_num = int(self._define_which_square(row, col)) - 1
        cell = self._rows[row].cells[col]

        if cell.cell_val != 0:
            return self._fill_remaining_recur(row, col + 1)

        cell.determine_not_possible_values()
        cell_poss_vals = self._possible_vals - cell.not_possible_vals

        if len(cell_poss_vals) == 0:
            return False

        cell.cell_val = cell_poss_vals.pop()
        while not self._check_if_can_be_placed(row, col, square_num, cell.cell_val)\
                and not self._fill_remaining_recur(row, col + 1):
            if len(cell_poss_vals) == 0:
                cell.cell_val = 0
                return False
            cell.cell_val = cell_poss_vals.pop()

        return True

    def _erase_part_of_the_board(self):
        # randomly erase and check whether it is possible to solve it
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if random.random() < self._FILL_BLANK_CHANCE:
                    self._rows[i].cells[j].cell_val = 0

    def _define_which_square(self, i, j):
        return self._SQRT_BOARD_SIZE * int(i / self._SQRT_BOARD_SIZE) + 1 + int(j / self._SQRT_BOARD_SIZE)

    def _init_cols_rows_squares(self):
        for i in range(self._BOARD_SIZE):
            self._squares.append(Square(i))
            self._rows.append(Row(i))
            self._cols.append(Column(i))

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                square_num = int(self._define_which_square(i, j)) - 1
                cell = Cell(0, self._squares[square_num], self._cols[j], self._rows[i])
                self._rows[i].cells.append(cell)
                self._cols[j].cells.append(cell)
                self._squares[square_num].cells.append(cell)

    def _check_if_can_be_placed(self, i, j, square_num, num):
        in_row = num not in self._rows[i].get_existing_values()
        in_col = num not in self._cols[j].get_existing_values()
        in_square = num not in self._squares[square_num].get_existing_values()
        return in_square and in_col and in_row
