import pygame;
from .constants import SQUARE_SIZE, BLACK;

class Piece:
    PADDING = 15 # Used to draw circles as pieces on the board
    OUTLINE = 2
    def __init__(self, row, col, color):
        '''Initializes piece with a row, col, color, and coordinates'''
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        '''Calculates the correct x and y coordinate for the piece'''
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        '''Draws the piece onto the board'''
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        '''Moves the piece to a new location'''
        self.row = row
        self.col = col
        self.calc_pos()

   