# python3
# T9.py - Given a string of numbers (representing the numbers on old cell phones), 
# a Trie of valid words, 
# and a dictionary mapping the numbers to their corresponding numbers, 
# A list of valid matching words are returned.

from collections import deque
from trie import EnglishLanguageTrie
from english_words import english_words_lower_alpha_set

import unittest

def numeric_search(numbers, valid_words, num_to_letters_dict):
    """
    Given a string of numbers (representing the numbers on old cell phones), 
    a Trie of valid words, 
    and a dictionary mapping the numbers to their corresponding numbers, 
    A list of valid matching words are returned.
    """
    possible_prefixes = deque()
    possible_words = []

    for num in numbers:
        if num not in num_to_letters_dict:
            return set()
        letters = num_to_letters_dict[num]

        if len(possible_prefixes) == 0:
            for letter in letters:
                prefix = ''
                prefix += letter
                match = valid_words.search_prefix(prefix)
                if match == True:
                    possible_prefixes.append(prefix)
        else:
            curr_prefixes = possible_prefixes
            possible_prefixes = deque()
            while len(curr_prefixes) > 0:
                prefix = curr_prefixes.popleft()
                for letter in letters:
                    prefix_changed = prefix
                    prefix_changed += letter
                    match = valid_words.search_prefix(prefix_changed)
                    if match == True:
                        possible_prefixes.append(prefix_changed)
    # Iterate through all the possible prefixes again
    # To check that they are actually valid words not just
    # valid prefixes
    for word in possible_prefixes:
        match_word = valid_words.search_word(word)
        if match_word == True:
            possible_words.append(word)
    
    return set(possible_words)


def example():

    num_to_letters_dict = {
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], 
        '7': ['p', 'q', 'r', 's'], 
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z'], 
    }
    english_trie = EnglishLanguageTrie()
    english_words = english_words_lower_alpha_set
    for word in english_words:
        english_trie.add_word(word)
    english_trie.add_word('used')

    
    numbers = '8733'
    print(numeric_search(numbers, english_trie, num_to_letters_dict))


class Test(unittest.TestCase):

    def set_up_data_structures(self, words):

        num_to_letters_dict = {
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], 
        '7': ['p', 'q', 'r', 's'], 
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z'], 
        }
        english_trie = EnglishLanguageTrie()
        english_words = english_words_lower_alpha_set
        for word in english_words:
            english_trie.add_word(word)

        for word in words:
            english_trie.add_word(word)

        return num_to_letters_dict, english_trie

    tests = [

        ('8733', set(['tree', 'used'])),
        ('3337', set(['deep', 'deer'])),
        ('4663', set(['good', 'hood', 'gone', 'goof', 'home', 'hone', 'hoof'])),
        ('277', set(['ass'])),
        ('2340', set([])),
        ('4613', set([])),
        ('asdpo', set([])),
        ('233', set(['add', 'bed', 'bee'])),

    ]

    def test_numeric_search(self):
        num_to_let_dict, english_trie = self.set_up_data_structures(['used'])
        for numbers, expected in self.tests:
            actual = numeric_search(numbers, english_trie, num_to_let_dict)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
