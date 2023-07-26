from unittest import TestCase

from board.board_parts.cell import Cell
from board.board_parts.store_cells import StoreCells


class TestStoreCells(TestCase):

    def test_get_existing_values_empty(self):
        store_cells = StoreCells()
        self.assertEquals(set(), store_cells.get_existing_values())

    def test_get_existing_values_get_values(self):
        store_cells = StoreCells()
        cell = Cell(None, None, None, None)
        store_cells.add_cell(cell)
        self.assertEquals({None}, store_cells.get_existing_values())

    def test_get_existing_values_same_cell(self):
        store_cells = StoreCells()
        cell = Cell(None, None, None, None)
        store_cells.add_cell(cell)
        store_cells.add_cell(cell)
        self.assertEquals({None}, store_cells.get_existing_values())

    def test_get_cell_at_empty(self):
        store_cells = StoreCells()
        self.assertRaises(IndexError, store_cells.get_cell_at, 0)

    def test_get_cell_at_negative(self):
        store_cells = StoreCells()
        self.assertRaises(IndexError, store_cells.get_cell_at, -1)

    def test_get_cell_at_out_of_range(self):
        store_cells = StoreCells()
        self.assertRaises(IndexError, store_cells.get_cell_at, 10)

    def test_get_cell_at_get_cell(self):
        store_cells = StoreCells()
        cell = Cell(None, None, None, None)
        store_cells.add_cell(cell)
        self.assertEquals(cell, store_cells.get_cell_at(0))

        cell2 = Cell(None, None, None, None)
        store_cells.add_cell(cell2)
        self.assertEquals(cell2, store_cells.get_cell_at(1))

        self.assertNotEquals(cell2, store_cells.get_cell_at(0))
        self.assertNotEquals(cell, store_cells.get_cell_at(1))

    def test_get_cell_at_wrong_type_ind(self):
        store_cells = StoreCells()
        self.assertRaises(TypeError, store_cells.get_cell_at, 'test')

    def test_add_cell_none(self):
        store_cells = StoreCells()
        self.assertEquals(False, store_cells.add_cell(None))

    def test_add_cell_other_type(self):
        store_cells = StoreCells()
        self.assertEquals(False, store_cells.add_cell(1))

    def test_add_cell_add_cell(self):
        store_cells = StoreCells()
        cell = Cell(None, None, None, None)
        self.assertEquals(True, store_cells.add_cell(cell))

    def test_add_cell_same_cell(self):
        store_cells = StoreCells()
        cell = Cell(None, None, None, None)
        store_cells.add_cell(cell)
        self.assertEquals(False, store_cells.add_cell(cell))
