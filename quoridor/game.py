import pygame
from quoridor.board import Board
from .fence import Fence;
from .constants import BLUE, COLS, FONT, HEIGHT, RED, ROWS, SQUARE_SIZE, BLACK, WHITE, WIDTH, YELLOW;

class Game:
    def __init__(self, win):
        '''Initializes the game'''
        self._init()
        self.win = win
    
    def update(self):
        '''Updates the display for the user'''
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.draw_valid_fences(self.valid_fences)
        self.display_win()
        pygame.display.update()

    def _init(self):
        '''Containes everything we need to initizlize the game'''
        self.selected = None
        self.selected_type = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = set()
        self.valid_fences = []
        self.winner = False
        self.blue_wins = ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8))
        self.red_wins = ((8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8))

    def select(self, row, col):
        '''Selects cells and calls methods to find valid piece movements and fence placements for selected cells'''
        if self.selected and self.selected_type == "Piece":
            self.valid_fences = []
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_cell(row, col).get_piece() # Either none or a piece object
            cell = self.board.get_cell(row, col)
            if piece and piece.color == self.turn:
                self.selected = piece   # Piece object
                self.selected_type = "Piece"
                self.valid_moves = self.board.get_valid_moves(piece)
                if self.check_fences():
                    self.valid_fences = self.board.get_valid_fences(row, col, cell)  
            else:
                self.selected = cell
                self.selected_type = "Open Cell"
                if self.check_fences():
                    self.valid_fences = self.board.get_valid_fences(row, col, cell)  

        return True
        
    def move(self, row, col):
        '''Moves a piece as long as it is a valid move'''
        piece = self.board.get_cell(row, col).get_piece() # Either none or a piece object
        if self.selected and not piece and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.check_for_win(row, col)
            self.change_turn()
        else:
            self.valid_moves = set()
            self.valid_fences = []
            return False
        return True

    def place_up_fence(self):
        '''Places an upper fence within a cell'''   
        if self.selected and "up" in self.valid_fences and self.check_fences():
            row, col = self.valid_fences[0], self.valid_fences[1]
            if row - 1 in range(ROWS):
                neighbor_cell = Board.get_cell(self.board, row - 1, col)
                neighbor_cell.set_down_fence(Fence(row - 1, col, self.turn))
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_up_fence(Fence(row, col, self.turn))
            self.decrement_fences()
            self.change_turn()

    def place_down_fence(self): 
        '''Places a bottom fence within a cell'''  
        if self.selected and "down" in self.valid_fences and self.check_fences():
            row, col = self.valid_fences[0], self.valid_fences[1]
            if row + 1 in range(ROWS):
                neighbor_cell = Board.get_cell(self.board, row + 1, col)
                neighbor_cell.set_up_fence(Fence(row + 1, col, self.turn))
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_down_fence(Fence(row, col, self.turn))
            self.decrement_fences()
            self.change_turn()

    def place_left_fence(self):
        '''Places a left fence within a cell'''   
        if self.selected and "left" in self.valid_fences and self.check_fences():
            row, col = self.valid_fences[0], self.valid_fences[1]
            if col - 1 in range(COLS):
                neighbor_cell = Board.get_cell(self.board, row, col -  1)
                neighbor_cell.set_right_fence(Fence(row, col - 1, self.turn))
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_left_fence(Fence(row, col, self.turn))
            self.decrement_fences()
            self.change_turn()

    def place_right_fence(self): 
        '''Places a right fence within a cell''' 
        if self.selected and "right" in self.valid_fences and self.check_fences():
            row, col = self.valid_fences[0], self.valid_fences[1]
            if col + 1 in range(COLS):
                neighbor_cell = Board.get_cell(self.board, row, col + 1)
                neighbor_cell.set_left_fence(Fence(row, col + 1, self.turn))
            cur_cell = Board.get_cell(self.board, row, col)
            cur_cell.set_right_fence(Fence(row, col, self.turn))
            self.decrement_fences()
            self.change_turn()

    def check_fences(self):  
        '''Checks if the current player has any fences left'''
        if self.turn == RED:
            if Board.get_red_fences(self.board) > 0:
                return True
            else:
                return False
        else:
            if Board.get_blue_fences(self.board) > 0:
                return True
            else:
                return False

    def decrement_fences(self):
        '''Decrements the fence count for the current player'''
        if self.turn == RED:
            Board.decrement_red_fences(self.board)
        else:
            Board.decrement_blue_fences(self.board)

    def draw_valid_moves(self, moves):
        '''Draws all valid moves for a given piece'''
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def draw_valid_fences(self, fences):
        '''Draws all valid fences for a given cell'''
        if fences != []: 
            row, col = fences[0], fences[1]
            for dir in range(2, len(fences)):
                if fences[dir] == "up":
                    pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col, SQUARE_SIZE * row), (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row ))
                if fences[dir] == "down":
                     pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col, SQUARE_SIZE * row + SQUARE_SIZE), (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row + SQUARE_SIZE))
                if fences[dir] == "left":
                     pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col, SQUARE_SIZE * row), (SQUARE_SIZE * col, SQUARE_SIZE * row + SQUARE_SIZE)) 
                if fences[dir] == "right":
                    pygame.draw.line(self.win, YELLOW, (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row), (SQUARE_SIZE * col + SQUARE_SIZE, SQUARE_SIZE * row + SQUARE_SIZE)) 

    def check_for_win(self, row, col):
        '''Checks for winner after a piece is moved'''   
        if self.turn == RED:
            if (row, col) in self.red_wins:
                self.winner = True
        else:
            if (row, col) in self.blue_wins:
                self.winner = True

    def display_win(self):
        '''Displays message that either red or blue has won'''
        if self.winner:
            if self.turn == RED:
                color = "Blue"
                winner = BLUE
            else:
                color = "Red"
                winner = RED
            game_over_text = FONT.render("Game Over: " + color + " Wins!", True, winner, WHITE)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (WIDTH//2, HEIGHT//2)
            self.win.blit(game_over_text, game_over_rect)
            
    def change_turn(self):
        '''Changes the turn'''
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED
        self.valid_moves = set()
        self.valid_fences = []