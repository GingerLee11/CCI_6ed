# python3
# sort_stack.py - A sorted stack whether the smallest items are at the top of the stack and the largest are at the bottom.

from random import randint

class Node:
    """
    Node class singly linked implementation.
    """
    def __init__(self, data):
        self.data = data 
        self.next = None 


class Stack:
    """
    Stack implementation using a singly linked list.
    """
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.size += 1

    def peek(self):
        if self.size == 0:
            raise Exception("Peeking from an empty stack.")
        return self.top.data

    def pop(self):
        if self.size == 0:
            raise Exception("Popping from an an empty Stack.")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item


class SortStack:
    """
    A sorted stack whether the smallest item is at the top of the stack and the largest is at the bottom.
    """
    def __init__(self):
        self.temp_stack = Stack()
        self.sorted_stack = Stack()

    def push(self, item):
        # If the sorted stack is empty then there is no reason to check
        # Because the single item will be the biggest and the smallest item.
        if self.sorted_stack.is_empty() == True:
            self.sorted_stack.push(item)
        else:
            # This isn't very elegant, but it will serve as a temp holding space as items are moved.
            node = Node(item)
            
            # Pop of items until the next item is bigger than the current item being pushed in
            while node.data > self.sorted_stack.peek():
                self.temp_stack.push(self.sorted_stack.pop())
                if self.sorted_stack.is_empty() == True:
                    break
            self.sorted_stack.push(item)

            # Push the stack "back on top" of the new item
            while self.temp_stack.is_empty() == False:
                self.sorted_stack.push(self.temp_stack.pop())

    def is_empty(self):
        return self.sorted_stack.is_empty()

    def peek(self):
        return self.sorted_stack.peek()

    
    def pop(self):
        return self.sorted_stack.pop()

"""
stack_items = SortStack()

for i in range(100):
    stack_items.push(randint(1, 100))

while stack_items.is_empty() == False:
    print(stack_items.pop())

"""