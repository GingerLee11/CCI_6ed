# python3
# diving_board.py - Calculates the total different lengths possible for a diving board. Assuming that the board are lined end-to-end,
# and there must be exactly k planks of wood. There are two different lengths of wood: shorter and longer.

import unittest

def diving_board(k, shorter, longer):
    """
    Calculates the total different lengths possible for a diving board. Assuming that the board are lined end-to-end,
    and there must be exactly k planks of wood. There are two different lengths of wood: shorter and longer 
    (as the names apply shorter must be the shorter of the two planks).
    """
    if k == 0:
        return None
    all_lengths = []
    for i in range(k + 1):
        length = (k - i) * shorter + (k - (k - i)) * longer
        all_lengths.append(length)
    
    return all_lengths


def example():

    for x in range(1, 11):

        print(diving_board(x, 1, 2))


class Test(unittest.TestCase):

    tests = [
        (1, 5, 10, [5, 10]),
        (3, 5, 10, [15, 20, 25, 30]),
        (10, 1, 2, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        (0, 3, 5, None),
        (2, 2, 3, [4, 5, 6]),
    ]
    def test_diving_board(self):
        for k, s, l, expected in self.tests:
            actual = diving_board(k, s, l)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
