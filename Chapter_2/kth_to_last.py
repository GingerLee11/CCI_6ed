# python3
# kth_to_last.py - Finds the index of an element counting k elements from the end of a singly linked list.

from collections import deque


def index_from_end(linked_list, k):
    '''
    Finds the index of an element counting k elements from the end of a singly linked list.

    index_from_end(linked_list, 3)
    '''

    # Check to make sure that k is not larger than the len of the linked list
    if len(linked_list) < k:
        return print(f"Please choose an index less than the length of the linked list: {len(linked_list)}. Current index is {k}.")

    # Subtract k from the length of the linked list to find the backward index of the k element
    back_index = len(linked_list) - k

    for i in range(len(linked_list)):
        if i == back_index:
            return print(linked_list[i])


numbers = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

'''
index_from_end(numbers, 3)
index_from_end(numbers, 2)
index_from_end(numbers, 0) # returns nothing since this is the end of the list
index_from_end(numbers, 21)
'''