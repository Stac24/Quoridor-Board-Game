import pygame;
from .constants import WHITE, GREY, BLUE, RED, ROWS, COLS, SQUARE_SIZE;
from .piece import Piece;

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None # Might not need
        self.blue = self.red = 1 # Each player has one piece
        self.blue_fences = self.red_fences = 10
        self.create_board()

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):    # Not sure if method will work yet... 
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
                if row == 0 and col == 4:
                    self.board[row].append(Piece(0, 4, RED))
                elif row == 8 and col == 4:
                    self.board[row].append(Piece(8, 4, BLUE))


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)