from board.board_parts.cell import Cell
from board.board_parts.store_cells import StoreCells


class Square(StoreCells):

    def add_cell(self, cell: Cell) -> None:
        super().add_cell(cell)
        cell.square = self
