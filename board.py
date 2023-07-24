import math
from cell import Cell
import random
from square import Square
from row import Row
from column import Column


class Board:
    def __init__(self, board_size):
        self._BOARD_SIZE = board_size
        self._SQRT_BOARD_SIZE = math.sqrt(self._BOARD_SIZE)
        self._FILL_CHANCE = 0.25
        self._squares = []
        self._rows = []
        self._cols = []
        self._possible_vals = {x for x in range(self._BOARD_SIZE)}
        self._create_board()

    def _create_board(self):
        self._init_cols_rows_squares()
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                square_num = int(self._define_which_square(i, j)) - 1
                cell = Cell('X', self._squares[square_num], self._cols[j], self._rows[i], self._possible_vals)

                if random.random() < self._FILL_CHANCE:
                    cell_val = random.randrange(1, self._BOARD_SIZE)
                    while self._check_if_can_be_placed(i, j, square_num, cell_val):
                        cell_val = random.randrange(1, self._BOARD_SIZE)
                    cell.cell_val = cell_val

                self._rows[i].add_cell(cell)
                self._cols[j].add_cell(cell)
                self._squares[square_num].add_cell(cell)

    def _init_cols_rows_squares(self):
        for i in range(self._BOARD_SIZE):
            self._squares.append(Square(i))
            self._squares[-1].possible_vals.update(self._possible_vals)

            self._rows.append(Row(i))
            self._rows[-1].possible_vals.update(self._possible_vals)

            self._cols.append(Column(i))
            self._cols[-1].possible_vals.update(self._possible_vals)

    def _define_which_square(self, i, j):
        return self._SQRT_BOARD_SIZE * int(i / self._SQRT_BOARD_SIZE) + 1 + int(j / self._SQRT_BOARD_SIZE)

    def _check_if_can_be_placed(self, i, j, square_num, num):
        in_row = self._rows[i].check_adding_to(num)
        in_col = self._cols[j].check_adding_to(num)
        in_square = self._squares[square_num].check_adding_to(num)
        return not in_square or not in_col or not in_row

    def draw_board(self):
        for cell_list in self._rows:
            print(*[cell.cell_val for cell in cell_list.cells], sep=" ")

    def save_board(self):
        file_name = input("Specify the filename: ")

        with open(file_name + '.txt', 'w') as f:
            for cell_list in self._rows:
                for cell in cell_list.cells:
                    f.write(str(cell.cell_val) + ", ")
                f.write('\n')

