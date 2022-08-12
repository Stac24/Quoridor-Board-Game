import pygame;
from .constants import SQUARE_SIZE;

class Fence:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
    

    def draw_fence_up(self, win):
        pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row), (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row)) 
      
   
    def draw_fence_down(self, win):
         pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row + SQUARE_SIZE), (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row + SQUARE_SIZE)) 
    
    def draw_fence_left(self, win):
         pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row), (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row + SQUARE_SIZE)) 

    def draw_fence_right(self, win):
         pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row), (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row + SQUARE_SIZE)) 

    

