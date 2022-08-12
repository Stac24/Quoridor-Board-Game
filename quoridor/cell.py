import pygame;
from .constants import BLUE, RED, SQUARE_SIZE, BLACK;
from .piece import Piece;
from .fence import Fence;

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

    def set_up_fence(self, fence):
        self.up_fence = fence

    def set_down_fence(self, fence):
        self.down_fence = fence

    def set_left_fence(self, fence):
        self.left_fence = fence

    def set_right_fence(self, fence):
        self.right_fence = fence

    #def draw_fences(self, win):
        #if self.up_fence:
            #Fence.draw_fence_up(win)
        #if self.down_fence:
            #Fence.draw_fence_down(win)
        #if self.left_fence:
            #Fence.draw_fence_left(win)
        #if self.right_fence:
            #Fence.draw_fence_right(win)

    
   