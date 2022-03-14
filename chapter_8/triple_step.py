# python3
# triple_step.py - Counts all the possible path a child could take up a flight of stairs with n steps going 1, 2, 3 steps at a time.

import unittest
import time

def triple_steps(n):
    """
    Counts all the possible path a child could take up a flight of stairs with n steps going 1, 2, 3 steps at a time.
    """
    a = 1
    b = 2
    c = 4
    if n == 0:
        return 0
    if n == 3:
        return c
    elif n == 2:    
        return b
    elif n == 1:    
        return a
    else:
        i = 3
        while i < n:
            new = c + b + a
            a = b
            b = c
            c = new
            i += 1

    return c

"""
big0_test = [10, 100, 1000, 10000, 100000, 1000000]
differences = []
for n in big0_test:
    start = time.time()
    triple_steps(n)
    end = time.time()
    difference = end - start
    differences.append(difference)
    print(f"{difference} seconds")
print(differences)
"""

class Test(unittest.TestCase):


    tests = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
        (6, 24),
        (7, 44),
        (8, 81),
        (9, 149),
        (10, 274),
        (11, 504),
    ]

    def test_triple_steps(self):
        for n, expected in self.tests:
            actual = triple_steps(n)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
