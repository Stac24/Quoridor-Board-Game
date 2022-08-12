import pygame;
from .constants import WHITE, GREY, BLUE, RED, ROWS, COLS, SQUARE_SIZE;
from .piece import Piece;
from .cell import Cell;

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
        return self.board[row][col].get_piece()
    
    def get_up_fence(self, row, col):
        return self.board[row][col].get_up_fence()

    def get_down_fence(self, row, col):
        return self.board[row][col].get_down_fence()

    def get_left_fence(self, row, col):
        return self.board[row][col].get_left_fence()

    def get_right_fence(self, row, col):
        return self.board[row][col].get_right_fence()

    def create_board(self):   # Draws pieces in starting positions 
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Cell())
        
        self.board[0][4].set_piece((Piece(0, 4, RED)))
        self.board[8][4].set_piece((Piece(8, 4, BLUE)))


    def draw(self, win): # Draws pieces onto board
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row,col)
                up_fence = self.get_up_fence(row,col)
                down_fence = self.get_down_fence(row, col)
                left_fence = self.get_left_fence(row, col)
                right_fence = self.get_right_fence(row,col)
                if piece:
                    piece.draw(win)
                if up_fence:
                    up_fence.draw_fence_up(win)
                if down_fence:
                    down_fence.draw_fence_down(win)
                if left_fence:
                    left_fence.draw_fence_left(win)
                if right_fence:
                    right_fence.draw_fence_right(win)


    def get_valid_moves(self, piece):
        moves = set()
        row = piece.row
        col = piece.col

        # UP
        if row - 1 in range(ROWS) and not self.board[row - 1][col].get_piece():
            moves.add((row - 1, col))

        # DOWN
        if row + 1 in range(ROWS) and not self.board[row + 1][col].get_piece():
            moves.add((row + 1, col))

        # LEFT
        if col - 1 in range(COLS) and not self.board[row][col - 1].get_piece():
            moves.add((row, col - 1))

        # RIGHT
        if col + 1 in range(COLS) and not self.board[row][col + 1].get_piece():
            moves.add((row, col + 1))
        
        return moves


