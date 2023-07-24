class StoreCells:
    def __init__(self, num):
        self.num = num
        self.cells = []
        self.vals = set()
        self.possible_vals = set()

    def check_adding_to(self, num):
        return not (num in self.vals)

    def add_cell(self, cell):
        self.cells.append(cell)
        if cell.cell_val is not 'X':
            self.vals.add(cell.cell_val)
            self.possible_vals.remove(cell.cell_val)