from board.board import Board
from board.board_out import BoardOut


if __name__ == '__main__':
    b = Board(4)
    b_printer = BoardOut(b)
    b_printer.draw_board()
    # b_printer.save_board()
