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

    tree = [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]

    test = [
        deque([8]),
        deque([7, 9]),
        deque([6, 10, 5, 11]),
        deque([4, 12, 3, 13, 2, 14, 1, 15]),
    ]

    def test_list_of_depths(self):
        expected = self.test
        actual = list_of_depths(self.tree)
        print(f"Actual:  {actual}\nExpected:{expected}\n")
        assert actual == expected

if __name__ == "__main__":
    unittest.main()