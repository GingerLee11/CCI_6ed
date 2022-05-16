# python3
# trie.py - Trie implementation for words in the English Language.

from string import printable
from english_words import english_words_lower_alpha_set
import unittest


class Node:

    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
        self.children = {}
        self.word_end = False


class EnglishLanguageTrie:

    def __init__(self):
        self.root = None
        self.alphabet = list(printable)

    def is_empty(self):
        return self.root == None

    def add_word(self, word):
        """
        Adds a word to the prefix Trie
        """
        if self.is_empty() == True:
            self.root = Node(None, None)
        node = self.root
        for indx, letter in enumerate(word):
            if letter not in self.alphabet:
                raise Exception(f"{word} is not an English word.") 
            # If the letter is not already in the children dictionary
            # Add the letter and move down into the node
            if letter not in node.children:
                node.children[letter] = Node(letter, node)
            node = node.children[letter]
            if indx == len(word) - 1:
                node.word_end = True

    def search_prefix(self, prefix):
        """
        Searches through the prefix Trie and returns True if the prefix is contained within the Trie
        Otherwise, it returns False
        """
        if self.is_empty() == True:
            raise Exception("Cannot search an empty Trie.")
        else:
            node = self.root
            for indx, char in enumerate(prefix):
                if char in node.children:
                    node = node.children[char]
                    if indx == len(prefix) - 1:
                        return True
                else:
                    return False
            
    def search_word(self, word):
        """
        Searches through the Trie and returns True only if the word is contained within the Trie 
        and the word_end boolean flag matches to the end of the word.
        """
        if self.is_empty() == True:
            raise Exception("Cannot search an empty Trie.")
        else:
            node = self.root
            for indx, letter in enumerate(word):
                if letter in node.children:
                    node = node.children[letter]
                    # End of the word and the word_end == True
                    if indx == len(word) - 1 and node.word_end == True:
                        return True
                else:
                    return False



class Test(unittest.TestCase):

    def initialize_trie(self, english_words):

        english_trie = EnglishLanguageTrie()
        for word in english_words:
            english_trie.add_word(word)
        
        not_found = []
        for word in english_words:
            match = english_trie.search_word(word)
            if match == False:
                not_found.append(word)

        return not_found

    def test_trie(self):
        expected = []
        actual = self.initialize_trie(english_words_lower_alpha_set)
        assert actual == expected
        
        
if __name__ == "__main__":
    unittest.main()
