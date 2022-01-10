# python3
# delete_middle_node.py - Given a node, delete that node from somewhere in the middle of the linked list.

from collections import deque

def delete_middle_node(llist, node):
    """
    Given a node, delete that node from somewhere in the middle of the linked list.
    """

    llist.remove(node)

    return llist


letters = deque('abcdefghij')

# delete_middle_node(delete_middle_node(letters, 'e'), 'i')