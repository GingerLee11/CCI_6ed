# python3
# langtons_ant.py - Prints out K moves of an ant moving through an initially all white grid of squares.

from string import ascii_lowercase


class Square:

    def __init__(self, x, y, pos):
        self.color = 'W'
        self.has_ant = False

        # Position of square on the grid
        self.x = x
        self.y = y
        self.pos = pos

        # Adjacent squares:
        # Based on 360 degree coordinates with positive x-axis as 0 or 360
        self.right = None
        self.top = None
        self.left = None
        self.bottom = None

        self.possible_options = self._check_possible_options()


    def _setup_adj_squares(self):
        adj_squares_dict = {
            0: self.right,
            90: self.top,
            180: self.left,
            270: self.bottom,
            -90: self.bottom,
            -180: self.left,
            -270: self.top,
        }
        return adj_squares_dict


    def _check_possible_options(self):
        possible_options = []
        check_options = [
            self.right, 
            self.top, 
            self.left, 
            self.bottom, 
        ]
        for option in check_options:
            if option !=None:
                possible_options.append(option)

        return possible_options
      

class LangtonsAnt:

    def __init__(self, N):
        self.letters = list(ascii_lowercase)
        self.N = N
        self.position_dict = {}
        self.grid = self._create_grid()


    def _setup_grid(self, N):
        """
        Sets up the grid for further relational mapping.
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

    def _create_grid(self):
        """
        Creates the full grid with all the relationships established
        """
        grid = self._setup_grid(self.N)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                square = grid[y][x]

                # This is for the (unrealistic) situation where there would only be one square in the puzzle
                if y == 0 and y == len(grid) - 1:
                    break

                if y == 0:
                    square.bottom = grid[y + 1][x]
                    if x == 0:
                        square.right = grid[y][x + 1]
                    elif x == len(grid[0]) -1:
                        square.left = grid[y][x - 1]
                    else:
                        square.left = grid[y][x - 1]
                        square.right = grid[y][x + 1]
                elif y == len(grid) -1:
                    square.top = grid[y - 1][x]
                    if x == 0:
                        square.right = grid[y][x + 1]
                    elif x == len(grid[0]) -1:
                        square.left = grid[y][x - 1]
                    else:
                        square.left = grid[y][x - 1]
                        square.right = grid[y][x + 1]
                elif x == 0:
                    square.top = grid[y - 1][x]
                    square.right = grid[y][x + 1]
                    square.bottom = grid[y + 1][x]
                elif x == len(grid[0]) -1:
                    square.top = grid[y - 1][x]
                    square.left = grid[y][x - 1]
                    square.bottom = grid[y + 1][x]
                else:
                    square.top = grid[y - 1][x]
                    square.right = grid[y][x + 1]
                    square.bottom = grid[y + 1][x]
                    square.left = grid[y][x - 1]

                square.possible_options = square._check_possible_options()
                square.adj_squares_dict = square._setup_adj_squares()
                self.position_dict[square.pos] = square
                    
        return grid


    def print_grid(self):
        """
        Prints the current state of the grid
        """
        grid = self.grid
        letters = self.letters
        space = '  '
        numbers_on_top = f' {space}'
        for x in range(len(grid[0])):
            numbers_on_top += f"{space}{letters[x]} "
        horizontal_line_segment = '____'
        horizontal_line = horizontal_line_segment * self.N
        print()
        print(numbers_on_top)
        print(f"{space} {horizontal_line}")
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                square = grid[y][x]
                if x == 0:

                    if y < 10:
                        if square.has_ant == True:
                            print(f'{y}  | ⊝ |', end='')
                        else:    
                            print(f'{y}  | {square.color} |', end='')

                    else:
                        if square.has_ant == True:
                            print(f'{y} | ⊝ |', end='')
                        else:
                            print(f'{y} | {square.color} |', end='')
                    

                else:
                    if square.has_ant == True:
                        print(f' ⊝ |', end='')
                    else:
                        print(f' {square.color} |', end='')

            print(f'\n   {horizontal_line}')

    
    def k_moves(self, k):
        """
        Prints k moves of the ant on the grid.
        """
        # Find the middle of the grid to start
        middle_of_grid = round(self.N / 2)
        x = middle_of_grid
        y = self.letters[middle_of_grid]
        pos = f"{y}{x}"
        # Find the initial position for the ant
        square = self.position_dict[pos]
        ant = 0

        # Move the ant K moves
        for i in range(k):

            if square == None:
                self.print_grid()
                print(f"The Ant has fallen off the grid after {i} moves!")
                break
            
            square.has_ant = True
            
            # Print the grid every move to see how the ant moves
            # self.print_grid()

            if square.color == 'W':
                square.color = 'B'
                ant -= 90
                # To check if the ant has gone full circle to speak
                if ant == 360 or ant == -360:
                    ant = 0

                square.has_ant = False
                # The ants moves to the next square
                square = square.adj_squares_dict[ant]
            
            elif square.color == 'B':
                square.color = 'W'
                ant += 90
                # To check if the ant has gone full circle to speak
                if ant == 360 or ant == -360:
                    ant = 0
                
                square.has_ant = False
                # The ants moves to the next square
                square = square.adj_squares_dict[ant]


def example():

    langtons_ant = LangtonsAnt(26)
    langtons_ant.k_moves(10000)


if __name__ == "__main__":
    example()
