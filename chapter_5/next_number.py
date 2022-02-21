# python3
# next_number.py

from insertion import convert_to_binary

import unittest

# TODO: Add logic for multiples of 2. E.g. 2, 4, 8, 16, 32.
# Should return the multiple below and above it 

# TODO: Add logic for 1 behind multiples of 2.
# Smaller integer should always be None

def count_ones(bin_num):
    """
    Helper function for next number that counts the number of ones in a binary string.
    """
    bit, num_of_ones = 0, 0
    
    while bit < len(bin_num):

        while bin_num[bit] != '0':
            num_of_ones += 1
            bit += 1
            if bit > len(bin_num) -1:
                break
        bit += 1

    return num_of_ones


def next_number(num):
    """
    Takes in a decimal number and prints the next smaller and larger integer
    with the same number of '1's in it's binary representation.
    """
    if num == 0:
        return None, None

    bin_num = convert_to_binary(num)
    num_of_ones = count_ones(bin_num)

    num_of_ones_smaller, num_of_ones_larger = 0, 0
    num_smaller, num_larger = num, num

    while num_of_ones_smaller != num_of_ones:
        num_smaller -= 1
        bin_num_smaller = convert_to_binary(num_smaller)
        num_of_ones_smaller = count_ones(bin_num_smaller)

        # Since it's possible that there won't be a number with the same number of ones smaller
        # Print None if num_smaller reaches zero
        if num_smaller == 0:
            print("There is no next smaller integer with the same number of ones.")
            num_smaller = None
            break 
        
    while num_of_ones_larger != num_of_ones:
        num_larger += 1
        bin_num_larger = convert_to_binary(num_larger)
        num_of_ones_larger = count_ones(bin_num_larger)
    
    return num_smaller, num_larger


class Test(unittest.TestCase):

    tests = [
        (0, None, None),
        (1, None, 2),
        (2, 1, 4),
        (3, None, 5),
        (4, 2, 8),
        (5, 3, 6),
        (6, 5, 9),
        (7, None, 11),
        (8, 4, 16),
        (9, 6, 10),
        (10, 9, 12),
        (11, 7, 13),
        (12, 10, 17),
        (13, 11, 14),
        (14, 13, 19),
        (15, None, 23),
        (16, 8, 32),
    ]

    def test_next_number(self):
        for num, expected_next_smallest, expected_next_largest in self.tests:
            actual_next_smallest, actual_next_largest = next_number(num)
            print(f"Actual:   {actual_next_smallest}\nExpected: {expected_next_smallest}")
            print(f"Actual:   {actual_next_largest}\nExpected: {expected_next_largest}")
            assert actual_next_smallest == expected_next_smallest
            assert actual_next_largest == expected_next_largest


if __name__ == "__main__":
    unittest.main()
