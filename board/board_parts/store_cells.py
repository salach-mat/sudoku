class StoreCells:
    def __init__(self, num):
        self.num = num
        self.cells = []

    def get_existing_values(self):
        return {cell.cell_val for cell in self.cells}
