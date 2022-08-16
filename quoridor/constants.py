import pygame;
pygame.init()

# Constant values used within the game
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 9, 9
SQUARE_SIZE = WIDTH//COLS

WHITE = (255, 255, 255)
GREY = (220, 220, 220)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255,255,0)

FONT = pygame.font.SysFont(None, 50, True, False)