# python3
# queue_via_stacks.py - Queue implementation that uses two stacks to achieve queue functionality.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class Stack:
    """
    Basic Stack implementation.
    """
    def __init__(self):
        self.size = 0
        self.top = None

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.size == 0:
            raise Exception("Peeking at an empty stack.")
        return self.top.data

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Popping off of an empty stack.")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1 
        return item

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + " -> "
            cur = cur.next
        return out[:-3]

    
class MyQueue:
    """
    Queue implementation that uses two stacks to achieve queue functionality.
    One stack is used as a "push_stack" to add new items, 
    and another is used as "pop_stack" to remove items. 
    """

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def is_empty(self):
        # Check to make sure that both stacks are empty
        if (self.push_stack.is_empty()) and (self.pop_stack.is_empty()):
            return True
        return False

    def add(self, item):
        """
        Add item goes into push_stack,
        but pop_stack has to be empty first so that the new item can be on the top. 
        """
        if self.push_stack.is_empty():
            if self.pop_stack.is_empty():
                self.push_stack.push(item)
            else:
                while self.pop_stack.is_empty() == False:
                    self.push_stack.push(self.pop_stack.pop())
                self.push_stack.push(item)
        else:
            self.push_stack.push(item)

    def peek(self):
        """
        Item is peeked at from the top of pop_stack,
        but push_stack has to be empty first to be sure that the item peeked is the first inputted.
        """
        if self.pop_stack.is_empty():
            if self.push_stack.is_empty():
                raise Exception("Peeking at an empty Queue.")
            else: 
                while self.push_stack.is_empty() == False:
                    self.pop_stack.push(self.push_stack.pop())
                return self.pop_stack.peek()
        else:
            return self.pop_stack.peek()

    def remove(self):
        """
        Item is removed from the top of pop_stack,
        but push_stack has to be empty first so that the first-in can be first-out.
        """
        if self.pop_stack.is_empty():
            if self.push_stack.is_empty():
                raise Exception("Can't remove from an empty Queue.")
            else: 
                while self.push_stack.is_empty() == False:
                    self.pop_stack.push(self.push_stack.pop())
                return self.pop_stack.pop()
        else:
            return self.pop_stack.pop()
    
