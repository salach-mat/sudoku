from board.board_parts.cell import Cell


class StoreCells:
    def __init__(self):
        self._cells = [] # jako slownik, z podanym wczesniej rozmiarem, bo latwo weryfikowac czy juz jest czy nie element

    def get_existing_values(self):
        return {cell.get_value() for cell in self._cells}

    def get_cell_at(self, ind: int):
        if 0 <= ind < len(self._cells):
            return self._cells[ind]
        else:
            raise IndexError

    def add_cell(self, cell: Cell):
        if isinstance(cell, Cell) and cell not in self._cells:
            self._cells.append(cell)
            return True
        else:
            return False
