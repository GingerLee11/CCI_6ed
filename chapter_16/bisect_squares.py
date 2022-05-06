# python3
# bisect_squares.py - Finds a line that will bisect two squares on a two-dimensional plane.
# The square data structure is as follows: 
# square = [(top left), (top right), (bottom left), (bottom right)]
# square = [(2, 8), (4, 8), (2, 6),  (4, 6)] for a square will side length of 2 starting at (2, 8).

import unittest

def find_center_of_square(square):
    """
    Helper function that finds the center of a square.
    The square data structure is as follows: 
    square = [(top left), (top right), (bottom left), (bottom right)]
    square = [(2, 8), (4, 8), (2, 6),  (4, 6)] for a square will side length of 2 starting at (2, 8).
    """
    # Assuming that the first elem of square is top left
    side_length = square[1][0] - square[0][0]
    horz_pos = square[0][0] + side_length / 2
    vert_pos = square[0][1] - side_length / 2
    center_pos = (horz_pos, vert_pos)
    return center_pos

def bisect_squares(square1, square2):
    """
    Finds a line that will bisect two squares on a two-dimensional plane.
    The square data structure is as follows: 
    square = [(top left), (top right), (bottom left), (bottom right)]
    square = [(2, 8), (4, 8), (2, 6),  (4, 6)] for a square will side length of 2 starting at (2, 8).
    """
    center_1 = find_center_of_square(square1)
    center_2 = find_center_of_square(square2)
    
    bisect_line = [center_1, center_2]
    return bisect_line


class Test(unittest.TestCase):

    test_squares = [
        [((2, 8), 2), ((8, 3), 2), [(3, 7), (9, 2)]],
    ]
    
    def generate_square(self, test_square):
        square = []
        starting_point = test_square[0]
        side_length = test_square[1]
        point_2 = (starting_point[0] + side_length, starting_point[1])
        point_3 = (starting_point[0], starting_point[1] - side_length)
        point_4 = (starting_point[0] + side_length, starting_point[1] - side_length)
        square.append(starting_point)
        square.append(point_2)
        square.append(point_3)
        square.append(point_4)
        
        return square

    def test_bisect_squares(self):
        for square1, square2, expected in self.test_squares:
            square_1 = self.generate_square(square1)
            square_2 = self.generate_square(square2)
            actual = bisect_squares(square_1, square_2)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
