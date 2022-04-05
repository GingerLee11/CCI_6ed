# python3
# eight_queens.py - Prints out all the possible positions that eight queens could inhabit on a chess board.


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

        
class Chess:

    def __init__(self):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.position_dict = {}
        self.queens = []
        self.board = self._create_board()
        
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
        space = '    '
        space_2 = '   '
        top_of_board = f"  "
        for letter in letters:
            top_of_board += f"{space}{letter}{space_2}"
        print(top_of_board)
        print('  ________________________________')
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
            print('\n  ________________________________')


    def eight_queens(self, num_queens):
        """
        Prints out all the possible positions that eight queens could inhabit on a chess board.
        """
        board = self.board
        row = 0

        for col in range(len(board[0]) -1, 0, -1):
            if len(self.queens) != 0:
                self.clear_queens()
            square = board[col][row]
            square.piece = 'Q'
            self.queens.append(square)
            self.find_spots_for_queens(num_queens, col)


    def find_spots_for_queens(self, num_queens, starting_col):
        """
        Iterates though all the possible spots that the eight queens could go.
        """
        cols = [y for y in range(len(self.board[0]))]
        rows = [x for x in range(len(self.board))]

        backwards_cols = cols[starting_col::-2]
        forward_cols = [col for col in cols if col not in backwards_cols] 

        
        while len(self.queens) < num_queens:
            last_row = 0
            for col in (backwards_cols + forward_cols):
                for row in rows[last_row :] + rows[: last_row]:
                    square = self.board[col][row]
                    if square.piece == 'Q':
                        break
                    for option in square.possible_options:
                        has_queen = self.check_option(option, square)
                        if has_queen == True:
                            break
                    
                    if has_queen == True:
                        continue
                    elif has_queen == False:
                        square.piece = 'Q'
                        self.queens.append(square)
                        last_row = row
                        break


        self.print_board()

    def check_option(self, option, square):
        """
        Recursively check all the way down an option.
        """
        # Bases Cases:
        if option == None:
            return False
        if option.piece == 'Q':
            return True
        next_sqaure = option.opposites[square]
        return self.check_option(next_sqaure, option)

    def clear_queens(self):
        for square in self.queens:
            square.piece = None



def example():


    chess_board = Chess()
    chess_board.eight_queens(8)

    
if __name__ == "__main__":
    example()
