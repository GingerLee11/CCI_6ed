# python3
# palindrome.py - Checks if a linked list is a palindrome

from collections import deque


def palindrome(llist):
    """
    Checks if a linked list is a palindrome
    """


    # Define front and back placeholders to pop the characters from the string into
    front = ''
    end = ''

    # Check if the linked list is empty
    if len(llist) == 0:
        return print("Empty String")

    while len(llist) != 0:

        if len(llist) == 1:
            return True

        front = llist.popleft()
        end = llist.pop()

        if front != end:
            return False

    return True

'''
string_1 = deque('racecar')
string_2 = deque('a')
string_3 = deque('')
string_4 = deque(''.join('Was it a car or a cat I saw'.lower().split(' ')))
string_5 = deque('noon')
 
palindrome(string_1)
palindrome(string_2)
palindrome(string_3)
palindrome(string_4)
palindrome(string_5)
'''