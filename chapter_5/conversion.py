# python3
# conversion.py - Takes in two integers and 
# returns that number of bits needed to be flipped to make the two integer identical

from insertion import convert_to_binary
from next_number import count_ones

import unittest

def conversion(num1, num2):
    """
    Takes in two integers and 
    returns that number of bits needed to be flipped to make the two integer identical.
    """
    not_maching = num1 ^ num2
    bin_num = convert_to_binary(not_maching)
    num_of_ones = count_ones(bin_num)
    return num_of_ones


class Test(unittest.TestCase):

    tests = [
        (29, 15, 2),
        (13, 5, 1),
        (8, 1, 2),
    ]

    def test_conversion(self):
        for num1, num2, expected in self.tests:
            actual = conversion(num1, num2)
            print(f"Actual:   {actual}\nExpected: {expected}")
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
