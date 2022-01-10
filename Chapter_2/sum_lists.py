# python3
# sum_lists.py - Takes in two linked lists and then returns the sum of the reverse order of those lists.

from collections import deque

def sum_list_reverse(num_list):
    '''
    Helper function that takes the reverse sum of any linked list comprised only of numbers.
    num_list.pop()
    returns a string of the number
    '''

    # Create an empty string to store the values
    n = ''

    # Pop of the elements one by one until the list is empty
    while len(num_list) != 0:
        if n == '':
            n = str(num_list.pop())
        else:
            n += str(num_list.pop())
        
    return n

def sum_list_forward(num_list):
    '''
    Helper function that takes the reverse sum of any linked list comprised only of numbers.
    num_list.pop()
    returns a string of the number
    '''

    # Create an empty string to store the values
    n = ''

    # Leftpop of the elements one by one until the list is empty
    while len(num_list) != 0:
        if n == '':
            n = str(num_list.popleft())
        else:
            n += str(num_list.popleft())
        
    return n


def sum_lists(nums1, nums2, direction):
    '''
    Takes in two linked lists and then returns the sum of the those lists in reverse or forward order.
    Ex: sum_lists(number_1, number_2, 'reverse')
    Ex: sum_lists(number_1, number_2, 'forward')

    '''
    if direction == 'reverse':
        # Call helper function to get number as string
        num_add_1 = sum_list_reverse(nums1)
        num_add_2 = sum_list_reverse(nums2)

    elif direction == 'forward':
        # Call helper function to get number as string
        num_add_1 = sum_list_forward(nums1)
        num_add_2 = sum_list_forward(nums2)

    else:
        return print("Type in either forward or reverse to pick a summation direction")

    num_sum = int(num_add_1) + int(num_add_2)
    llist_sum = deque(str(num_sum))
    return llist_sum


number_1 = deque([7,1,6])
number_2 = deque([5,9,2])

sum_lists(number_1, number_2, 'reverse') # Should return 912

number_1 = deque([7,1,6])
number_2 = deque([5,9,2])

sum_lists(number_1, number_2, 'forward') # Should return 1308

# Downside to current implementation is that numbers have to be redefined for every call of sum_lists