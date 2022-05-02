# python3
# word_frequencies.py - Find the frequency of a word or list of words in a "book".

import re
import os


def word_frequency(book, word):
    """
    Find the frequency of a word in a book.
    """
    word_regex = fr"\b{word}\b"
    words = re.findall(word_regex, book)
    return len(words)


def check_word_frequencies(book, list_of_words, word_freq_dict=None):
    """
    Find all the frequencies of a list of words 
    and returns a dictionary with all the frequencies.
    """
    if word_freq_dict == None:
        word_freq_dict = {}
    for word in list_of_words:
        # if word not in word_freq_dict:
        word_count = word_frequency(book, word)
        word_freq_dict[word] = word_count

    return word_freq_dict


def example():
    folder = r'C:\Users\Cleme\Practice_Code\Interview_prep\CCI_6ed\chapter_16'
    os.chdir(folder)
    with open('1112.txt', 'r') as r_and_j:
        romeo_and_juliet = ''
        for line in r_and_j:
            romeo_and_juliet += line

    r_and_j_words = ['you', 'I', 'the', 'thou', 'Romeo', 'Juliet', 'Montagues', "Montague", 'Capulet', 'Capulets', 'Verona', 'lovers', 'love']

    word_freq_dict = check_word_frequencies(romeo_and_juliet, r_and_j_words)
    print(word_freq_dict)

if __name__ == "__main__":
    example()
