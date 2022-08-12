import pygame
from quoridor.board import Board;
from quoridor.constants import SQUARE_SIZE, WIDTH, HEIGHT, RED;
from quoridor.game import Game;


FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Quoridor')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.place_up_fence()
                elif event.key == pygame.K_DOWN:
                    game.place_down_fence()
                elif event.key == pygame.K_LEFT:
                    game.place_left_fence()
                elif event.key == pygame.K_RIGHT:
                    game.place_right_fence()
               

        game.update()
    pygame.quit()

main()