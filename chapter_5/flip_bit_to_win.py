# python3
# flip_bit_to_win.py - Takes in a decimal integer, then converts that value into a binary string.
# Returns the longest sequence of ones that can be created by flipping one zero.

from insertion import convert_to_binary

import unittest

def flip_bit_to_win(dec_num):
    """
    Takes in a decimal integer, then converts that value into a binary string.
    Returns the longest sequence of ones that can be created by flipping one zero.
    """
    bin_num = convert_to_binary(dec_num)

    bit, seq, max = 0, 0, -10
    sequence_of_ones = []

    while bit < len(bin_num) - 1:

        while bin_num[bit] != '0':
            seq += 1
            bit += 1
            if bit > len(bin_num) - 1:
                break

        if seq > max:
            max = seq
        sequence_of_ones.append(seq)
        seq = 0
        # Add this to "skip" past the zero's so as not to get stuck in an infinite loop
        bit += 1

    longest_sequence, seq_index = 0, 0

    for i, seq in enumerate(sequence_of_ones):

        if seq == max:
            if i == len(sequence_of_ones) - 1:
                longest_sequence = max + sequence_of_ones[i -1] + 1

            elif i == 0:
                seq_index += seq
                longest_sequence = max + sequence_of_ones[i + 1] + 1

            elif sequence_of_ones[i - 1] > sequence_of_ones[i + 1]:
                longest_sequence = max + sequence_of_ones[i -1] + 1

            elif sequence_of_ones[i - 1] < sequence_of_ones[i + 1]:
                seq_index += seq
                longest_sequence = max + sequence_of_ones[i -1] + 1

        else:
            seq_index += seq
            seq_index += 1

    return longest_sequence



class Test(unittest.TestCase):

    tests = [
        (),
    ]