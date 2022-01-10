# python3
# palindrome_permutation.py - Determines whether a string is a permutation of a palindrome.


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

def palindrome_permutation(s):
    '''
    Determines whether a string is a permutation of a palindrome. 
    Rules: 
    If a string has only characters with even counts (2, 4, 6, etc...) then it is a permutation of a palindrome.
    A string may have one character with an odd count and still be a palindrome.
    '''
    s = s.replace(' ', '')

    # Create a dictionary of the count of all the characters in the string
    count_dict = string_count_dict(s)
    # Go through every count in the dictionary and increment when there is a character with an odd count. 
    odd_count = 0
    for count in count_dict.values():
        if count % 2 == 1:
            odd_count += 1

    if odd_count > 1:
        return ("Not Permutation")

    elif odd_count == 1:
        return ("Permutation; one odd")

    else:
        return ("Permutation; all even")

    
# palindrome_permutation("taco cat")