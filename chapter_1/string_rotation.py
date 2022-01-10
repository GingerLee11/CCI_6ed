# python3 
# String_rotation.py - Compares two string and determines whether one string is a rotation of the other.

from palindrome_permutation import string_count_dict

def string_rotation(s1, s2):
    '''
    Compares two string and determines whether one string is a rotation of the other.
    '''

    # Check len()s of strings
    if len(s1) != len(s2):
        return False
    
    # Create count dictionaries for each of the strings
    s1_dict = string_count_dict(s1)
    s2_dict = string_count_dict(s2)

    # Check if the two strings have the same count 
    # For each character:
    if s1_dict != s2_dict:
        return False

    # Store characters from s2 starting with initial char; s1[0]
    initial_chars = []
    for char in range(len(s2)):
        if s2[char] == s1[0]:
            initial_chars.append(char)

    # Loop through s2 starting at each initial char index
    s2_rot = ''
    for i in initial_chars:
        for char in range(i, len(s2) + i, 1):
            if i == len(s2) - 1:
                s2_rot += s2[char]
                char = 0
            elif i >= len(s2):
                char = char - len(s2)
                s2_rot += s2[char]
            else:   
                s2_rot += s2[char]
            i += 1

        if s1 != s2_rot:
            s2_rot = ''
            continue
        elif s1 == s2_rot:
            return True
    
    if s1 != s2_rot:
        return False

    
string_rotation('waterbottle', 'erbottlewat')
string_rotation('lollipop', 'oplollip')
string_rotation('lollipop', 'lipoplol')
string_rotation('sandwich', 'sandwiches')
string_rotation('eggplant', 'eggplent')
string_rotation('samurai', 'iarumas')