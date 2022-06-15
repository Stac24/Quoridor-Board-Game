# Author: Stephanie Cox
# Date: August 10, 2021
# Description: Quoridor board game in which each player has 1 pawn in a 9x9 grid. On each turn,
# a player may either move their pawn or place a fence to block the other player's movement.
# Each player starts with 10 fences and once they are placed they may not be removed. The first
# player to reach the other side of the board wins.

class QuoridorGame:
    """Represents the Quoridor game"""
    def __init__(self):
        """Creates a new Quoridor game with a game board, current player, two pawns,
        and fences"""
        self._board = Board()
        self._current_player = 1
        self._p1_pawn = (4, 0)
        self._p1_win = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
        self._p2_win = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
        self._p2_pawn = (4, 8)
        self._p1_fences = 10
        self._p2_fences = 10

    def get_cur_player(self):
        """Returns the current player"""
        return self._current_player

    def get_p1_pawn(self):
        """Returns player one's pawn tuple"""
        return self._p1_pawn

    def get_p2_pawn(self):
        """Returns player two's pawn tuple"""
        return self._p2_pawn

    def get_p1_fences(self):
        """Returns how many fences player one has left"""
        return self._p1_fences

    def get_p2_fences(self):
        """Returns how many fences player two has left"""
        return self._p2_fences

    def change_player(self, player):
        """Changes the current player"""
        if player == 1:
            self._current_player = 2
        elif player == 2:
            self._current_player = 1

    def is_winner(self, player):
        """Checks to see if a given player has won the game"""
        if player == 1:
            if self._p1_pawn in self._p1_win:
                return True
            else:
                return False
        if player == 2:
            if self._p2_pawn in self._p2_win:
                return True
            else:
                return False

    def place_fence(self, player, direction, pos):
        """Allows for players to place their fences along the board"""
        if self.fence_validity(player, pos) is True:  # Helper method to check if the move is valid
            col = pos[0]
            col_min_one = pos[0] - 1
            row = pos[1]
            row_min_one = pos[1] - 1
            if direction == 'h' and self._board.get_cell(col, row).get_fences().get_up_fence() is None:
                self._board.get_cell(col, row).get_fences().set_up_fence(True)
                # Sets the cell below the fence to have an upper fence
                self._board.get_cell(col, row_min_one).get_fences().set_down_fence(True)
                # Sets the cell above the fence to have a lower fence
                if player == 1:
                    self._p1_fences -= 1
                    self.change_player(1)
                elif player == 2:
                    self._p2_fences -= 1
                    self.change_player(2)
                return True
            elif direction == 'v' and self._board.get_cell(col, row).get_fences().get_left_fence() is None:
                self._board.get_cell(col, row).get_fences().set_left_fence(True)
                # Sets the cell to the right of the fence to have a left fence
                self._board.get_cell(col_min_one, row).get_fences().set_right_fence(True)
                # Sets the cell to the left of the fence to have a right fence
                if player == 1:
                    self._p1_fences -= 1
                    self.change_player(1)
                elif player == 2:
                    self._p2_fences -= 1
                    self.change_player(2)
                return True
        return False

    def fence_validity(self, player, pos):
        """Helper method for place_fence method. Checks to make sure it's the player's
         turn, that they have enough fences, that their chosen fence placement
         is within the range of the board, and that there isn't already a winner."""
        if self.is_winner(1) is True or self.is_winner(2) is True:
            return False
        if player != self._current_player:
            return False
        if player == 1:
            fence_count = self._p1_fences
        else:
            fence_count = self._p2_fences
        if fence_count == 0:
            return False
        if pos[0] not in range(9) or pos[1] not in range(9):
            return False
        return True

    def move_pawn(self, player, pos):
        """Allows for players to move their pawns along the board"""
        if self.move_validity(player, pos) is not True:  # Helper method to check if the move is valid before continuing
            return False

        if self.find_move_direction(player, pos) == "Left":
            return self.move_left(player, pos)

        elif self.find_move_direction(player, pos) == "Right":
            return self.move_right(player, pos)

        elif self.find_move_direction(player, pos) == "Up":
            return self.move_up(player, pos)

        elif self.find_move_direction(player, pos) == "Down":
            return self.move_down(player, pos)

        elif self.special_direction(player, pos) == "Left Jump":
            return self.jump_left(player, pos)

        elif self.special_direction(player, pos) == "Right Jump":
            return self.jump_right(player, pos)

        elif self.special_direction(player, pos) == "Up Jump":
            return self.jump_up(player, pos)

        elif self.special_direction(player, pos) == "Down Jump":
            return self.jump_down(player, pos)

        elif self.special_direction(player, pos) == "Up Left Diagonal":
            return self.up_left_diagonal(player, pos)

        elif self.special_direction(player, pos) == "Up Right Diagonal":
            return self.up_right_diagonal(player, pos)

        elif self.special_direction(player, pos) == "Down Right Diagonal":
            return self.down_right_diagonal(player, pos)

        elif self.special_direction(player, pos) == "Down Left Diagonal":
            return self.down_left_diagonal(player, pos)

        else:
            return False

    def move_validity(self, player, pos):
        """Helper method for move_pawn. Checks if there is a win, if the player
        trying to move is the current player, if the space is within the range of the
        board, and if there is a pawn in the space the player is trying to move to."""
        if self.is_winner(1) is True or self.is_winner(2) is True:
            return False

        if player != self._current_player:
            return False

        if pos[0] not in range(9) or pos[1] not in range(9):
            return False

        if pos[0] == self._p1_pawn[0] and pos[1] == self._p1_pawn[1]:
            return False

        if pos[0] == self._p2_pawn[0] and pos[1] == self._p2_pawn[1]:
            return False

        else:
            return True

    def find_move_direction(self, player, pos):
        """Takes the player and their chosen position as parameters. Determines the
        direction that the player is trying to move their pawn. This method is only
        for normal moves (no diagonal or jumps)"""
        if player == 1:
            cur_pos = self._p1_pawn
        else:
            cur_pos = self._p2_pawn
        if cur_pos[0] == pos[0] + 1 and cur_pos[1] == pos[1]:
            return "Left"
        elif cur_pos[0] == pos[0] - 1 and cur_pos[1] == pos[1]:
            return "Right"
        elif cur_pos[0] == pos[0] and cur_pos[1] == pos[1] + 1:
            return "Up"
        elif cur_pos[0] == pos[0] and cur_pos[1] == pos[1] - 1:
            return "Down"

    def special_direction(self, player, pos):
        """Takes the player and their chosen position as parameters. If a player is trying
        to make a special move such as a jump or a diagonal, this method will check which
        way they are trying to go."""
        if player == 1:
            cur_pos = self._p1_pawn
        else:
            cur_pos = self._p2_pawn
        if cur_pos[0] == pos[0] + 2 and cur_pos[1] == pos[1]:
            return "Left Jump"
        elif cur_pos[0] == pos[0] - 2 and cur_pos[1] == pos[1]:
            return "Right Jump"
        elif cur_pos[0] == pos[0] and cur_pos[1] == pos[1] + 2:
            return "Up Jump"
        elif cur_pos[0] == pos[0] and cur_pos[1] == pos[1] - 2:
            return "Down Jump"
        elif cur_pos[0] == pos[0] - 1 and cur_pos[1] == pos[1] - 1:
            return "Down Right Diagonal"
        elif cur_pos[0] == pos[0] + 1 and cur_pos[1] == pos[1] + 1:
            return "Up Left Diagonal"
        elif cur_pos[0] == pos[0] + 1 and cur_pos[1] == pos[1] - 1:
            return "Down Left Diagonal"
        elif cur_pos[0] == pos[0] - 1 and cur_pos[1] == pos[1] + 1:
            return "Up Right Diagonal"

    def move_left(self, player, pos):
        """If the find_move_direction method finds that the player wants
        to move left, this method will first check if there
         is a fence in the way. If their is no fence, it will move their pawn
         and change the current player to the next player."""
        if self.display_right_fence(pos[0], pos[1]) is None:
            if player == 1:
                self._p1_pawn = pos
                self.change_player(1)
                return True
            elif player == 2:
                self._p2_pawn = pos
                self.change_player(2)
                return True
        return False

    def move_right(self, player, pos):
        """If the find_move_direction method finds that the player wants
        to move right, this method will first check if there
        is a fence in the way. If their is no fence, it will move their pawn
        and change the current player to the next player."""
        if self.display_left_fence(pos[0], pos[1]) is None:
            if player == 1:
                self._p1_pawn = pos
                self.change_player(1)
                return True
            elif player == 2:
                self._p2_pawn = pos
                self.change_player(2)
                return True
        return False

    def move_up(self, player, pos):
        """If the find_move_direction method finds that the player wants
        to move up, this method will first check if there
        is a fence in the way. If their is no fence, it will move their pawn
        and change the current player to the next player."""
        if self.display_down_fence(pos[0], pos[1]) is None:
            if player == 1:
                self._p1_pawn = pos
                self.change_player(1)
                return True
            if player == 2:
                self._p2_pawn = pos
                self.change_player(2)
                return True
        return False

    def move_down(self, player, pos):
        """If the find_move_direction method finds that the player wants
        to move down, this method will first check if there
        is a fence in the way. If their is no fence, it will move their pawn
        and change the current player to the next player."""
        if self.display_up_fence(pos[0], pos[1]) is None:
            if player == 1:
                self._p1_pawn = pos
                self.change_player(1)
                return True
            elif player == 2:
                self._p2_pawn = pos
                self.change_player(2)
                return True
        return False

    def jump_left(self, player, pos):
        """This method will check if a left jump is valid. If so, it will
        move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] + 1 != self._p2_pawn[0] or pos[1] != self._p2_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_right_fence(pos[0] + 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_left_fence(pos[0] + 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] + 1 != self._p1_pawn[0] or pos[1] != self._p1_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_right_fence(pos[0] + 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_left_fence(pos[0] + 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def jump_right(self, player, pos):
        """This method will check if a right jump is valid. If so, it will
        move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] - 1 != self._p2_pawn[0] or pos[1] != self._p2_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_left_fence(pos[0] - 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_right_fence(pos[0] - 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] - 1 != self._p1_pawn[0] or pos[1] != self._p1_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_left_fence(pos[0] - 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_right_fence(pos[0] - 1, pos[1]) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def jump_up(self, player, pos):
        """This method will check if a up jump is valid. If so, it will
        move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] != self._p2_pawn[0] or pos[1] + 1 != self._p2_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_down_fence(pos[0], pos[1] + 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_up_fence(pos[0], pos[1] + 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] != self._p1_pawn[0] or pos[1] + 1 != self._p1_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_down_fence(pos[0], pos[1] + 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_up_fence(pos[0], pos[1] + 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def jump_down(self, player, pos):
        """This method will check if a down jump is valid. If so, it will
        move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] != self._p2_pawn[0] or pos[1] - 1 != self._p2_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_up_fence(pos[0], pos[1] - 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_down_fence(pos[0], pos[1] - 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] != self._p1_pawn[0] or pos[1] - 1 != self._p1_pawn[1]:
                # Checks if the other pawn is there to be jumped over
                return False
            elif self.display_up_fence(pos[0], pos[1] - 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            elif self.display_down_fence(pos[0], pos[1] - 1) is True:
                # Checks if there is a fence blocking the jump
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def down_right_diagonal(self, player, pos):
        """This method will check if a down right diagonal move is valid.
        If so, it will move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] - 1 != self._p2_pawn[0] or pos[1] != self._p2_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_left_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_down_fence(pos[0] - 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] - 1 != self._p1_pawn[0] or pos[1] != self._p1_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_left_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_down_fence(pos[0] - 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def up_left_diagonal(self, player, pos):
        """This method will check if an up left diagonal move is valid.
        If so, it will move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] + 1 != self._p2_pawn[0] or pos[1] != self._p2_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_right_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_up_fence(pos[0] + 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] + 1 != self._p1_pawn[0] or pos[1] != self._p1_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_right_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_up_fence(pos[0] + 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def down_left_diagonal(self, player, pos):
        """This method will check if a down left diagonal move is valid.
        If so, it will move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] + 1 != self._p2_pawn[0] or pos[1] != self._p2_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_right_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_down_fence(pos[0] + 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] + 1 != self._p1_pawn[0] or pos[1] != self._p1_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_right_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_down_fence(pos[0] + 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def up_right_diagonal(self, player, pos):
        """This method will check if an up right diagonal move is valid.
        If so, it will move the player's pawn and change the current player."""
        if player == 1:
            if pos[0] - 1 != self._p2_pawn[0] or pos[1] != self._p2_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_left_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_up_fence(pos[0] - 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p1_pawn = pos
                self.change_player(1)
                return True
        if player == 2:
            if pos[0] - 1 != self._p1_pawn[0] or pos[1] != self._p1_pawn[1]:
                # Checks to see if the other pawn is facing the player's pawn
                return False
            if self.display_left_fence(pos[0], pos[1]) is True:
                # Checks to see if there is a fence blocking the move
                return False
            if self.display_up_fence(pos[0] - 1, pos[1]) is None:
                # Checks to see if the fence that allows for a diagonal move is present
                return False
            else:
                self._p2_pawn = pos
                self.change_player(2)
                return True

    def display_up_fence(self, x, y):
        """Displays whether a given cell has an upper fence or not"""
        return self._board.get_cell(x, y).get_fences().get_up_fence()

    def display_down_fence(self, x, y):
        """Displays whether a given cell has a lower fence or not"""
        return self._board.get_cell(x, y).get_fences().get_down_fence()

    def display_left_fence(self, x, y):
        """Displays whether a given cell has a left fence or not"""
        return self._board.get_cell(x, y).get_fences().get_left_fence()

    def display_right_fence(self, x, y):
        """Displays whether a given cell has a right fence or not"""
        return self._board.get_cell(x, y).get_fences().get_right_fence()


class Board:
    """Represents a board with a 9x9 grid and fences along the edges."""

    def __init__(self):
        """Creates a 9x9 grid with fences along the edges"""
        self._grid = []
        for i in range(9):
            self._grid.append([])  # Creates a list of 9 lists
            for j in range(9):
                self._grid[i].append(Cell())  # Appends a cell object to each of the 9 lists
        for i in range(9):
            self._grid[i][0].get_fences().set_up_fence(True)
            self._grid[0][i].get_fences().set_left_fence(True)
            self._grid[i][8].get_fences().set_down_fence(True)
            self._grid[8][i].get_fences().set_right_fence(True)

    def get_cell(self, x, y):
        """Returns a cell within the grid"""
        return self._grid[x][y]


class Cell:
    """Represents a cell with fences"""
    def __init__(self):
        """Creates a cell with a fence object"""
        self.fences = Fences()

    def get_fences(self):
        """Returns the fence object"""
        return self.fences


class Fences:
    """Represents the fences within the cells"""
    def __init__(self):
        """Creates a cell with fences initialized to None for all sides"""
        self._up = None
        self._down = None
        self._left = None
        self._right = None

    def get_up_fence(self):
        """Returns the upper fence of a cell"""
        return self._up

    def set_up_fence(self, val):
        """Sets the upper fence of a cell"""
        self._up = val

    def get_down_fence(self):
        """Returns the lower fence of a cell"""
        return self._down

    def set_down_fence(self, val):
        """Sets the lower fence of a cell"""
        self._down = val

    def get_left_fence(self):
        """Returns the left fence of a cell"""
        return self._left

    def set_left_fence(self, val):
        """Sets the left fence of a cell"""
        self._left = val

    def get_right_fence(self):
        """Returns the right fence of a cell"""
        return self._right

    def set_right_fence(self, val):
        """Sets the right fence of a cell"""
        self._right = val
