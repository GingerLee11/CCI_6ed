# python3
# stack_implementation.py - Geeks for Geeks Linked list stack implementation
# https://www.geeksforgeeks.org/stack-in-python/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# GeeksforGeeks implementation: 
class Stack:
    """
    Linked List Stack Implementation.
    """
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack 
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + " -> "
            cur = cur.next
        return out[:-3]

    # Get current size of the stack
    def get_size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Check to see if stack is empty
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.data

    # Push a value into the stack
    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack and return
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data


# Driver code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1,11):
        stack.push(i)
    print(f"Stack: {stack}")

    for j in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
