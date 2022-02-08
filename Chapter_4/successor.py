# python3
# successor.py - Finds the next node in the succession (In order succession) using a binary search tree (BTS).

from binary_tree import BinaryTree

def successor(node):
    """
    Finds the next node in the succession (In order succession) using a binary search tree (BTS).
    Assumes that the given node is part of the succession, and the next node is the node that follows (not the beginning of the succession).
    """

    # node = binary_search_tree.search(node)
    # Left:
    # Edge case for if the node is in the left-most corner
    if node.left == None and node.parent.key > node.key:
        next = node.parent
        return next.key

    # Parent:
    # Edge case for root node
    if node.parent == None:
        next = node.right
        return next.key

    # Edge case for right-most corner
    if node.right == None and node.parent.key < node.key:
        next = node.parent.left
        return next.key
     
    
    # Case for multi-level trees:
    # Parent
    # Does not "move" up a level instead goes to right child
    if node.left.key < node.parent.key:
        next = node.right
    # Right
    elif node.right.key > node.parent.key:
        next = node.parent.left
        # return next.key

    return next.key



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
    return tree

def _search_BST(node):
    tree = _gen_BST_1()
    found = tree.search(node)
    return found

tests = [
    (_search_BST(4), 6),
    (_search_BST(8), 12),
    (_search_BST(12), 4),
    (_search_BST(1), 2),
    (_search_BST(2), 3),
    (_search_BST(3), 1),
    (_search_BST(14), 10),
    (_search_BST(10), 11),
]



def test_successor():
    for given_node, expected in tests:
        actual = successor(given_node)
        print(f"Actual:   {actual}\nExpected: {expected}")
        error_msg = f"{successor.__name__} failed on {given_node.key}"
        assert actual == expected, error_msg

if __name__ == '__main__':
    test_successor()