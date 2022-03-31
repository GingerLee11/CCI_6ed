# python3
# permutations_without_dups.py - Computes all the permutations for a given string with unique characters.

from collections import deque


def permutations_without_dups(text, char=None, perm=None, all_permutations=None):
    """
    Computes all the permutations for a given string with unique characters.
    """
    if perm == None:
        perm = ''

    all_permutations = []
    text_deque = deque(text)
    while len(text_deque) != 0: 
        char = text_deque.popleft()
        perm += char
        perm = perms_wo_dups(char, text_deque, perm)
        all_permutations.append(perm)

    return all_permutations


def perms_wo_dups(char, text, perm=None):
    """
    Helper recursive function for permutations without dups
    """
    if perm == None:
        perm = ''
    
    while len(text) != 0:
        char_2 = text.popleft()
        perm += char_2
        perm = perms_wo_dups(char_2, text, perm)

    return perm


print(permutations_without_dups('abcd'))
