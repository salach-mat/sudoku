from unittest import TestCase

from board.board_parts.cell import Cell
from board.board_parts.store_cells import StoreCells


class TestStoreCells(TestCase):

    def setUp(self):
        self.store_cells = StoreCells()

    def test_get_existing_values_empty(self):
        self.assertEquals(set(), self.store_cells.get_existing_values())

    def test_get_existing_values_get_values(self):
        cell = Cell(None, None, None, None, None)
        self.store_cells.add_cell(cell)
        self.assertEquals({None}, self.store_cells.get_existing_values())

    def test_get_existing_values_same_cell(self):
        cell = Cell(None, None, None, None, None)
        self.store_cells.add_cell(cell)
        self.store_cells.add_cell(cell)
        self.assertEquals({None}, self.store_cells.get_existing_values())

    def test_get_cell_at_empty(self):
        self.assertRaises(IndexError, self.store_cells.get_cell_at, 0)

    def test_get_cell_at_negative(self):
        self.assertRaises(IndexError, self.store_cells.get_cell_at, -1)

    def test_get_cell_at_out_of_range(self):
        self.assertRaises(IndexError, self.store_cells.get_cell_at, 10)

    def test_get_cell_at_get_cell(self):
        cell = Cell(None, None, None, None, None)
        self.store_cells.add_cell(cell)
        self.assertEquals(cell, self.store_cells.get_cell_at(0))

        cell2 = Cell(None, None, None, None, None)
        self.store_cells.add_cell(cell2)
        self.assertEquals(cell2, self.store_cells.get_cell_at(1))

        self.assertNotEquals(cell2, self.store_cells.get_cell_at(0))
        self.assertNotEquals(cell, self.store_cells.get_cell_at(1))

    def test_get_cell_at_wrong_type_ind(self):
        self.assertRaises(TypeError, self.store_cells.get_cell_at, 'test')

    def test_add_cell_none(self):
        self.assertEquals(False, self.store_cells.add_cell(None))

    def test_add_cell_other_type(self):
        self.assertEquals(False, self.store_cells.add_cell(1))

    def test_add_cell_add_cell(self):
        cell = Cell(None, None, None, None, None)
        self.assertEquals(True, self.store_cells.add_cell(cell))

    def test_add_cell_same_cell(self):
        cell = Cell(None, None, None, None, None)
        self.store_cells.add_cell(cell)
        self.assertEquals(False, self.store_cells.add_cell(cell))
