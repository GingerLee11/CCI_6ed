# python3
# set_of_stacks.py - Stack implementation that creates a new stack when a certain threshold is reached for the current stack.

# Use double linked list in order to maintain connections between the stacks


import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.above = None
        self.below = None

    def __repr__(self):
        return self.data


class Stack:
    """
    Stack implementation that mimics a stack of dishes.
    Threshold determines how many dishes can be in the stack.

    """
    def __init__(self, threshold):
        self.size = 0 
        self.threshold = threshold
        self.top = None
        self.bottom = None

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + " -> "
            cur = cur.next
        return out[:-3]

    def is_full(self):
        return self.size == self.threshold

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, data):
        if self.size >= self.threshold:
            return False
        self.size += 1
        
        node = Node(data)

        if self.size == 1:
            self.bottom = node
        self.join(node, self.top)
        self.top = node
        return True

    def pop(self):
        if not self.top:
            return None
        top = self.top
        self.top = self.top.below
        self.size -= 1
        return top.data

    def remove_bottom(self):
        bottom = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return bottom.data

    
class SetOfStacks:
    """
    Stack implementation that creates a new stack when a certain threshold is reached for the current stack.
    """
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []

    def get_last_stack(self):
        if not self.stacks:
            return None 
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()

    def push(self, data):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(data)
        else:
            stack = Stack(self.threshold)
            stack.push(data)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        data = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return data

    def pop_at(self, index):
        return self.left_shift(index, True)

    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            data = self.left_shift(index + 1, False)
            stack.push(data)
        return removed_item


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []

        for _ in range(31):
            lst.append(stacks.pop_at(0))
        assert lst == list(range(4, 35))



if __name__ == "__main__":
    unittest.main()

