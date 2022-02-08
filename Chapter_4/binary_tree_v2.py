<<<<<<< HEAD
# python3
# binary_tree.py

from collections import deque

=======
>>>>>>> 62e7fe04f998b2f42a5741ffcd06b13dfdacd136
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("A root already exists")

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception("A node cannot have more than two children")
        return new

<<<<<<< HEAD
    def search(self, node):
        """
        Given a node's key returns that node
        """
        if self.root == None:
            raise Exception("Cannot search an empty tree.")
        
        if self.root.key == node:
            return self.root
        
        checked = set()

        # Create a queue to search through all the nodes in the binary tree 
        queue = deque()
        queue.append(self.root)

        while len(queue) != 0:
            curr_node = queue.popleft()

            if curr_node.key == node:
                return curr_node

            if curr_node.left == None:
                queue.append(curr_node.parent)
                checked.add(curr_node)
                continue
            if (curr_node.left is not None) and (curr_node.left not in checked):
                checked.add(curr_node)
                if curr_node.left.key == node:
                    return curr_node.left
                else:
                    queue.append(curr_node.left)
            if (curr_node.right is not None) and (curr_node.right not in checked):
                checked.add(curr_node)
                if curr_node.right.key == node:
                    return curr_node.right
                else:
                    queue.append(curr_node.right)

        return print(f"Node {node} does not exist in this binary tree.")
                

=======
>>>>>>> 62e7fe04f998b2f42a5741ffcd06b13dfdacd136

def example():
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n6 = t.insert(6, n3)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)
    t.insert(9, n4)
    t.insert(10, n5)
    t.insert(11, n5)
    t.insert(12, n6)
    t.insert(13, n6)
    t.insert(14, n7)
    t.insert(15, n7)
    t.insert(16, n8)
<<<<<<< HEAD
    t.search(1)
    t.search(16)
    t.search(15)
=======
>>>>>>> 62e7fe04f998b2f42a5741ffcd06b13dfdacd136

    print(t.root.right.right.key)
    print(t.root.left.left.left.key)
    print(t.root.left.left.right.key)
    print(t.root.right.right.right.key)
    print(t.root.left.left.left.left.key)
<<<<<<< HEAD
    print(t.root.right.parent.key)

if __name__ == "__main__":
    example()
=======
    


if __name__ == "__main__":
    example()
>>>>>>> 62e7fe04f998b2f42a5741ffcd06b13dfdacd136
