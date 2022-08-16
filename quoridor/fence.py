import pygame;
from .constants import SQUARE_SIZE;

class Fence:
    def __init__(self, row, col, color):
        '''Initializes a fence with a row, col, and color'''
        self.row = row
        self.col = col
        self.color = color
    
    def draw_fence_up(self, win):
        '''Draws the top fence for a cell'''
        pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row), (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row)) 
   
    def draw_fence_down(self, win):
        '''Draws the bottom fence for a cell'''
        pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row + SQUARE_SIZE), (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row + SQUARE_SIZE)) 
    
    def draw_fence_left(self, win):
        '''Draws the left fence for a cell'''
        pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row), (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row + SQUARE_SIZE)) 

    def draw_fence_right(self, win):
        '''Draws the right fence for a cell'''
        pygame.draw.line(win, self.color, (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row), (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row + SQUARE_SIZE)) 

    

