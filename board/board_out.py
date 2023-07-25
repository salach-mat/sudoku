class BoardOut:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        for cell_list in self.board._rows:
            print(*[cell.cell_val for cell in cell_list.cells], sep=" ")

    def save_board(self):
        file_name = input("Specify the filename: ")

        with open(file_name + '.txt', 'w') as f:
            for cell_list in self.board._rows:
                for cell in cell_list.cells:
                    f.write(str(cell.cell_val if cell.cell_val != 0 else 'X') + ", ")
                f.write('\n')