import pygame
from quoridor.board import Board;
from quoridor.constants import WIDTH, HEIGHT;


FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Quoridor')

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        board = Board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()