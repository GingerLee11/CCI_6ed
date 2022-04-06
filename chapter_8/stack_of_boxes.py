# python3
# stack_of_boxes.py - Find the tallest height possible for a stack of boxes given a number "n" of boxes.


import unittest


def stack_of_boxes(n, height_diff_btwn_boxes=1):
    """
    Find the tallest height possible for a stack of boxes given a number "n" of boxes.

    If the height of the boxes are only positive integers then height_diff_btwn_boxes=1.
    The smaller the possible difference between the boxes the larger the possible high of the box tower.
    """
    
    difference_from_first_to_last = n * height_diff_btwn_boxes
    last_box = n - difference_from_first_to_last

    if height_diff_btwn_boxes == 1:
        total_height = n * (n + 1) / 2
    else:
        total_height = n * (n + last_box) / 2

    
    return total_height


class TestSuite(unittest.TestCase):

    tests = [
        (100, 1, 5050.0),
        (100, 0.5, 7500),
        (100, 0.0125, 9937.5),
        (100, 9.99e-99, 10000),
        (10000, 1, 50005000.0),
        (100000000000000, 1, 5.00000000000005e+27),
        (1, 1, 1),
        (0, 1, 0),
        (2, 1, 3),
        (3, 1, 6),
        (4, 1, 10),
        (5, 1, 15),
    ]
    
    def test_stack_of_boxes(self):
        for n, height_diff, expected in self.tests:
            actual = stack_of_boxes(n, height_diff)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()


def example():

    print(stack_of_boxes(100))
    print(stack_of_boxes(100, 0.5))
    print(stack_of_boxes(100, 0.0125))
    print(stack_of_boxes(100, 9.99e-99))

