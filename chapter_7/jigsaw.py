# python3
# jigsaw.py - Creates an N x N jigsaw puzzle with methods to solve it.


import unittest


class Piece:
    """
    Jigsaw puzzle piece subclass.
    """
    def __init__(self, grid_number):
        self.top = None
        self.right = None
        self.left = None
        self.bottom = None
        self.grid_number = grid_number


class Jigsaw:
    """
    Creates an N x N jigsaw puzzle with methods to solve it.
    """
    def __init__(self, N):
        self.N = N
        self.grid = self._create_grid(N)
        self.solved_puzzle = self._create_puzzle(self.grid)

    
    def _create_grid(self, N):
        """
        Creates a grid containing all the pieces without any relationships.
        """
        
        grid = []
        for y in range(N):
            row = []
            y *= N
            for x in range(N):
                piece = Piece(x + y)
                row.append(piece)
            grid.append(row)
            

        return grid

    def _create_puzzle(self, grid):
        """
        Creates the solved puzzle using the grid with the pieces.
        """
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                piece = grid[y][x]

                # This is for the (unrealistic) situation where there would only be one piece in the puzzle
                if y == 0 and y == len(grid) - 1:
                    break

                if y == 0:
                    piece.bottom = grid[y + 1][x]
                    if x == 0:
                        piece.right = grid[y][x + 1]
                    elif x == len(grid[0]) -1:
                        piece.left = grid[y][x - 1]
                    else:
                        piece.left = grid[y][x - 1]
                        piece.right = grid[y][x + 1]
                elif y == len(grid) -1:
                    piece.top = grid[y - 1][x]
                    if x == 0:
                        piece.right = grid[y][x + 1]
                    elif x == len(grid[0]) -1:
                        piece.left = grid[y][x - 1]
                    else:
                        piece.left = grid[y][x - 1]
                        piece.right = grid[y][x + 1]
                elif x == 0:
                    piece.top = grid[y - 1][x]
                    piece.right = grid[y][x + 1]
                    piece.bottom = grid[y + 1][x]
                elif x == len(grid[0]) -1:
                    piece.top = grid[y - 1][x]
                    piece.left = grid[y][x - 1]
                    piece.bottom = grid[y + 1][x]
                else:
                    piece.top = grid[y - 1][x]
                    piece.right = grid[y][x + 1]
                    piece.bottom = grid[y + 1][x]
                    piece.left = grid[y][x - 1]
                    
        return grid

    

class Test(unittest.TestCase):

    test_puzzle_dimensions = [1, 2, 3]

    expected_relationships = [
        (
            1, 
            [[None]],  # Top
            [[None]],  # Right
            [[None]],  # Bottom
            [[None]],  # Right
        ),
        (
            2, # puzzle size
            [
                [None, None],
                [0, 1],
            ], # Top
            [
                [1, None],
                [3, None],
            ], # Right
            [
                [2, 3],
                [None, None],
            ], # Bottom
            [
                [None, 0],
                [None, 2],
            ], # Right
        ),
        (
            3, # Puzzle size
            [
                [None, None, None],
                [0, 1, 2],
                [3, 4, 5],
            ], # Top
            [
                [1, 2, None],
                [4, 5, None],
                [7, 8, None],
                
            ], # Right
            [
                [3, 4, 5],
                [6, 7, 8,],
                [None, None, None],
            ], # Bottom
            [
                [None, 0, 1],
                [None, 3, 4],
                [None, 6, 7],
            ], # Right
        ),
    ]


    def test_created_puzzle(self):
        
        for N, expected_top, expected_right, expected_bottom, expected_left in self.expected_relationships:
            actual_top, actual_right, actual_bottom, actual_left = [], [], [], []
            
            jigsaw = Jigsaw(N)
            actual_jigsaw = jigsaw.solved_puzzle
            for y in range(len(actual_jigsaw)):
                row_top, row_right, row_bottom, row_left = [], [], [], []
                for x in range(len(actual_jigsaw[0])):
                    piece = actual_jigsaw[y][x]

                    if piece.top != None:    
                        row_top.append(piece.top.grid_number)
                    else:
                        row_top.append(None)
                    if piece.right != None:    
                        row_right.append(piece.right.grid_number)
                    else:
                        row_right.append(None)
                    if piece.bottom != None:    
                        row_bottom.append(piece.bottom.grid_number)
                    else:
                        row_bottom.append(None)
                    if piece.left != None:    
                        row_left.append(piece.left.grid_number)
                    else:
                        row_left.append(None)
                actual_top.append(row_top)
                actual_right.append(row_right)
                actual_bottom.append(row_bottom)
                actual_left.append(row_left)
                print(f"Puzzle size: N={N}")
                print(f'Expected top: {expected_top[y]}\n  Actual top: {row_top}')
                print(f'Expected right: {expected_right[y]}\n  Actual right: {row_right}')
                print(f'Expected bottom: {expected_bottom[y]}\n  Actual bottom: {row_bottom}')
                print(f'Expected left: {expected_left[y]}\n  Actual left: {row_left}')
            
            assert expected_top == actual_top
            assert expected_right == actual_right
            assert expected_bottom == actual_bottom
            assert expected_left == actual_left





if __name__ == "__main__":
    unittest.main()