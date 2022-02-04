# python3
# minimal_tree.py - Takes a sorted set-like list, and creates a binary search tree with minimal height

import unittest

from math import ceil

def minimal_tree(sorted_set, start, end, min_tree=None):
    """
    Takes a sorted set-like list, and creates a binary search tree with minimal height
    """
    if len(sorted_set) == 0:
        return []
    
    # Create minimal tree list if none
    if min_tree == None:
        min_tree = []

    if start > end:
        return None

    mid = ceil((start + end) / 2) 

    min_tree.append(sorted_set[mid])

    left = minimal_tree(sorted_set, start, mid - 1, min_tree)
    right = minimal_tree(sorted_set, mid + 1, end, min_tree)

    return min_tree


class Test(unittest.TestCase):

    sorted_lists = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 40, 85, 128, 365, 444, 987],
        [],
        
    ]
    tests = [
        [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15],
        [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13],
        [7, 4, 2, 1, 3, 6, 5, 11, 9, 8, 10, 13, 12],
        [],
    ]

    def test_minimal_tree(self):
        for expected, sorted_list in zip(self.tests, self.sorted_lists):
            actual = minimal_tree(sorted_list, 0, len(sorted_list) - 1)
            print(f"Actual:  {actual}\nExpected:{expected}\n")
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
