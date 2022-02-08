#!
# python3
# validate_bst.py - Validates that the given tree is a Binary Search Tree


import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


import unittest

from binary_tree import BinaryTree

def validate_bst_v1(node, checked=None):
    """
    Validates that the given tree is a Binary Search Tree.
    """
    if checked == None:
        checked = set()
    
    # Check if the node on the left is None (which means the right node is None too)
    # Then if the two child nodes are also in checked move up to the parent node
    if (node.left is None) or (node.left in checked and node.right in checked):
        if node.parent == None:
            return True

        checked.add(node)
        return validate_bst_v1(node.parent, checked)   
        

    if node.left.data > node.data or node.right.data <= node.data:
        return False

    if (node.left is not None) and (node.left not in checked):
        checked.add(node)
        return validate_bst_v1(node.left, checked)

    if (node.right is not None) and (node.right not in checked):
        checked.add(node)
        return validate_bst_v1(node.right, checked) 

     



def _gen_BST_1():
    tree = BinaryTree()
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
    return root

def _gen_not_BST_1():
    tree = BinaryTree()
    root = tree.insert(8, None)
    n1 = tree.insert(7, root)
    n2 = tree.insert(9, root)
    n3 = tree.insert(6, n1)
    n4 = tree.insert(5, n1)
    n5 = tree.insert(10, n2)
    n6 = tree.insert(11, n2)
    tree.insert(4, n3)
    tree.insert(3, n3)
    tree.insert(2, n4)
    tree.insert(1, n4)
    tree.insert(12, n5)
    tree.insert(13, n5)
    tree.insert(14, n6)
    tree.insert(15, n6)
    return root

def _gen_not_BST_2():
    tree = BinaryTree()
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
    tree.insert(15, n6) # Left element is greater than parent
    tree.insert(16, n6)
    return root

test_cases = [
    (_gen_BST_1, True),
    # (_gen_balanced_2, True),
    (_gen_not_BST_1, False),
    (_gen_not_BST_2, False),
]

testable_functions = [validate_bst_v1]

def test_validate_bst():
    for tree_gen, expected in test_cases:
        for validate_bst in testable_functions:
            error_msg = f"{validate_bst.__name__} failed on {tree_gen.__name__}"
            actual = validate_bst(tree_gen())
            print(f"Actual:   {actual}\nExpected: {expected}")
            assert actual == expected, error_msg



test_validate_bst()