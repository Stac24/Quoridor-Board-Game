import pygame
from quoridor.board import Board
from .fence import Fence;
from .constants import BLUE, RED, SQUARE_SIZE, BLACK, YELLOW;

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.draw_valid_fences(self.valid_fences)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.selected_type = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = set()
        self.valid_fences = []

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected and self.selected_type == "Piece":
            self.valid_fences = []
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col) # Either none or a piece object
            cell = self.board.get_cell(row, col)
            if piece and piece.color == self.turn:
                self.selected = piece   # Piece object
                self.selected_type = "Piece"
                self.valid_moves = self.board.get_valid_moves(piece)
                self.valid_fences = self.board.get_valid_fences(row, col, cell)  
            else:
                self.selected = cell
                self.selected_type = "Open Cell"
                self.valid_fences = self.board.get_valid_fences(row, col, cell)  

        return True
        
       

    def move(self, row, col):
        piece = self.board.get_piece(row, col) # Either none or a piece object
        if self.selected and not piece and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            self.valid_moves = set()
            self.valid_fences = []
            return False

        return True

    def place_up_fence(self):   # NEED TO IMPLEMENT
        if self.selected and "up" in self.valid_fences:
            row, col = self.valid_fences[0], self.valid_fences[1]
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_up_fence(Fence(row, col, self.turn))
            self.change_turn()

    def place_down_fence(self):   # NEED TO IMPLEMENT
        if self.selected and "down" in self.valid_fences:
            row, col = self.valid_fences[0], self.valid_fences[1]
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_down_fence(Fence(row, col, self.turn))
            self.change_turn()

    def place_left_fence(self):   # NEED TO IMPLEMENT
        if self.selected and "left" in self.valid_fences:
            row, col = self.valid_fences[0], self.valid_fences[1]
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_left_fence(Fence(row, col, self.turn))
            self.change_turn()

    def place_right_fence(self):   # NEED TO IMPLEMENT
        if self.selected and "right" in self.valid_fences:
            row, col = self.valid_fences[0], self.valid_fences[1]
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_right_fence(Fence(row, col, self.turn))
            self.change_turn()

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def draw_valid_fences(self, fences):
        if fences != []: 
            row, col = fences[0], fences[1]
            for dir in range(2, len(fences)):
                if fences[dir] == "up":
                    pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col, SQUARE_SIZE * row), (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row))
                if fences[dir] == "down":
                     pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col, SQUARE_SIZE * row + SQUARE_SIZE), (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row + SQUARE_SIZE))
                if fences[dir] == "left":
                     pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col, SQUARE_SIZE * row), (SQUARE_SIZE * col, SQUARE_SIZE * row + SQUARE_SIZE)) 
                if fences[dir] == "right":
                    pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row), (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row + SQUARE_SIZE)) 
            

    def change_turn(self):
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED
        self.valid_moves = set()
        self.valid_fences = []