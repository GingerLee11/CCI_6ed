# python3
# check_permutations.py - Checks whether one string is a permutation of another string

'''
# Brute Force method:
# Split both strings into indiv comps and check if chats in not in one string. If not, then False

def check_permutation(s1, s2):
    ''''''
    Checks whether one string is a permutation of another string.
    ''''''
    # Quick len() check
    if len(s1) != len(s2):
        return print("Different length; not permutation.")

    # Loop through all indiv chars for both s
    s1_chars = [char for char in s1]
    for char1 in s1.lower():
        for char2 in s2.lower():
            if char2 not in s1_chars:
                return print("Not Permutation")
    return print("Permutation")


check_permutation("taco cat", "tact coa") # True
check_permutation("buffalo", "olaffbu") # True
check_permutation("dog", "god")  # True
check_permutation("snack", "snick")  # False 
check_permutation("snack", "snacks")  # False; different length
check_permutation("iiiij", "ijjjj")  # False --> But returns True


# Regex implementation:
import re

def check_permutation(s1, s2):
    # If lengths are unequal not permutation  
    if len(s1) != len(s2):
        return print("Different length; not permutation.")

    # Create regex
    s_regex = re.compile(f'[{s1}]')
    mo = re.search(s_regex, s2)
    if mo != None:
        return print("Permutation")
    else:
        return print("Not Permutation")


check_permutation("taco cat", "tact coa") # True
check_permutation("buffalo", "olaffbu") # True
check_permutation("dog", "god")  # True
check_permutation("snack", "snick")  # False 
check_permutation("snack", "snacks")  # False; different length
check_permutation("iiiij", "ijjjj")  # False --> But returns True
'''

# Dictionary implementation:

def check_permutation(s1, s2):
    '''
    Checks whether one string is a permutation of another string.
    '''
    # If lengths are unequal not permutation  
    if len(s1) != len(s2):
        return print("Different length; not permutation.")

    # Create dictionaries for both strings
    def string_count_dict(s):
        '''
        Takes in a string and returns the count of each character
        '''
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        return s_dict

    s1_dict = string_count_dict(s1)
    s2_dict = string_count_dict(s2)

    # Check if the dictionaries are equal
    if s1_dict == s2_dict:
        return print("Permutation")
    else: 
        return print("Not Permutation")

check_permutation("taco cat", "tact coa") # True
check_permutation("buffalo", "olaffbu") # True
check_permutation("dog", "god")  # True
check_permutation("snack", "snick")  # False 
check_permutation("snack", "snacks")  # False; different length
check_permutation("iiiij", "ijjjj")  # False

