# python3
# minesweeper.py - Text-based minesweeper game.


from random import randint
import string

import pyinputplus as pyip


class Square:

    def __init__(self, x, y, grid_number):
        self.num_adj_bombs = 0
        self.bomb = False
        self.flagged = False

        # Position of square on the board
        self.x = x
        self.y = y
        self.grid_number = grid_number
        # Adjacent squares:
        self.right = None
        self.top_right = None
        self.top = None
        self.top_left = None
        self.left = None
        self.bottom_left = None
        self.bottom = None
        self.bottom_right = None

        self.possible_options = self._check_possible_options()

    def _search_adj_for_bombs(self):
        if self.bomb == True:
            self.num_adj_bombs = None
        else:
            adjacent_squares = [
                self.right, 
                self.top_right, 
                self.top, 
                self.top_left, 
                self.left, 
                self.bottom_left, 
                self.bottom, 
                self.bottom_right, 
            ]
            for square in adjacent_squares:
                if square.bomb == True:
                    self.num_adj_bombs += 1


    def _check_possible_options(self):
        possible_options = []
        check_options = [
            self.right, 
            self.top_right, 
            self.top, 
            self.top_left, 
            self.left, 
            self.bottom_left, 
            self.bottom, 
            self.bottom_right, 
        ]
        for option in check_options:
            if option !=None:
                possible_options.append(option)

        return possible_options
        


class Minesweeper:
    """
    Text-based minesweeper game.
    """
    
    def __init__(self, N=6, num_bombs=3):
        self.letters = list(string.ascii_uppercase)
        if N <= len(self.letters):
            self.N = N
        else:
            self.N = 20
        self.num_bombs = num_bombs 

        self.position_dict = {}
        self.flags_left = num_bombs
        self.bomb_locations = []
        self.revealed = []
        self.flagged = []

        # Creates the board
        self.board = self._create_board()
        

    
    def _create_grid(self, N):
        """
        Creates the basic grid for the game.
        """
        
        grid = []
        for y in range(N):
            row = []
            for x in range(N):
                pos = f"{self.letters[y]}{x}"
                square = Square(x, y, pos)
                row.append(square)
            grid.append(row)

        return grid

    def _place_bombs(self, N, grid):
        """
        Places the bombs in random locations
        """
        while len(self.bomb_locations) < self.num_bombs:
            x = randint(0, N - 1)
            y = randint(0, N - 1)
            square = grid[y][x]
            if square.bomb == False:
                square.bomb = True
                for option in square.possible_options:
                    if option.bomb == False:
                        option.num_adj_bombs += 1
                
                self.bomb_locations.append(square.grid_number)
            
        return grid

        
    def _create_board(self):
        """
        Creates board for the game based on dimensions and number of bombs given.
        """
        N = self.N
        grid = self._create_grid(N)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                square = grid[y][x]
                
                if y == 0:
                    square.bottom = grid[y + 1][x]
                    if x == 0:
                        square.bottom_right = grid[y + 1][x + 1]
                        square.right = grid[y][x + 1]
                    elif x == len(grid[0]) - 1:
                        square.bottom_left = grid[y + 1][x - 1]
                        square.left = grid[y][x - 1]
                    else:
                        square.right = grid[y][x + 1]
                        square.bottom_right = grid[y + 1][x + 1]
                        square.bottom_left = grid[y + 1][x - 1]
                        square.left = grid[y][x - 1]
                
                elif y == len(grid) -1:
                    square.top = grid[y - 1][x]
                    if x == 0:
                        square.top_right = grid[y - 1][x + 1]
                        square.right = grid[y][x + 1]
                    elif x == len(grid[0]) - 1:
                        square.top_left = grid[y - 1][x - 1]
                        square.left = grid[y][x - 1]
                    else:
                        square.right = grid[y][x + 1]
                        square.top_right = grid[y - 1][x + 1]
                        square.top_left = grid[y - 1][x - 1]
                        square.left = grid[y][x - 1]
                
                elif x == 0:
                    square.right = grid[y][x + 1]
                    square.top_right = grid[y - 1][x + 1]
                    square.top = grid[y - 1][x]
                    square.bottom = grid[y + 1][x]
                    square.bottom_right = grid[y + 1][x + 1]

                elif x == len(grid[0]) - 1:
                    square.left = grid[y][x - 1]
                    square.bottom_left = grid[y + 1][x - 1]
                    square.bottom = grid[y + 1][x]
                    square.top = grid[y - 1][x]
                    square.top_left = grid[y - 1][x - 1]

                else:
                    square.right = grid[y][x + 1]
                    square.top_right = grid[y - 1][x + 1]
                    square.top = grid[y - 1][x]
                    square.top_left = grid[y - 1][x - 1]
                    square.left = grid[y][x - 1]
                    square.bottom_left = grid[y + 1][x - 1]
                    square.bottom = grid[y + 1][x]
                    square.bottom_right = grid[y + 1][x + 1]
                
                square.possible_options = square._check_possible_options()
                self.position_dict[square.grid_number] = square

        grid_with_bombs = self._place_bombs(N, grid)

        return grid_with_bombs

    
    def print_board(self):
        """
        Prints the current state of the board
        """
        board = self.board
        letters = self.letters
        space = '  '
        numbers_on_top = f' {space}'
        for x in range(len(board[0])):
            numbers_on_top += f"{space}{letters[x]} "
        horizontal_line_segment = '____'
        horizontal_line = horizontal_line_segment * self.N
        print()
        print(numbers_on_top)
        print(f"{space} {horizontal_line}")
        for y in range(len(board)):
            for x in range(len(board[0])):
                square = board[x][y]
                if x == 0:

                        if y < 10:
                            if square.grid_number in self.flagged:
                                print(f'{y}  | F |', end='')

                            elif square.bomb == True:
                                    print(f'{y}  |[ ]|', end='')

                            elif square.grid_number in self.revealed:
                                if square.num_adj_bombs != 0:
                                    print(f'{y}  | {square.num_adj_bombs} |', end='')
                                else:
                                    print(f'{y}  |   |', end='')

                            
                            else:
                                print(f'{y}  |[ ]|', end='')
                        else:
                            if square.grid_number in self.flagged:
                                print(f'{y} | F |', end='')
                            
                            elif square.bomb == True:
                                    print(f'{y} |[ ]|', end='')

                            elif square.grid_number in self.revealed:
                                if square.num_adj_bombs != 0:
                                    print(f'{y} | {square.num_adj_bombs} |', end='')
                                else:
                                    print(f'{y} |   |', end='')
                            
                            else:
                                print(f'{y} |[ ]|', end='')
                    

                else:
                    if square.grid_number in self.flagged:
                        print(f' F |', end='')

                    elif square.bomb == True:
                        print(f'[ ]|', end='')

                    elif square.grid_number in self.revealed:
                        
                        if square.num_adj_bombs != 0:
                            print(f' {square.num_adj_bombs} |', end='')
                        elif square.bomb == False:
                            print(f'   |', end='')
                    
                    else:
                        print(f'[ ]|', end='')

            print(f'\n   {horizontal_line}')

    def print_game_over_board(self):
        """
        Shows where the bombs are when the player loses.
        """
        board = self.board
        letters = self.letters
        space = '  '
        numbers_on_top = f' {space}'
        for x in range(len(board[0])):
            numbers_on_top += f"{space}{letters[x]} "
        horizontal_line_segment = '____'
        horizontal_line = horizontal_line_segment * self.N
        print()
        print(numbers_on_top)
        print(f"{space} {horizontal_line}")
        for y in range(len(board)):
            for x in range(len(board[0])):
                square = board[x][y]
                if x == 0:

                        if y < 10:

                            if square.grid_number in self.bomb_locations:
                                print(f'{y}  | B |', end='')
                        
                            elif square.grid_number in self.flagged:

                                if square.bomb == True:
                                    print(f'{y}  | B |', end='')
                                
                                else:
                                    print(f'{y}  | X |', end='')

                            
                            elif square.grid_number in self.revealed:
                                if square.num_adj_bombs != 0:
                                    print(f'{y}  | {square.num_adj_bombs} |', end='')
                                else:
                                    print(f'{y}  |   |', end='')

                            
                            else:
                                print(f'{y}  |[ ]|', end='')
                        else:
                            if square.grid_number in self.bomb_locations:
                                print(f'{y} | B |', end='')
                            
                            
                            elif square.grid_number in self.flagged:
  
                                if square.bomb == True:
                                    print(f'{y} | B |', end='')
                                else:
                                    print(f'{y} | X |', end='')

                            elif square.grid_number in self.revealed:
                                if square.num_adj_bombs != 0:
                                    print(f'{y} | {square.num_adj_bombs} |', end='')
                                else:
                                    print(f'{y} |   |', end='')
                            
                            else:
                                print(f'{y} |[ ]|', end='')
                    

                else:
                    if square.grid_number in self.bomb_locations:
                        print(f' B |', end='')

                    elif square.grid_number in self.flagged:

                        if square.bomb == True:
                            print(f' B |', end='')
                        else:
                            print(f' X |', end='')

                    elif square.grid_number in self.revealed:
                        
                        if square.num_adj_bombs != 0:
                            print(f' {square.num_adj_bombs} |', end='')
                        elif square.bomb == False:
                            print(f'   |', end='')
                    
                    else:
                        print(f'[ ]|', end='')

            print(f'\n   {horizontal_line}')

    def _print_board_with_bombs(self):
        """
        Prints the board completely revealed.
        """
        board = self.board
        letters = self.letters
        space = '  '
        numbers_on_top = f' {space}'
        for x in range(len(board[0])):
            numbers_on_top += f"{space}{letters[x]} "
        horizontal_line_segment = '____'
        horizontal_line = horizontal_line_segment * self.N
        print()
        print(numbers_on_top)
        print(f"{space} {horizontal_line}")
        for y in range(len(board)):
            for x in range(len(board[0])):
                square = board[x][y]
                if x == 0:
                        if y < 10:                                
                                if square.bomb == True:
                                    print(f'{y}  | B |', end='')
                                
                                elif square.num_adj_bombs != 0:
                                    print(f'{y}  | {square.num_adj_bombs} |', end='')

                                else:
                                    print(f'{y}  |   |', end='')       
                        else:
                            
                                if square.bomb == True:
                                    print(f'{y} | B |', end='')
                                
                                elif square.num_adj_bombs != 0:
                                    print(f'{y} | {square.num_adj_bombs} |', end='')
                                
                                else:
                                    print(f'{y} |   |', end='')
                else:   
                    if square.bomb == True:
                        print(f' B |', end='')
                    elif square.num_adj_bombs != 0:
                        print(f' {square.num_adj_bombs} |', end='')
                    else:
                        print(f'   |', end='')

            print(f'\n   {horizontal_line}')


    def _valid_position(self, text):
        
        if text not in self.position_dict:
            raise Exception("Inputted position is not on the board")

        if text in self.revealed and text not in self.flagged:
            raise Exception("Must choose a position that hasn't already been played.")

        '''
        if text in self.flagged:
            raise Exception(f"Can not select a position that has been flagged. Flagged positions:\n {self.flagged}")
        '''

    def _reveal_squares(self, square):
        """
        Reveals all squares adjacent to inputted position
        and all positions adjacent to those positions up until squares with adjacent bombs. 
        """
        if square.bomb == False: 
            if square.grid_number not in self.revealed:
                self.revealed.append(square.grid_number)
                if square.grid_number in self.flagged:
                    self.flagged.remove(square.grid_number)
                    self.flags_left += 1
            if square.num_adj_bombs == 0:
                for option in square.possible_options:
                    if option.grid_number not in self.revealed:
                        if option.num_adj_bombs != 0:
                            self.revealed.append(option.grid_number)
                            if option.grid_number in self.flagged:
                                self.flagged.remove(option.grid_number)
                                self.flags_left += 1

                        # Recursive call if the adjacent square doesn't have any adjacent bombs
                        else:
                            self._reveal_squares(option)

    def _flag_square(self, square):
        """
        Flags the sqaure inputted.
        """
        square.flagged = True
        self.flags_left -= 1
        self.flagged.append(square.grid_number)
        return square

    def play_game(self):
        """
        Starts the single player game.
        """
        print("Game start!")
        self.print_board()
        turn = None
        while turn not in self.bomb_locations or ((len(self.revealed) + len(self.flagged)) < len(self.position_dict)):
        
            turn = pyip.inputCustom(self._valid_position, prompt=f"Please type in a square (Ex: A0).\n\n")

            square = self.position_dict[turn]

            if turn in self.flagged:
                unflag = pyip.inputYesNo(f"Would you like to unflag this position: {turn}?\n")
                if unflag == 'yes':
                    square.flagged = False
                    self.flags_left += 1
                    self.flagged.remove(square.grid_number)
                self.print_board()
                print(f"\nFlags remaining: {self.flags_left}\n")
                continue



            if self.flags_left > 0:

                flag_or_reveal = pyip.inputChoice(prompt="\nPlease type in either 'f': (flag) or 'r': (reveal) this position:\n", choices=['F', 'R'])

            else: 
                flag_or_reveal = 'R'

            

            if flag_or_reveal == 'F':
                self._flag_square(square)

            elif flag_or_reveal == 'R':
                if turn in self.bomb_locations:
                    print("Bomb!\nGame Over.")
                    self.print_game_over_board()
                    break
                self._reveal_squares(square)

            self.print_board()
            print(f"\nFlags remaining: {self.flags_left}\n")

            if len(self.revealed) == len(self.position_dict) - len(self.bomb_locations):
                print("Congratulations! You won!")
                self.print_game_over_board()
                break



def example():

    minesweeper = Minesweeper(6, 5)
    minesweeper.play_game()
        

if __name__ == "__main__":
    example()

