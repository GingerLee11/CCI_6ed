# python3
# list_of_depths.py - Creates a linked list at each depth of the given binary tree.

from collections import deque 
from math import log2, ceil

import unittest

def list_of_depths(binary_tree):
    """
    Creates a linked list at each depth of the given binary tree.
    """
    # Calculate the depth "d", which represents how many levels there are in the tree and the num of linked lists
    D = ceil(log2(len(binary_tree)))
    list_of_linked_lists = []
    tree_linked_list = deque(binary_tree)

    for i in range(D):
        linked_list = deque()
        num_nodes = 2 ** i

        # Append nodes until the max for each level (1, 2, 4, 8, 16, 32...)
        while len(linked_list) < num_nodes:
            linked_list.append(tree_linked_list.popleft())
        
        list_of_linked_lists.append(linked_list)

    return list_of_linked_lists


class Test(unittest.TestCase):

    trees = [
        [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15],
        [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 16],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [0, 1, 2, None, 4, None, 6, None, 8, None, 10, None, 12, None, 14], # Represents a full, but not complete binary tree
    ]

    tests = [
        [
        deque([8]),
        deque([7, 9]),
        deque([6, 10, 5, 11]),
        deque([4, 12, 3, 13, 2, 14, 1, 15]),
        ],
        [
        deque([8]),
        deque([7, 9]),
        deque([6, 10, 5, 11]),
        deque([4, 12, 3, 13, 2, 14, 1, 15]),
        deque([8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 16]),
        ],
        [
        deque([0]),
        deque([1, 2]),
        deque([3, 4, 5, 6]),
        deque([7, 8, 9, 10, 11, 12, 13, 14]),
        ],
        [
        deque([0]),
        deque([1, 2]),
        deque([None, 4, None, 6]),
        deque([None, 8, None, 10, None, 12, None, 14]),
        ],
    ]

    def test_list_of_depths(self):
        for expected, tree in zip(self.tests, self.trees):
            actual = list_of_depths(tree)
            print(f"Actual:  {actual}\nExpected:{expected}\n")
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
