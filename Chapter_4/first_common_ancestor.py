# python3
# first_common_ancestor.py - Finds the first common ancestor of two nodes in a binary tree.

import unittest

from binary_tree_v2 import BinaryTree

from collections import deque

class AncestorNode:
    def __init__(self, key):
        self.key = key
        self.level = 0
        self.parent = None
        self.left = None
        self.right = None


class BinaryTreeCommonAncestor(BinaryTree):
    NodeCls = AncestorNode

    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("A root already exists")
        if parent is not None:
            new.level = parent.level + 1
            if not parent.left:
                parent.left = new
                new.parent = parent
            elif not parent.right:
                parent.right = new
                new.parent = parent
            else:
                raise Exception("A node cannot have more than two children")
            return new


def first_common_ancestor(node1, node2):
    """
    Finds the first common ancestor of two nodes in a binary tree.
    """
    # Check first to see if the nodes are the same.
    if node1 == node2:
        return node1.key, node1.level
    
    if node2.level > node1.level:
        node = node2
        node2 = node1
        node1 = node

    # "Move up" node1 until it is at the same level as node 2
    while node1.level > node2.level:
        node1 = node1.parent

    # Once the levels are equal move the two nodes up until they are equal
    while node1 != node2:
        node1 = node1.parent 
        node2 = node2.parent

    return node1.key, node1.level



def _search_example_tree(node1, node2):
    t = BinaryTreeCommonAncestor()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n6 = t.insert(6, n3)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)
    n9 = t.insert(9, n4)
    n10 = t.insert(10, n5)
    n11 = t.insert(11, n5)
    n12 = t.insert(12, n6)
    n13 = t.insert(13, n6)
    n14 = t.insert(14, n7)
    n15 = t.insert(15, n7)
    t.insert(16, n8)
    t.insert(17, n8)
    t.insert(18, n9)
    t.insert(19, n9)
    t.insert(20, n10)
    t.insert(21, n10)
    t.insert(22, n11)
    t.insert(23, n11)
    t.insert(24, n12)
    t.insert(25, n12)
    t.insert(26, n13)
    t.insert(27, n13)
    t.insert(28, n14)
    t.insert(29, n14)
    t.insert(30, n15)
    t.insert(31, n15)
    n1 = t.search(node1)
    n2 = t.search(node2)
    return n1, n2


tests = [
    (_search_example_tree(31, 16), 1, 0),
    (_search_example_tree(16, 17), 8, 3),
    (_search_example_tree(19, 20), 2, 1),
    (_search_example_tree(17, 18), 4, 2),
    (_search_example_tree(30, 25), 3, 1),
    (_search_example_tree(22, 22), 22, 4),
    (_search_example_tree(16, 5), 2, 1),
    (_search_example_tree(2, 24), 1, 0),
    (_search_example_tree(23, 3), 1, 0),
]

def test_first_common_ancestor():
    for nodes, expected_common_ancestor, expected_ancestor_level in tests:
        actual_common_ancestor, actual_ancestor_level = first_common_ancestor(nodes[0], nodes[1])
        print(f"Expected: Common Ancestor: {expected_common_ancestor}, at level {expected_ancestor_level}")
        print(f"Actual:   Common Ancestor: {actual_common_ancestor}, at level {actual_ancestor_level}")
        assert actual_common_ancestor == expected_common_ancestor
        assert actual_ancestor_level == expected_ancestor_level

if __name__ == "__main__":
    test_first_common_ancestor()