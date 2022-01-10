# python3 
# intersection.py - Checks whether two linked lists "intersect"; 
# whether the two linked lists have the same value at the same reference

from collections import deque

def intersection(llist1, llist2):
    """
    Checks whether two linked lists "intersect";
    whether the two linked lists have the same value at the same reference
    """
    k = ''
    j = ''

    while (len(llist1) != 0) & (len(llist2) != 0):

        k = llist1.popleft()
        j = llist2.popleft()

        if k == j:
            return print(f'These two lists intersect at {k}.')

    return print("These lists do not intersect.")


letters1 = deque('abcdefghijklmnopq')
letters2 = deque('qponmlkjihgfedcba')

intersection(letters1, letters2) # 'i'

letters1 = deque('abcdefghijklmnop')
letters2 = deque('ponmlkjihgfedcba')


intersection(letters1, letters2) # 'These lists do not intersect.'