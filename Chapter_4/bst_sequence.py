# python3
# bst_sequence.py - Takes in a binary search tree
#  and returns all possible lists that could have generated that binary search tree
#  if nodes were inserted from left to right.

import unittest
from collections import deque

from binary_tree_v2 import BinaryTree

def bst_sequence(binary_search_tree):
    """
    Takes in a binary search tree
    and returns all possible lists that could have generated that binary search tree
    if nodes were inserted from left to right.
    """
    root_node = binary_search_tree.root

    if root_node == None:
        return None, None

    left_first_queue = deque()
    right_first_queue = deque()

    left_first_queue.append(root_node)
    right_first_queue.append(root_node)

    left_first_list, right_first_list = [], []

    # Use a Breadth first approach to add all the nodes level by level
    # Simulataneously append to a left first and right first orientation (by order of insertion in binary tree)
    while len(left_first_queue) != 0 or len(right_first_queue) != 0:

        node_left_first = left_first_queue.popleft()
        node_right_first = right_first_queue.popleft()

        left_first_list.append(node_left_first.key)
        right_first_list.append(node_right_first.key)

        if node_left_first.left != None:
            left_first_queue.append(node_left_first.left)
            left_first_queue.append(node_left_first.right)

        if node_right_first.right != None:
            right_first_queue.append(node_right_first.right)
            right_first_queue.append(node_right_first.left)

    return left_first_list, right_first_list


# TODO: Add a DFS implementation that goes all the way down a node on the left before moving right
# and vice-versa for right to left


class Test(unittest.TestCase):


    def _gen_binary_tree(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(8, None)
        n1 = tree.insert(4, root)
        n2 = tree.insert(12, root)
        n3 = tree.insert(2, n1)
        n4 = tree.insert(6, n1)
        n5 = tree.insert(10, n2)
        n6 = tree.insert(14, n2)
        tree.insert(1, n3)
        tree.insert(3, n3)
        tree.insert(5, n4)
        tree.insert(7, n4)
        tree.insert(9, n5)
        tree.insert(11, n5)
        tree.insert(13, n6)
        tree.insert(15, n6)
        return tree

    test = (
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 
            [8, 12, 4, 14, 10, 6, 2, 15, 13, 11, 9, 7, 5, 3, 1], 
        )
    

    def test_bst_sequence(self):
        expected_left, expected_right = self.test
        actual_left, actual_right = bst_sequence(self._gen_binary_tree())
        print(f"Expected for left: {expected_left} Expected for right: {expected_right}")
        print(f"Actual for left:   {actual_left} Actual for right:   {actual_right}")
        assert expected_left == actual_left
        assert expected_right == actual_right


if __name__ == "__main__":
    unittest.main()