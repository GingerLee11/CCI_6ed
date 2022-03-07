# python3
# othello.py - Creates an othello board and allows two players to play a game.

from collections import deque

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
        self.opposites = {}


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

    def _generate_opposites(self):
        if self.opposites == {}: 
            first_list = [
                self.right,
                self.top_right,
                self.top,
                self.top_left,
                self.left,
                self.bottom_left,
                self.bottom,
                self.bottom_right,
            ]
            second_list = [
                self.left,
                self.bottom_left,
                self.bottom,
                self.bottom_right, 
                self.right,
                self.top_right,
                self.top, 
                self.top_left,
            ]
            # Iterate through to remove the Nones
            for first, second in zip(first_list, second_list):
                if first != None:
                    self.opposites[first] = second
            # self.opposites = dict(zip(first_list, second_list))

        
class Othello:

    def __init__(self):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.position_dict = {}
        self.black_count = 0
        self.white_count = 0
        self.curr_turn = 'Black'
        self.board = self._create_board()
        self.all_positions = self._all_positions()
        self.played_positions = self._check_if_played()
        self.empty_squares = self._find_empty_squares(self.all_positions, self.played_positions)
        self.possible_positions = self._check_possible_positions()

        # TODO: Create a counter for both White and Black to see who has more squares
        
        
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
                    elif square.pos in starting_black:
                        square.piece = 'Black'

                    square.right = grid[y][x + 1]
                    square.top_right = grid[y - 1][x + 1]
                    square.top = grid[y - 1][x]
                    square.top_left = grid[y - 1][x - 1]
                    square.left = grid[y][x - 1]
                    square.bottom_left = grid[y + 1][x - 1]
                    square.bottom = grid[y + 1][x]
                    square.bottom_right = grid[y + 1][x + 1]
                
                square.possible_options = square._check_possible_options()
                self.position_dict[square.pos] = square
                square._generate_opposites()

                if square.piece == 'Black':
                    self.black_count += 1
                elif square.piece == 'White':
                    self.white_count += 1

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
                square = board[x][y]
                if x == 0:
                    if square.pos in self.possible_positions:
                        print(f'{y} |(     )|', end='')
                    elif square.piece == None:
                        print(f'{y} |       |', end='')
                    else:
                        print(f"{y} | {square.piece} |",end='')
                else:
                    if square.pos in self.possible_positions:
                        print('(     )|', end='')
                    elif square.piece == None:
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
        empty_squares = list(set(all_squares)-set(p_squares))
        self.empty_squares = empty_squares
        return empty_squares

    def _search_opposite(self, opposite, current):
        """
        Recursive function that searches in one direction opposite of the current option of the current square.
        option <--> current <--> opposite
        Returns True if opposite sqaure is equal to the current color of the turn (e.g. 'White' or 'Black')
        """
        if opposite != None:
            if opposite.piece == None:
                return False
            elif opposite.piece == self.curr_turn:
                return True
            else:
                new_opposite = opposite.opposites[current]
                return self._search_opposite(new_opposite, opposite)

    def _check_possible_positions(self):
        """
        Checks the possible options for the player before any moves are made.
        """
        posssible_positions = []
        for square in self.played_positions:
            played_square = self.position_dict[square]
            for option in played_square.possible_options:
                if played_square.piece != self.curr_turn:
                    if option.piece == None:
                        opposite = played_square.opposites[option]
                        square_possible = self._search_opposite(opposite, played_square)
                        if square_possible == True:
                            if option.pos not in posssible_positions:
                                posssible_positions.append(option.pos)

        return posssible_positions
        

    def play_game(self):
        """
        Method starts the game and 
        runs the game until all the spaces have been played or 
        both player can no longer play.
        """
        print("Game start! Black goes first.")

        while len(self.empty_squares) != 0:

            count = 0
        
            # Print board to show options for black.
            self.curr_turn = 'Black'
            self.possible_positions = self._check_possible_positions()
            self.print_board()
            print(f"Number of pieces: Black: {self.black_count}, White: {self.white_count}\n")
            comma = ', '
            print(f'Options to play for {self.curr_turn}:')
            print(f'{comma.join(f"{pos}" for pos in self.possible_positions)}')
            
            # Checks to see if there are any possible moves to play
            # If not go to next player
            # If neither player can play, then the game ends
            if len(self.possible_positions) > 0:
                black_turn = pyip.inputCustom(self._valid_position, prompt=f"{self.curr_turn}: Please place a piece.\n", )
                piece = self._add_piece(black_turn)
                self.played_positions.append(piece)
                print(f'{self.curr_turn} played {piece}')
                
                # Refresh the number of empty squares
                self._find_empty_squares(self.all_positions, self.played_positions)
            
            else:
                count += 1
            

            # Print the board after the piece is played to show options for white.
            self.curr_turn = 'White'
            self.possible_positions = self._check_possible_positions()
            self.print_board()
            print(f"Number of pieces: Black: {self.black_count}, White: {self.white_count}\n")

            comma = ', '
            print(f'Options to play for {self.curr_turn}:')
            print(f'{comma.join(f"{pos}" for pos in self.possible_positions)}')

            if len(self.possible_positions) > 0:
                white_turn = pyip.inputCustom(self._valid_position, prompt=f"{self.curr_turn}: Please place a piece.\n", )
                piece = self._add_piece(white_turn)
                self.played_positions.append(piece)
                print(f'{self.curr_turn} played {piece}')

                self.curr_turn = 'Black'
                self.possible_positions = self._check_possible_positions()
                # self.print_board()

                # Refresh the number of empty squares
                self._find_empty_squares(self.all_positions, self.played_positions)
            
            else:
                count += 1

            if count == 2:
                break

        self.print_board()
        print(f"Number of pieces: Black: {self.black_count}, White: {self.white_count}\n")

        # Determine who wins; based on the number of pieces each player has.
        if self.black_count > self.white_count:
            print(f'Black wins!')
        elif self.white_count > self.black_count:
            print(f"White wins!")
        elif self.white_count == self.black_count:
            print("It's a tie!")


    def _valid_position(self, text):
        position_combos = self.all_positions
        
        if text not in position_combos:
            raise Exception("Inputted position is not on the board")
        if text in self.played_positions:
            raise Exception("Must choose a position that hasn't already been played.")

        if text not in self.possible_positions:
            raise Exception(f"Position played is not a valid position.\n Please choose from the following positions:\n {self.possible_positions}")
        

    def _flip_piece(self, square, option):
        """
        Flips piece adjacent to the current square if a piece color change has occurred.

        Ex: None  | White | Black
            Black | Black | Black
        """
        
        opposite = option.opposites[square]
        if opposite != None:
            if opposite.piece != self.curr_turn:
                self._flip_piece(option, opposite)   
            if opposite.piece == self.curr_turn:
                if option.piece != None:
                    option.piece = self.curr_turn

                    # Increase the piece count for white or black
                    if self.curr_turn == 'Black':
                        self.black_count += 1
                        self.white_count -= 1
                    else:
                        self.white_count += 1
                        self.black_count -= 1

            
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
                    
                    # Increase the piece count for white or black
                    if self.curr_turn == 'Black':
                        self.black_count += 1
                    else:
                        self.white_count += 1

                    # Go through all the options for played piece 
                    # and check what piece need to be flipped
                    # Then return the piece
                    for option in square.possible_options:
                        if option.piece == None or option.piece == self.curr_turn:
                            continue
                        else:
                            self._flip_piece(square, option)

                    return square.pos


    
def example():

    othello_game = Othello()
    othello_game.play_game()


if __name__ == "__main__":
    example()



class Test(unittest.TestCase):

    

    expected_relationships = [
        # top
        [
            [], 
            ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'],
            ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'], 
            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
            ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'], 
            ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'], 
            ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'], 
            ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']
        ],
        # top_right
        [
            [],
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
            ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'],
            ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']
        ], 
        # Right
        [
            ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'],
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
            ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'],
            ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'],
            ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7']
        ], 
        # Bottom_right
        [
            ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
            ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'],
            ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
            ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'],
            ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'],
            ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7'],
            []
        ],
        # Bottom
        [
            ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'], 
            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
            ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'], 
            ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'], 
            ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'], 
            ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'], 
            ['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7'],
            []
        ],
        # Bottom_left
        [    
            ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
            ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
            ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6'],
            ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6'],
            ['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6'],
            []
        ],
        # Left
        [
            ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
            ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
            ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
            ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6'],
            ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6'],
            ['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6']
        ], 
        # top_left
        [
            [],
            ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
            ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
            ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
            ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6'],
            ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6']
        ],
        

    ]
    
    expected_board = [
        ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'], 
        ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'], 
        ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
        ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'], 
        ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'], 
        ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7'], 
        ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'], 
        ['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7']
        ] 



    def test_created_puzzle(self):
        
        expected = self.expected_board
            
        othello = Othello()
        othello_board = othello.board
        actual = []
        for y in range(len(othello_board)):
            row = []
            for x in range(len(othello_board[0])):
                square = othello_board[y][x]
                row.append(square.pos)
            print(f'Expected: {expected[y]}\n  Actual: {row}')

            actual.append(row)
        print(f'Expected: {expected}\n  Actual: {actual}')
        assert actual == expected

        expected_top = self.expected_relationships[0]
        expected_top_right = self.expected_relationships[1]
        expected_right = self.expected_relationships[2]
        expected_bottom_right = self.expected_relationships[3]
        expected_bottom = self.expected_relationships[4]
        expected_bottom_left = self.expected_relationships[5]
        expected_left = self.expected_relationships[6]
        expected_top_left = self.expected_relationships[7]

        actual_top = []
        actual_top_right = []
        actual_right = []
        actual_bottom_right = []
        actual_bottom = []
        actual_bottom_left = []
        actual_left = []
        actual_top_left = []

        for y in range(len(othello_board)):
            row_top = []
            row_top_right = []
            row_right = []
            row_bottom_right = []
            row_bottom = []
            row_bottom_left = []
            row_left = []
            row_top_left = []
            for x in range(len(othello_board[0])):
                square = othello_board[y][x]
                if square.top != None:
                    row_top.append(square.top.pos)
                    if square.right != None:
                        row_top_right.append(square.top_right.pos)
                if square.right != None:
                    row_right.append(square.right.pos)
                if square.bottom != None:
                    row_bottom.append(square.bottom.pos)
                    if square.right != None:
                        row_bottom_right.append(square.bottom_right.pos)  
                    if square.left != None:
                        row_bottom_left.append(square.bottom_left.pos)
                if square.left != None:
                    row_left.append(square.left.pos)
                    if square.top != None:
                        row_top_left.append(square.top_left.pos)         

            print(f'Expected top: {expected_top[y]}\n  Actual top: {row_top}')
            print(f'Expected top_right: {expected_top_right[y]}\n  Actual top_right: {row_top_right}')
            print(f'Expected right: {expected_right[y]}\n  Actual right: {row_right}')
            print(f'Expected bottom_right: {expected_bottom_right[y]}\n  Actual bottom_right: {row_bottom_right}')
            print(f'Expected bottom: {expected_bottom[y]}\n  Actual bottom: {row_bottom}')
            print(f'Expected bottom_left: {expected_bottom_left[y]}\n  Actual bottom_left: {row_bottom_left}')
            print(f'Expected left: {expected_left[y]}\n  Actual left: {row_left}')
            print(f'Expected top_left: {expected_top_left[y]}\n  Actual top_left: {row_top_left}')
            
            actual_top.append(row_top)
            actual_top_right.append(row_top_right)
            actual_right.append(row_right)
            actual_bottom_right.append(row_bottom_right)
            actual_bottom.append(row_bottom)
            actual_bottom_left.append(row_bottom_left)
            actual_left.append(row_left)
            actual_top_left.append(row_top_left)

        assert actual_top == expected_top
        assert actual_top_right == expected_top_right
        assert actual_right == expected_right
        assert actual_bottom_right == expected_bottom_right
        assert actual_bottom == expected_bottom
        assert actual_bottom_left == expected_bottom_left
        assert actual_left == expected_left
        assert actual_top_left == expected_top_left
            




