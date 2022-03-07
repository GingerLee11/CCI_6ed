# python3
# circular_array.py - Array like data structure that allows for efficient rotations.

import time

# Without using deque:

class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.key)


class CircularArray:
    """
    Array like data structure that allows for efficient rotations.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key):
        """
        Adds nodes to the end of the array
        """
        if self.is_empty() == True:
            self.head = self.tail = Node(key)
        else:
            self.tail.next = Node(key, self.tail, None)
            self.tail = self.tail.next
        return self

    def is_empty(self):
        return self.head == None

    def popleft(self):
        if self.is_empty() == True:
            raise Exception("Popping from an empty array.")
        elif self.head.next == None:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head

            # Clear old node relationships and create new ones for next node
            new_head = self.head.next
            self.head = new_head
            self.head.next = new_head.next
            self.head.prev = None
        return node

    def rotate(self, num_rotations):
        if self.is_empty() == True:
            raise Exception("Rotating an empty array.")
        else:
            for x in range(num_rotations):
                node = self.popleft()
                self.add(node.key)

    def __str__(self):
        values = [str(x) for x in self]
        return " <--> ".join(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next



def example():
    circular_array = CircularArray()
    
    for x in range(1, 10):
        circular_array.add(x)
        circular_array.rotate(10)
        print(circular_array)

    circular_array.rotate(10)
    print(circular_array)
    circular_array.popleft()
    print(circular_array)

    for x in range(1, 9):
        circular_array.popleft()

    start = time.time()
    for x in range(1, 100):
        circular_array.add(x)
    start = time.time()
    circular_array.rotate(1000)
    end = time.time()
    difference = end - start    
    print(f"100 items: {round(difference, 16)} seconds")
    for x in range(1, 100):
        circular_array.popleft()

    for x in range(1, 1000):
        circular_array.add(x)

    start = time.time()
    circular_array.rotate(1000)
    end = time.time()
    difference = end - start    
    print(f"10000 items: {round(difference, 16)} seconds")

    for x in range(1, 1000):
        circular_array.popleft()

    
    for x in range(1, 100):
        circular_array.add(x)

    start = time.time()
    circular_array.rotate(10)
    end = time.time()
    difference = end - start  
    print(f"10 rotations: {round(difference, 16)} seconds")

    start = time.time()
    circular_array.rotate(100)
    end = time.time()
    difference = end - start  
    print(f"100 rotations: {round(difference, 16)} seconds")

    start = time.time()
    circular_array.rotate(10000)
    end = time.time()
    difference = end - start  
    print(f"10000 rotations: {round(difference, 16)} seconds")

    start = time.time()
    circular_array.rotate(1000000)
    end = time.time()
    difference = end - start  
    print(f"1000000 rotations: {round(difference, 16)} seconds")

    
if __name__ == "__main__":
    example()