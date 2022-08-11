import pygame;
from .constants import SQUARE_SIZE, BLACK;
from .piece import Piece;

class Cell:
    
    def __init__(self):
        self.piece = None
        self.up_fence = None
        self.down_fence = None
        self.left_fence = None
        self.right_fence = None
    
    def get_piece(self):
        return self.piece
        
    def get_up_fence(self):
        return self.up_fence
    
    def get_down_fence(self):
        return self.down_fence

    def get_left_fence(self):
        return self.left_fence

    def get_right_fence(self):
        return self.right_fence

    def set_piece(self, piece):
        self.piece = piece
    
   