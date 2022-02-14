# python3
# check_subtree.py - Checks if T2 is a subtree of T1. Both trees are binary trees.

from collections import deque
import unittest

from binary_tree_v2 import BinaryTree


def check_subtree(T1, T2):
    """
    Checks if T2 is a subtree of T1. Both trees are binary trees.
    """
    if T2.root == None:
        return False
    '''
    if T1.root == T2.root:
        return False
    '''
    T1_queue_left, T1_queue_right = deque(), deque()
    T2_queue = deque()

    T1_queue_left.append(T1.root.left)
    T1_queue_right.append(T1.root.right)

    T2_queue.append(T2.root)

    T1_left, T1_right, T2_checked = [], [], []

    while len(T2_queue) != 0:
        if len(T1_queue_left) != 0:
            T1_sub_left = T1_queue_left.popleft()
        if len(T1_queue_right) != 0:
            T1_sub_right = T1_queue_right.popleft()

        T2_node = T2_queue.popleft()

        # Check if the node in the left sub-tree of T1 equals the root of T2
        if T1_sub_left.key == T2_node.key:
            T1_left.append(T1_sub_left.key)

            if T2_node.key not in T2_checked:
                T2_checked.append(T2_node.key)

            if T2_node.left != None:
                if T1_sub_left.left.key == T2_node.left.key:
                    T1_queue_left.append(T1_sub_left.left)
                    T2_queue.append(T2_node.left)
                else:
                    if T2_node.left.key not in T2_checked:
                        T2_checked.append(T2_node.left.key)

            if T2_node.right != None:
                if T1_sub_left.right.key == T2_node.right.key:
                    T1_queue_left.append(T1_sub_left.right)
                    T2_queue.append(T2_node.right)
                else:
                    if T2_node.right.key not in T2_checked:
                        T2_checked.append(T2_node.right.key)

            

        elif T1_sub_right.key == T2_node.key:
            T1_right.append(T1_sub_right.key)

            if T2_node.key not in T2_checked:
                T2_checked.append(T2_node.key)

            if T2_node.left != None:
                if T1_sub_right.left.key == T2_node.left.key:
                    T1_queue_right.append(T1_sub_right.left)
                    
                    T1_right.append(T1_sub_right.left.key)
                    T2_checked.append(T2_node.left.key)
                    
                else:
                    if T2_node.left.key not in T2_checked:
                        T2_checked.append(T2_node.left.key)

            if T2_node.right != None:
                if T1_sub_right.right.key == T2_node.right.key:
                    T1_queue_right.append(T1_sub_right.right)
                    T2_queue.append(T2_node.right)
                else:
                    if T2_node.right.key not in T2_checked:
                        T2_checked.append(T2_node.right.key)

            

        # If neither node in either subtree matches append the same node for T2 and move down the other trees
        elif T1_sub_left.key != T2_node.key and T1_sub_right.key != T2_node.key:
            T2_queue.append(T2_node)
            T1_queue_left.append(T1_sub_left.left)
            T1_queue_left.append(T1_sub_left.right)
            T1_queue_right.append(T1_sub_right.left)
            T1_queue_right.append(T1_sub_right.right)

        if (T1_sub_left.left == None and T1_sub_left.right == None) and (T1_sub_right.left == None and T1_sub_right.right == None):
            break

    # If none of the nodes match return False
    if T2_checked == []:
        return False
    elif T1_left == T2_checked or T1_right == T2_checked:
        return True
    else:
        return False



class Test(unittest.TestCase):


    def _T1(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(1, None)
        n2 = tree.insert(2, root)
        n3 = tree.insert(3, root)
        n4 = tree.insert(4, n2)
        n5 = tree.insert(5, n2)
        n6 = tree.insert(6, n3)
        n7 = tree.insert(7, n3)
        n8 = tree.insert(8, n4)
        tree.insert(9, n4)
        tree.insert(10, n5)
        tree.insert(11, n5)
        tree.insert(12, n6)
        tree.insert(13, n6)
        tree.insert(14, n7)
        tree.insert(15, n7)
        tree.insert(16, n8)
        tree.insert(17, n8)
        return tree

    def _T2_v1_sub_left(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(2, None)
        n2 = tree.insert(4, root)
        n3 = tree.insert(5, root)
        tree.insert(8, n2)
        tree.insert(9, n2)
        tree.insert(10, n3)
        tree.insert(11, n3)
        return tree

    def _T2_v1_sub_right(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(3, None)
        n2 = tree.insert(6, root)
        n3 = tree.insert(7, root)
        tree.insert(12, n2)
        tree.insert(13, n2)
        tree.insert(14, n3)
        tree.insert(15, n3)
        return tree

    def _T2_v1_not_sub_left(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(2, None)
        n2 = tree.insert(4, root)
        n3 = tree.insert(5, root)
        tree.insert(8, n2)
        tree.insert(9, n2)
        tree.insert(10, n3)
        tree.insert(42, n3)
        return tree
    
    def _T2_v1_not_sub_right(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(5, None)
        n2 = tree.insert(6, root)
        n3 = tree.insert(7, root)
        tree.insert(12, n2)
        tree.insert(13, n2)
        tree.insert(14, n3)
        tree.insert(15, n3)
        return tree

    def _T2_copy_of_T1(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(1, None)
        n2 = tree.insert(2, root)
        n3 = tree.insert(3, root)
        n4 = tree.insert(4, n2)
        n5 = tree.insert(5, n2)
        n6 = tree.insert(6, n3)
        n7 = tree.insert(7, n3)
        n8 = tree.insert(8, n4)
        tree.insert(9, n4)
        tree.insert(10, n5)
        tree.insert(11, n5)
        tree.insert(12, n6)
        tree.insert(13, n6)
        tree.insert(14, n7)
        tree.insert(15, n7)
        tree.insert(16, n8)
        tree.insert(17, n8)
        return tree

    def _T2_v1_sub_left_small_v1(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(8, None)
        tree.insert(16, root)
        tree.insert(17, root)
        return tree

    def _T2_v1_sub_right_small_v1(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(7, None)
        tree.insert(14, root)
        tree.insert(15, root)
        return tree

    def _T2_v1_sub_left_v2(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(4, None)
        n2 = tree.insert(8, root)
        n3 = tree.insert(9, root)
        tree.insert(16, n2)
        tree.insert(17, n2)
        return tree

    def _T2_v1_sub_left_v3(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(4, None)
        n2 = tree.insert(8, root)
        tree.insert(9, root)
        tree.insert(16, n2)
        return tree

    def _T2_v1_sub_right_v2(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(3, None)
        n2 = tree.insert(6, root)
        tree.insert(12, n2)
        tree.insert(13, n2)
        return tree

    def _T2_v1_not_sub_right_v2(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(3, None)
        n2 = tree.insert(6, root)
        n3 = tree.insert(7, root)
        n4 = tree.insert(12, n2)
        tree.insert(13, n2)
        tree.insert(14, n3)
        tree.insert(15, n3)
        tree.insert(24, n4)
        return tree

    def _T2_v1_not_sub_right_v3(self):
        self.tree = BinaryTree()
        tree = self.tree
        root = tree.insert(3, None)
        n2 = tree.insert(6, root)
        n3 = tree.insert(7, root)
        tree.insert(12, n2)
        tree.insert(13, n2)
        tree.insert(14, n3)
        n7 = tree.insert(15, n3)
        tree.insert(31, n7)
        return tree

    tests = [
            (_T1, _T2_v1_sub_left, True),
            (_T1, _T2_v1_sub_right, True),
            (_T1, _T2_v1_not_sub_left, False),
            (_T1, _T2_v1_not_sub_right, False),
            (_T1, _T2_copy_of_T1, False),
            (_T1, _T2_v1_sub_left_small_v1, True),
            (_T1, _T2_v1_sub_right_small_v1, True),
            (_T1, _T2_v1_sub_left_v2, True),
            (_T1, _T2_v1_sub_left_v3, True),
            (_T1, _T2_v1_sub_right_v2, True),
            (_T1, _T2_v1_not_sub_right_v2, False),
            (_T1, _T2_v1_not_sub_right_v3, False),
    ]
    

    def test_check_subtree(self):
        for T1_gen, T2_gen, expected in self.tests:
            error_msg = f"{check_subtree.__name__} failed on {T2_gen.__name__}."
            actual = check_subtree(T1_gen(self), T2_gen(self))
            print(f"Expected: {expected}\nActual:   {actual}")
            assert actual == expected, error_msg
            

if __name__ == "__main__":
    unittest.main()
