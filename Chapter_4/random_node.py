# python3
# random_node.py - Binary Class method that returns a random node from the Binary Tree.

from random import randint

from binary_tree_v2 import BinaryTree


class BinaryTreeRandomNode(BinaryTree):
    """
    Binary tree with a get_random_node class method.
    """
    all_nodes = []

    def insert(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                self.all_nodes.append(new)
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
        self.all_nodes.append(new)
        return new

    def get_random_node(self):
        '''
        Binary Class method that returns a random node from the Binary Tree.
        '''
        random_index = randint(0, len(self.all_nodes) -1)
        random_node = self.all_nodes[random_index]
        return random_node.key


def example():
    t = BinaryTreeRandomNode()
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

    # Print 100 random nodes
    for x in range(1000):
        t.get_random_node()


# TODO: Write some tests to see if the method returns within a margin of error for several thousand iterations


if __name__ == "__main__":
    example()