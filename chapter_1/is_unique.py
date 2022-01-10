# python3
# is_unique.py - Checks to see if all characters in a string are unique

# Edge cases: 
# String is empty or contains only one char

# Brute force method: 
# Split string into indiv chars and then append to new list if elem is not present 

def is_unique(s):
    # Edge case for empty string
    if len(s) == 0: 
        return print("Empty String.")

    # Edge case for string with one element
    if len(s) == 1:
        return True
    
    # Split string into indiv chats & loop through chars; exit if char is already present 
    unique_chars = []
    for char in s:
        if char in unique_chars:
            return False
        else:
            unique_chars.append(char)

    return True

is_unique("apple") # False
is_unique("pear") # True 
is_unique("A") # Edge Case: True
is_unique("") # Empty String: Empty String
