from re import L
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

    def get_blue_fences(self):
        '''Returns the current number of fences that the blue player has'''
        return self.blue_fences

    def get_red_fences(self):
        '''Returns the current number of fences that the red player has'''
        return self.red_fences
    
    def decrement_blue_fences(self):
        """Decrements the number of blue fences by 1"""
        self.blue_fences -= 1

    def decrement_red_fences(self):
        """Decrements the number of red fences by 1"""
        self.red_fences -= 1

    def draw_squares(self, win): 
        '''Makes checkerboard pattern on display'''
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def move(self,piece, row, col):
        self.board[row][col].set_piece(self.board[piece.row][piece.col].get_piece()) 
        self.board[piece.row][piece.col].set_piece(None)
        piece.move(row, col)

    def get_cell(self, row, col):
        return self.board[row][col]
    
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
                piece = self.board[row][col].get_piece()
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

        if row - 1 in range(ROWS):
            if not self.board[row - 1][col].get_piece(): 
                if not self.board[row][col].get_up_fence():
                    moves.add((row - 1, col))               # UP
            else:
                if not self.board[row][col].get_up_fence() and not self.board[row - 1][col].get_up_fence() and row - 2 in range(ROWS): # UP JUMP 
                    moves.add((row - 2, col))
                elif self.board[row - 1][col].get_up_fence():
                    if not self.board[row - 1][col + 1].get_piece() and not self.board[row - 1][col].get_right_fence() and col + 1 in range(COLS):
                        moves.add((row - 1, col + 1))  # UP-RIGHT DIAGONAL
                    if not self.board[row - 1][col - 1].get_piece() and not self.board[row - 1][col].get_left_fence() and col - 1 in range(COLS):
                        moves.add((row - 1, col - 1))  # UP-LEFT DIAGONAL

        if row + 1 in range(ROWS):
            if not self.board[row + 1][col].get_piece(): 
                if not self.board[row][col].get_down_fence():
                    moves.add((row + 1, col))               # DOWN
            else:
                if not self.board[row][col].get_down_fence() and not self.board[row + 1][col].get_down_fence() and row + 2 in range(ROWS): # DOWN JUMP 
                    moves.add((row + 2, col))
                elif self.board[row + 1][col].get_down_fence():
                    if not self.board[row + 1][col + 1].get_piece() and not self.board[row + 1][col].get_right_fence() and col + 1 in range(COLS):
                        moves.add((row + 1, col + 1))  # DOWN-RIGHT DIAGONAL
                    if not self.board[row + 1][col - 1].get_piece() and not self.board[row + 1][col].get_left_fence() and col - 1 in range(COLS):
                        moves.add((row + 1, col - 1))  # DOWN-LEFT DIAGONAL

        if col - 1 in range(COLS):
            if not self.board[row][col - 1].get_piece(): 
                if not self.board[row][col].get_left_fence():
                    moves.add((row, col - 1))               # LEFT 
            else:
                if not self.board[row][col].get_left_fence() and not self.board[row][col - 1].get_left_fence() and col - 2 in range(COLS): # LEFT JUMP 
                    moves.add((row, col - 2))
                elif self.board[row][col - 1].get_left_fence():
                    if not self.board[row - 1][col - 1].get_piece() and not self.board[row][col - 1].get_up_fence() and row - 1 in range(ROWS):
                        moves.add((row - 1, col - 1))  # UP-LEFT DIAGONAL
                    if not self.board[row + 1][col - 1].get_piece() and not self.board[row][col - 1].get_down_fence() and row + 1 in range(ROWS):
                        moves.add((row + 1, col - 1))  # DOWN-LEFT DIAGONAL

        if col + 1 in range(COLS):
            if not self.board[row][col + 1].get_piece(): 
                if not self.board[row][col].get_right_fence():
                    moves.add((row, col + 1))               # RIGHT 
            else:
                if not self.board[row][col].get_right_fence() and not self.board[row][col + 1].get_right_fence() and col + 2 in range(COLS): # RIGHT JUMP 
                    moves.add((row, col + 2))
                elif self.board[row][col + 1].get_right_fence():
                    if not self.board[row - 1][col + 1].get_piece() and not self.board[row][col + 1].get_up_fence() and row - 1 in range(ROWS):
                        moves.add((row - 1, col + 1))  # UP-RIGHT DIAGONAL
                    if not self.board[row + 1][col + 1].get_piece() and not self.board[row][col + 1].get_down_fence() and row + 1 in range(ROWS):
                        moves.add((row + 1, col + 1))  # DOWN-RIGHT DIAGONAL
        return moves

    def get_valid_fences(self, row, col, cell):
        fences = []
        fences.append(row)
        fences.append(col)
        if not cell.get_up_fence():
            fences.append("up")
        if not cell.get_down_fence():
            fences.append("down")
        if not cell.get_left_fence():
            fences.append("left")
        if not cell.get_right_fence():
            fences.append("right")
        return fences


