import pygame;
from .constants import BLUE, RED, SQUARE_SIZE, BLACK;
from .piece import Piece;
from .fence import Fence;

class Cell:
    
    def __init__(self):
        '''Initializes a cell with a piece and its fences'''
        self.piece = None
        self.up_fence = None
        self.down_fence = None
        self.left_fence = None
        self.right_fence = None
    
    def get_piece(self):
        '''Returns the piece within the cell'''
        return self.piece
        
    def get_up_fence(self):
        '''Returns the up fence within the cell'''
        return self.up_fence
    
    def get_down_fence(self):
        '''Returns the down fence within the cell'''
        return self.down_fence

    def get_left_fence(self):
        '''Returns the left fence within the cell'''
        return self.left_fence

    def get_right_fence(self):
        '''Returns the right fence within the cell'''
        return self.right_fence

    def set_piece(self, piece):
        '''Sets the piece for the cell'''
        self.piece = piece

    def set_up_fence(self, fence):
        '''Sets the up fence for the cell'''
        self.up_fence = fence

    def set_down_fence(self, fence):
        '''Sets the down fence for the cell'''
        self.down_fence = fence

    def set_left_fence(self, fence):
        '''Sets the left fence for the cell'''
        self.left_fence = fence

    def set_right_fence(self, fence):
        '''Sets the right fence for the cell'''
        self.right_fence = fence

   

    
   