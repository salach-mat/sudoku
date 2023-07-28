from unittest import TestCase

from board.board_parts.cell import Cell
from board.board_parts.column import Column
from board.board_parts.row import Row
from board.board_parts.square import Square


class TestCell(TestCase):

    def setUp(self):
        self.row = Row()
        self.col = Column()
        self.square = Square()

    def test_get_not_possible_vals_val_is_default(self):
        cell = Cell(0, 0, self.square, self.col, self.row)
        self.assertEquals(set(), cell.get_not_possible_vals())

    def test_get_not_possible_vals_val_is_not_default(self):
        cell = Cell(1, 0, self.square, self.col, self.row)
        self.square.add_cell(cell)
        self.row.add_cell(cell)
        self.col.add_cell(cell)
        self.assertEquals({1}, cell.get_not_possible_vals())
