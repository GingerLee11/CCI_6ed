# python3
# tic_tac_toe.py - Creates a Tic Tac Toe game.

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
            if option != None:
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


        
class TicTacToe:

    def __init__(self):
        self.letters = ['A', 'B', 'C']
        self.position_dict = {}
        self.curr_turn = 'X'
        self.board = self._create_board()
        self.all_positions = self._all_positions()
        self.played_positions = self._check_if_played()
        self.empty_squares = self._find_empty_squares(self.all_positions, self.played_positions)
        self.possible_positions = self._check_possible_positions()


        # TODO: Create a counter for both White and Black to see who has more squares
        
        
        # Create either two possible position lists for black and white or use one and switch between
        
       

    def _create_grid(self):
        N = 3
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
                self.position_dict[square.pos] = square
                square._generate_opposites()

        return grid

    def print_board(self):
        """
        Prints the current state of the board
        """
        board = self.board
        letters = self.letters
        space = '  '
        space_2 = ' '
        top_of_board = f"  "
        for letter in letters:
            top_of_board += f"{space}{letter}{space_2}"
        print(top_of_board)
        print('  _____________')
        for y in range(len(board)):
            for x in range(len(board[0])):
                square = board[x][y]
                if x == 0:
                    if square.piece == None:
                        print(f'{y} |   |', end='')
                    else:
                        print(f"{y} | {square.piece} |",end='')
                else:
                    if square.piece == None:
                        print('   |', end='')
                    else:
                        print(f" {square.piece} |", end='')
            print('\n  _____________')

    def _all_positions(self):
        """
        Adds all the possible positions that can be played
        """
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

    def _check_possible_positions(self):
        """
        Checks the possible options for the player before any moves are made.
        """
        posssible_positions = []
        for square in self.all_positions:
            played_square = self.position_dict[square]
            if played_square.piece == None:
                posssible_positions.append(played_square.pos)

        return posssible_positions

    def _valid_position(self, text):
        """
        Checks whether the inputted position is valid.
        """
        position_combos = self.all_positions
        
        if text not in position_combos:
            raise Exception("Inputted position is not on the board")
        if text in self.played_positions:
            raise Exception("Must choose a position that hasn't already been played.")

        if text not in self.possible_positions:
            raise Exception(f"Position played is not a valid position.\n Please choose from the following positions:\n {self.possible_positions}")
        

    def play_2p_game(self):
        """
        Starts a two person game and checks to see if one of the players has won.
        """
        print('Game start! "X" goes first.')
        
        win_condition = False
        while win_condition == False:

            # Player "X"s turn:
            self.curr_turn = "X"
            X_turn = pyip.inputCustom(self._valid_position, prompt=f'Player "{self.curr_turn}" Please place a piece.\n', )
            piece = self._add_piece(X_turn)
            self.played_positions.append(piece)
            self.print_board()
            win_condition = self._check_for_win()
            if win_condition == True:
                print(f'Player "{self.curr_turn}" won!')
                break
            
            # Check if it's a tie
            self._find_empty_squares(self.all_positions, self.played_positions)
            if len(self.empty_squares) < 1:
                print("Tie! Cat Game!")
                break

            # Player "O"s turn:
            self.curr_turn = "O"
            O_turn = pyip.inputCustom(self._valid_position, prompt=f'Player "{self.curr_turn}" Please place a piece.\n', )
            piece = self._add_piece(O_turn)
            self.played_positions.append(piece)
            self.print_board()
            win_condition = self._check_for_win()
            if win_condition == True:
                print(f'Player "{self.curr_turn}" won!')
                break

            # Check if it's a tie
            self._find_empty_squares(self.all_positions, self.played_positions)
            if len(self.empty_squares) < 1:
                print("Tie! Cat Game!")
                break


    def _add_piece(self, position):
        """
        Adds a piece "X" or "O" onto the board.
        """
        square = self.position_dict[position]
        square.piece = self.curr_turn
        return square.pos

    def _check_for_win(self):
        """
        Checks after every piece is played.
        """
        for square in self.played_positions:
            played_square = self.position_dict[square]
            # Make sure to check for the curr turn.
            if played_square.piece == self.curr_turn:
                # Check the adjacent squares to see if any of them match
                for option in played_square.possible_options:
                    # Check if the piece is the same for the adjacent square
                    # and the square on the opposite side of that.
                    if option.piece == self.curr_turn:
                        opposite = played_square.opposites[option]
                        if opposite != None:
                            if opposite.piece == self.curr_turn:
                                return True
        return False


                    






def example():

    tic_tac_toe_game = TicTacToe()
    tic_tac_toe_game.print_board()
    tic_tac_toe_game.play_2p_game()


if __name__ == "__main__":
    example()