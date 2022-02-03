# python3
# check_balanced.py - Checks whether a binary tree is balanced or not 
# Balanced here is defined to be a tree such that the heights of the two subtrees never differ by more than one.

import math
import unittest

def check_balanced(tree_list, n=0, no_children=None, level=1):
    """
    Checks whether a binary tree is balanced or not.
    Balanced here is defined to be a tree such that the heights of the two subtrees never differ by more than one.
    """
    if n == 0:
        left = n + 1
        right = n + 2
    elif n % 2 == 1:
        left = 2 * n + 1
        right = 2 * n + 3
    elif n % 2 == 0:
        left = 2 * n
        right = 2 * n + 2

    # Create no_children dict if none
    if no_children == None:
        no_children = dict()

    # Check if the node has children
    if (left > len(tree_list) and right > len(tree_list)) or (left == None and right == None):
        no_children[n] = level

    # Check if the number is a multiple of 2.
    # If so go up a level
    if n == 0 or n == 1:
        pass
    elif math.log2(n) == int(math.log2(n)):
        level += 1

    # Check for end condition only if there are elements in the dict
    if len(no_children) != 0:


        for node_level in no_children.values():
            if level - node_level > 1:
                return False

    # If the whole list is iterated through and the nodes are all within one level of difference, return True
    if n > len(tree_list):
        return True
    else:
        n += 1
        return check_balanced(tree_list, n, no_children, level)



class Test(unittest.TestCase):

    tree = [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]
    
    
    test = True

    def test_check_balanced(self):
        expected = self.test
        actual = check_balanced(self.tree)
        print(f"Actual:   {actual}\nExpected: {expected}\n")
        assert actual == expected


if __name__ == "__main__":
    unittest.main()