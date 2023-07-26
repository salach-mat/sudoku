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
        self._PART_TO_REMOVE = math.ceil(self._BOARD_SIZE * self._BOARD_SIZE / 1.5)
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
        removed_cells = {}
        coord = (random.randrange(self._BOARD_SIZE), random.randrange(self._BOARD_SIZE))
        multi_solutions = False
        while len(removed_cells) < self._PART_TO_REMOVE:
            while coord in removed_cells.keys():
                coord = (random.randrange(self._BOARD_SIZE), random.randrange(self._BOARD_SIZE))
            removed_cells[coord] = self._rows[coord[0]].cells[coord[1]].cell_val
            self._rows[coord[0]].cells[coord[1]].cell_val = 0

            self.draw_board()
            print()

            multi_solutions = self._check_multiple_solutions(removed_cells)
            if multi_solutions:
                self._rows[coord[0]].cells[coord[1]].cell_val = removed_cells[coord]
                break

    def _check_multiple_solutions(self, empty_cells):
        print("rozw: " + str(self._check_multiple_solutions_rec(list(empty_cells.keys()), 0)))
        return self._check_multiple_solutions_rec(list(empty_cells.keys()), 0) > 1

    def _check_multiple_solutions_rec(self, empty_coords, ind):
        solution_counter = 0
        if ind == len(empty_coords):
            return 1

        row = empty_coords[ind][0]
        col = empty_coords[ind][1]
        square_num = int(self._define_which_square(row, col)) - 1
        cell = self._rows[row].cells[col]

        cell.determine_not_possible_values()
        cell_poss_vals = self._possible_vals - cell.not_possible_vals

        if len(cell_poss_vals) == 0:
            return 0

        cell.cell_val = cell_poss_vals.pop()
        while not self._check_if_can_be_placed(row, col, square_num, cell.cell_val):
            solution_counter += self._check_multiple_solutions_rec(empty_coords, ind + 1)
            if len(cell_poss_vals) == 0:
                cell.cell_val = 0
                return solution_counter
            cell.cell_val = cell_poss_vals.pop()

        solution_counter += self._check_multiple_solutions_rec(empty_coords, ind + 1)

    def _fill_zeros_list(self, coord_list):
        for coord in coord_list:
            self._rows[coord[0]].cells[coord[1]].cell_cal = 0

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
