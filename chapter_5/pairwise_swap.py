# python3
# pairwise_swap.py - Swaps the odd and even bits in a binary representation of an integer with as few instructions as possible.

from collections import deque
import unittest

from insertion import convert_to_binary, convert_to_decimal

def pairwise_swap(num):
    """
    Swaps the odd and even bits in a binary representation of an integer with as few instructions as possible.
    """
    bin_num = convert_to_binary(num)
    bin_queue = deque(bin_num)

    new_bin_num = ''

    while len(bin_queue) != 0:
        even = bin_queue.popleft()

        if len(bin_queue) != 0:
            odd = bin_queue.popleft()
            new_bin_num += odd
            
        new_bin_num += even

    num_swapped = convert_to_decimal(new_bin_num)
    return num_swapped


class Test(unittest.TestCase):

    tests = [
        (9, 6), # '0110'
        (19, 13), # '01101'
        (8, 4), # '0100'
        (46, 29), # '011101'
        (31, 31), # '011101'
    ]

    def test_parwise_swap(self):
        for num, expected in self.tests:
            actual = pairwise_swap(num)
            print(f"Actual:   {actual}\nExpected: {expected}")
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
