import pygame;
from .constants import WHITE, GREY, BLUE, RED, ROWS, COLS, SQUARE_SIZE;
from .piece import Piece;

class Board:
    def __init__(self):
        self.board = []
        self.blue = self.red = 1 # Each player has one piece
        self.blue_fences = self.red_fences = 10
        self.create_board()

    def draw_squares(self, win): # Makes checkerboard pattern on board
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def move(self,piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]


    def create_board(self):   # Draws pieces in starting positions and places 0's where there are no pieces
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
        
        self.board[0][4] = (Piece(0, 4, RED))
        self.board[8][4] = (Piece(8, 4, BLUE))


    def draw(self, win): # Draws pieces onto board
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_valid_moves(self, piece):
        pass