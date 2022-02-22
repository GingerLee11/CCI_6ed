# python3
# draw_line.py - Draws a horizontal "line" on a monochrome screen by turning the zeros into ones. 
# The width of the screen must be divisible by 8, and y must be less than the height of the screen.

import unittest

def draw_line(screen, width, x1, x2, y):
    """
    Draws a horizontal "line" on a monochrome screen by turning the zeros into ones. 
    The width of the screen must be divisible by 8, and y must be less than the height of the screen.
    """
    if width % 8 != 0:
        return print("Width must be divisible by 8.")

    if x1 > x2 or x2 > width:
        return print("x2 must be greater than x1 and x2 must be smaller than the width of the screen.")

    height = int(len(screen) / width)

    if y > height or y == 0:
        return print("y must be smaller than screen height and non-zero.")

    start = width * (y -1) + x1
    end = width * (y -1) + x2

    while start != end:
        screen[start] = 1
        start += 1

    return screen



class Test(unittest.TestCase):

    def gen_screen(num_pixels):
        """
        Generates screen for testing. 
        The num_pixels must be divisible by 8.
        """
        if num_pixels % 8 != 0:
            return False
        else:
            screen = [0 for x in range(num_pixels)]

        return screen

    tests = [
        (gen_screen(64), 8, 1, 7, 4, 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
        (gen_screen(64), 16, 2, 14, 2, 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
        (gen_screen(64), 32, 3, 28, 1,
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
        (gen_screen(64), 12, 3, 5, 2, None),
        (gen_screen(800), 64, 15, 5, 3, None),
        (gen_screen(128), 16, 1, 22, 3, None),
        (gen_screen(64), 32, 1, 22, 3, None),
        (gen_screen(64), 32, 1, 22, 0, None),
        (gen_screen(64), 0, 1, 5, 1, None),
    ]

    def test_draw_line(self):
        for screen, width, x1, x2, y, expected in self.tests:
            actual = draw_line(screen, width, x1, x2, y)
            print(f"Actual:   {actual}\nExpected: {expected}")
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
