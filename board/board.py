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
        self._possible_vals = {x + 1 for x in range(self._BOARD_SIZE)}

        self._squares = [Square(self._possible_vals.copy()) for _ in range(self._BOARD_SIZE)]
        self._rows = [Row(self._possible_vals.copy()) for _ in range(self._BOARD_SIZE)]
        self._cols = [Column(self._possible_vals.copy()) for _ in range(self._BOARD_SIZE)]
        self._cells = [Cell(self._possible_vals.copy()) for _ in range(self._BOARD_SIZE ** 2)]

        for i, cell in enumerate(self._cells):
            row_num = i // self._BOARD_SIZE
            col_num = i % self._BOARD_SIZE
            square_num = self._define_which_square(row_num, col_num)

            self._rows[row_num].add_cell(cell)
            self._cols[col_num].add_cell(cell)
            self._squares[square_num].add_cell(cell)

        self._create_board()

    def _create_board(self):
        self._fill_diagonal()
        self._fill_remaining()
        # while not self._fill_remaining():
        #     self._clear_board()
        #     self._fill_diagonal()
        # self._erase_part_of_the_board()

    def _clear_board(self):
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                self._rows[i].get_cell_at(j).set_value(0)

    def _fill_diagonal(self):
        sqr_size = int(math.sqrt(self._BOARD_SIZE))
        ind = 0
        for _ in range(sqr_size):
            self._fill_box(ind)
            ind += sqr_size + 1

    def _fill_box(self, square):
        for i in range(len(self._cells)):
            row_num = i // self._BOARD_SIZE
            col_num = i % self._BOARD_SIZE
            square_num = self._define_which_square(row_num, col_num)

            if square == square_num:
                self._cells[i].choose_value()

    def _fill_remaining(self):
        start_ind = 0
        return self._fill_remaining_recur(start_ind)

    def _fill_remaining_recur(self, ind):
        for i in range(self._BOARD_SIZE ** 2):
            if i % self._BOARD_SIZE == 0:
                print()
            print(self._cells[i].get_value() if self._cells[i].get_value() is not None else "X", end=" ")
        print(self._cells[ind].row.possible_values)
        print(self._cells[ind].col.possible_values)
        print(self._cells[ind].square.possible_values)
        print(self._cells[ind].possible_values)
        print(ind)
        print()
        if ind == self._BOARD_SIZE ** 2:
            return True

        cell = self._cells[ind]

        if cell.get_value() is not None:
            return self._fill_remaining_recur(ind + 1)

        if len(cell.get_possible_values()) == 0:
            return False

        cell.choose_value()
        while not self._fill_remaining_recur(ind + 1):
            if len(cell.get_possible_values()) == 0:
                # cell.remove_actual_value()
                return False
            cell.choose_value()
        # while not self._check_if_can_be_placed(row, col, square_num, cell.get_value())\
        #         and not self._fill_remaining_recur(row, col + 1):
        #     if len(cell_poss_vals) == 0:
        #         cell.set_value(0)
        #         return False
        #     cell.set_value(cell_poss_vals.pop())

        return True

    def _erase_part_of_the_board(self):
        removed_cells = {}
        coord = (random.randrange(self._BOARD_SIZE), random.randrange(self._BOARD_SIZE))
        while len(removed_cells) < self._PART_TO_REMOVE:
            while coord in removed_cells.keys():
                coord = (random.randrange(self._BOARD_SIZE), random.randrange(self._BOARD_SIZE))
            removed_cells[coord] = self._rows[coord[0]].get_cell_at(coord[1]).get_value()
            self._rows[coord[0]].get_cell_at(coord[1]).set_value(0)

            multi_solutions = self._check_multiple_solutions(removed_cells)
            if multi_solutions:
                self._rows[coord[0]].get_cell_at(coord[1]).set_value(removed_cells[coord])
                break

    def _check_multiple_solutions(self, empty_cells):
        return self._check_multiple_solutions_rec(list(empty_cells.keys()), 0) > 1

    def _check_multiple_solutions_rec(self, empty_coords, ind):
        solution_counter = 0
        if ind == len(empty_coords):
            return 1

        row = empty_coords[ind][0]
        col = empty_coords[ind][1]
        square_num = int(self._define_which_square(row, col))
        cell = self._rows[row].get_cell_at(col)

        cell_poss_vals = self._possible_vals - cell.get_not_possible_vals()

        if len(cell_poss_vals) == 0:
            return 0

        cell.set_value(cell_poss_vals.pop())
        while not self._check_if_can_be_placed(row, col, square_num, cell.get_value()):
            solution_counter += self._check_multiple_solutions_rec(empty_coords, ind + 1)
            if len(cell_poss_vals) == 0:
                cell.set_value(0)
                return solution_counter
            cell.set_value(cell_poss_vals.pop())

        solution_counter += self._check_multiple_solutions_rec(empty_coords, ind + 1)

    def _define_which_square(self, row_num, col_num):
        sqr_size = int(math.sqrt(self._BOARD_SIZE))
        return sqr_size * (row_num // sqr_size) + col_num // sqr_size

    def _add_cell_to_row_col_square(self, row, col, square, cell):
        self._rows[row].add_cell(cell)
        self._cols[col].add_cell(cell)
        self._squares[square].add_cell(cell)

    def _check_if_can_be_placed(self, i, j, square_num, num):
        in_row = num not in self._rows[i].get_existing_values()
        in_col = num not in self._cols[j].get_existing_values()
        in_square = num not in self._squares[square_num].get_existing_values()
        return in_square and in_col and in_row
