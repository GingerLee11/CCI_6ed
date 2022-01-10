# python3
# llist_partition.py - Returns a linked list with elements less than the partitioned element "x" on the left side, 
# and elements greater than x on the right side

from collections import deque

def llist_partition(llist, x):
    """
    Returns a linked list with elements less than the partitioned element "x" on the left side, and elements greater than x on the right side
    """

    # Created an empty partitioned list to add elements to
    partitioned_llist = deque()

    for elem in llist:

        if elem < x:
            partitioned_llist.appendleft(elem)

        if elem >= x:
            partitioned_llist.append(elem)

    return print(partitioned_llist)

numbers = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
numbers = deque([10, 5, 1, 2, 3, 6, 2, 9, 1, 3, 4, 5, 6, 7, 8, 9,2, 1, 23, 5, 4, 5, 6234, 3])

llist_partition(numbers, 5)
