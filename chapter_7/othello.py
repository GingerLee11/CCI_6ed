# python3
# othello.py - Creates an othello board and allows two players to play a game.


import unittest

import pyinputplus as pyip

class Square:

    def __init__(self, x, y, pos, piece=None):
        self.piece = piece
        
        # Position of square on the board
        self.x = x
        self.y = y
        self.pos = pos

        # Adjacent squares:
        self.right = None
        self.top_right = None
        self.top = None
        self.top_left = None
        self.left = None
        self.bottom_left = None
        self.bottom = None
        self.bottom_right = None

        # Create a list of potential options for all squares
        self.possible_options = self._check_possible_options()


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

    def play_options(self):
        pass

        
class Othello:

    def __init__(self):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.board = self._create_board()
        self.all_positions = self._all_positions()
        self.played_positions = self._check_if_played()
        self.empty_squares = list(self._find_empty_squares(self.all_positions, self.played_positions))
        self.possible_positions = self._check_possible_positions()
        self.curr_turn = None
        self.next_turn = None
        # Create either two possible position lists for black and white or use one and switch between
        
       

    def _create_grid(self):
        N = 8
        letters = self.letters
        grid = []
        for y in range(N):
            row = []
            for x in range(N):
                pos = f'{letters[y]}{x}'
                square = Square(x, letters[y], pos)
                row.append(square)
            grid.append(row)

        return grid

    def _create_board(self):
        """
        Creates a standard Othello board.
        """
        grid = self._create_grid()

        starting_white, starting_black = ['D3', 'E4'], ['D4', 'E3']

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
                    if square.pos in starting_white:
                        square.piece = 'White'
                        square.is_empty = False
                    elif square.pos in starting_black:
                        square.piece = 'Black'
                        square.is_empty = False

                    square.right = grid[y][x + 1]
                    square.top_right = grid[y - 1][x + 1]
                    square.top = grid[y - 1][x]
                    square.top_left = grid[y - 1][x - 1]
                    square.left = grid[y][x - 1]
                    square.bottom_left = grid[y + 1][x - 1]
                    square.bottom = grid[y + 1][x]
                    square.bottom_right = grid[y + 1][x + 1]
                
                square.possible_options = square._check_possible_options()

        return grid

    def print_board(self):
        """
        Prints the current state of the board
        """
        board = self.board
        letters = self.letters
        space = '    '
        space_2 = '   '
        top_of_board = f"  "
        for letter in letters:
            top_of_board += f"{space}{letter}{space_2}"
        print(top_of_board)
        print('  _________________________________________________________________')
        for y in range(len(board)):
            for x in range(len(board[0])):
                square = board[y][x]
                if x == 0:
                    if square.piece == None:
                        print(f'{y} |       |', end='')
                    else:
                        print(f"| {square.piece} |",end='')
                else:
                    if square.piece == None:
                            print('       |', end='')
                    else:
                        print(f" {square.piece} |", end='')
            print('\n  _________________________________________________________________')


    def _all_positions(self):
        letters = self.letters
        vertical = [letters[y] for y in range(len(self.board))]
        horizontal = [x for x in range(len(self.board[0]))]
        pos_combos = []
        for y in vertical:
            for x in horizontal:
                pos = f"{y}{x}"
                pos_combos.append(pos)
        return pos_combos

    def _check_if_played(self, squares_with_pieces=None):
        if squares_with_pieces == None:
            squares_with_pieces = []
        
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                square = self.board[y][x]
                if square.pos in squares_with_pieces:
                    continue
                if square.piece != None:
                    squares_with_pieces.append(square.pos)

        return squares_with_pieces

    def _find_empty_squares(self, all_squares, p_squares):
        return set(all_squares)-set(p_squares)

    def _check_possible_positions(self):
        for square in self.empty_squares:
            for option in square.possible_options:
                # TODO: figure out how to find possible options
                pass


    def play_game(self):
        
        print("Game start! Black goes first.")
        
        self.curr_turn = 'Black'
        self.next_turn = 'White'
        # TODO: Update possible positions for black
        
        black_turn = pyip.inputCustom(self._valid_position, prompt="Black: Please place a piece.", )
        self._add_piece(black_turn)

        self.next_turn = 'Black'
        self.curr_turn = 'White'
        


    def _valid_position(self, text):
        position_combos = self.all_positions
        
        if text not in position_combos:
            raise Exception("Inputted position is not on the board")
        if text in self.played_positions:
            raise Exception("Must choose a position that hasn't already been played.")

        # TODO: Check to make sure the position is a possible play
        
               

    def _add_piece(self, position):
        """
        Adds a piece to the board.
        And checks for any changes.
        """
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                square = self.board[y][x]
                if square.pos == position:
                    square.piece = self.curr_turn
                    break

        if square.right != None:
            square_right = square.right
        # self._check_horizontal





    def _check_horizontal(self, squares, square_left=None):
        pass

    def _check_vertical(self, square):
        pass

    def _check_diagonal(self, square):
        pass


    
def example():

    othello_game = Othello()
    othello_game.print_board()


if __name__ == "__main__":
    example()

    

