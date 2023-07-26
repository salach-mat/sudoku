class BoardOut:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        for cell_list in self.board._rows:
            print(*[cell._cell_val for cell in cell_list._cells], sep=" ")

    def save_board(self):
        file_name = input("Specify the filename: ")

        with open(file_name + '.txt', 'w') as f:
            for cell_list in self.board._rows:
                for cell in cell_list._cells:
                    f.write(str(cell._cell_val if cell._cell_val != 0 else 'X') + ", ")
                f.write('\n')