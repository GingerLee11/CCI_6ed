# python3
# robot_in_a_grid.py - Finds a path through a grid that a robot can take moving only right and down.

from operator import imod, le
from random import randint


class Square:
    """
    Jigsaw puzzle piece subclass.
    """
    def __init__(self, grid_number):
        self.off_limits = False
        self.right = None
        self.down = None
        self.grid_number = grid_number


class Grid:
    """
    Creates an N x N grid for a robot maze.
    """
    def __init__(self, r, c, num_off_limit_squares):
        self.r = r
        self.c = c
        self.off_limits_locations = []
        if num_off_limit_squares <= (r * c) / 8:
            self.num_off_limit_squares = num_off_limit_squares
        else:
            self.num_off_limit_squares = (r * c) / 8
        self.grid = self._fill_grid()

    def _create_grid(self, r, c):
        """
        Creates a grid containing all the pieces without any relationships.
        """
        
        grid = []
        for y in range(r):
            row = []
            y *= r
            for x in range(c):
                piece = Square(x + y)
                row.append(piece)
            grid.append(row)
            

        return grid


    def _place_off_limit_cells(self, grid):
        """
        Places the bombs in random locations
        """

        while len(self.off_limits_locations) < self.num_off_limit_squares:
            x = randint(0, self.c - 1)
            y = randint(0, self.r - 1)
            square = grid[y][x]
            # Shorten to improve legibility of if statements
            num = square.grid_number
            # Make sure the robot can get out initially
            if num != 0 and num != 1 and num != self.c:
                # Make sure the goal isn't off_limits
                if num != (self.c * self.r) - 1 and num != (self.c * self.r) - 2 and num != (self.c * self.r) - self.c:
                    if square.off_limits == False:
                        square.off_limits = True
                        self.off_limits_locations.append(square.grid_number)
            
        return grid

    
    def _fill_grid(self):
        """
        Creates the relationships betweeen grids
        """
        grid = self._create_grid(self.r , self.c)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                piece = grid[y][x]

                # This is for the (unrealistic) situation where there would only be one square
                if y == 0 and y == len(grid) - 1:
                    break
                if y == 0:
                    piece.down = grid[y + 1][x]
                    if x != len(grid[0]) - 1:
                        piece.right = grid[y][x + 1]

                elif y == len(grid) -1:
                    if x != len(grid[0]) - 1:
                        piece.right = grid[y][x + 1]

                elif x == 0:
                    piece.right = grid[y][x + 1]
                    piece.down = grid[y + 1][x]

                elif x == len(grid[0]) -1: 
                    piece.down = grid[y + 1][x]

                else:
                    piece.right = grid[y][x + 1]
                    piece.down = grid[y + 1][x]


        grid = self._place_off_limit_cells(grid)        
                    

        return grid




def check_path_down(square):
    """
    Checks the paths going one left and then search down until 
    """
    until_off_limts = []

    while square != None:

        moves_until_off_limits = check_down(square)
        until_off_limts.append(moves_until_off_limits)
        square = square.right
    
    return until_off_limts
    

def check_down(square):
    """
    Moves the robot right if certain criteria is met.
    """
    count = 0
    while square.down != None:
        
        if square.down.off_limits == True:
            return count
        count += 1
        square = square.down
    
    return count
    

def check_path_right(square):
    """
    Checks the paths going one left and then search down until 
    """
    until_off_limts = []

    while square != None:

        moves_until_off_limits = check_right(square)
        until_off_limts.append(moves_until_off_limits)
        square = square.down
    
    return until_off_limts
    

def check_right(square):
    """
    Moves the robot right if certain criteria is met.
    """
    count = 0
    while square.right != None:
        
        if square.right.off_limits == True:
            return count
        count += 1
        square = square.right
    
    return count


def find_robot_path(grid):
    robot = grid[0][0]
    goal = grid[len(grid) - 1][len(grid[0]) - 1]
    row_length = len(grid) - 1
    col_length = len(grid[0]) - 1
    
    
    off_limits_right = None
    off_limits_down = None

    while robot != goal:
        row = 0
        col = 0
        col_max = 0
        row_max = 0

        if off_limits_down == None:
            off_limits_down = check_path_down(robot)
        if off_limits_right == None:
            off_limits_right = check_path_right(robot)

        # If the current row and end column are clear have the robot move all the way to the finish
        if off_limits_right[0] == col_length and off_limits_down[-1] == row_length:
            while robot.right != None:
                if robot.right.off_limits != True:
                    robot = robot.right

            while robot.down != None:
                if robot.down.off_limits != True:
                    robot = robot.down
            
            # IF this condition is met then the robot is at the goal
            break

        
        if col_length not in off_limits_down:
            col_max = max(off_limits_down)
            col = off_limits_down[col_max - 1]
        else:
            for indx, down in enumerate(off_limits_down):
                if down == col_length:
                    col = indx
                    break
        

        if row_length not in off_limits_right:
            row_max = max(off_limits_right)
            row = off_limits_right[row_max - 1]
        else:
            for indx, right in enumerate(off_limits_right):
                if right == row_length:
                    row = indx
                    break          


        
        if row not in off_limits_down:
            x = 0
            while x < row_length:
                if robot.right == None or robot.right.off_limits == True:
                    break
                robot = robot.right
                row_length -= 1
                off_limits_down = check_path_down(robot)
                row += 1

        elif robot.right != None:
            if robot.right.off_limits != True:
                robot = robot.right
                row_length -= 1
                off_limits_down = check_path_down(robot)


        if col not in off_limits_right:
            y = 0
            while y < col_length:
                if robot.down == None or robot.down.off_limits == True:
                    break
                robot = robot.down
                col_length -= 1
                off_limits_right = check_path_right(robot)
                y += 1

        elif robot.down != None:
            if robot.right.off_limits != True:
                robot = robot.down
                col_length -= 1
                off_limits_right = check_path_right(robot)


    print("Robot has reached the Goal!")


def example():

    robot_grid = Grid(10, 10, 12)
    grid = robot_grid.grid

    find_robot_path(grid)


if __name__ == "__main__":
    example()