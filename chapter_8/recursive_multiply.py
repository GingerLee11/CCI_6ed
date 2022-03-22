# python3
# recursive_multiply - Recursive function that multiplies two integers without using "*".


import unittest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from chapter_5.insertion import convert_to_binary, convert_to_decimal


def add_num(num, sum):
    """
    Adds a number to a sum
    """
    sum += num
    return sum


def recursive_multi_addition(a, b):
    """
    Recursive function that multiplies two integers without using the "*" operator.
    """
    sum = 0
    if a >= b:
        for x in range(b):
            sum = add_num(a, sum)
    elif a < b:
        for x in range(a):
            sum = add_num(b, sum)

    return sum


def recursive_multi_addition_2(a, b, sum=0):
    sum += a
    b -= 1
    if b != 0:
        return recursive_multi_addition_2(a, b, sum)
    else:
        return sum


def shift_left(bin_num):
    bin_num += '0'
    return bin_num


def multiplication_with_bit_shifting(a, b):
    sum = 0
    shifting = 1
    # Choose which ever number is smaller to be the "count" number
    # and whatever number is larger to be the number being added
    # for less overall computations
    if a >= b:
        a_bin = convert_to_binary(a)
        while b >= shifting:
            shifting *= 2
            if shifting > b:
                shifting /= 2
                b -= shifting
                break
            a_bin = shift_left(a_bin)   

        sum = convert_to_decimal(a_bin)
        while b > 0 and b != 0:
            sum += a
            b -= 1

    elif a < b:
        b_bin = convert_to_binary(b)
        while a >= shifting:
            
            # This is technically cheating since I'm using the "*" operator
            shifting *= 2
            if shifting > a:
                shifting /= 2
                a -= shifting
                break
            b_bin = shift_left(b_bin)
            
        sum = convert_to_decimal(b_bin)
        while a != 0:
            sum += b
            a -= 1
    
    return sum



class Test(unittest.TestCase):

    tests = [
        (3, 5, 15),
        (2, 2, 4),
        (10, 10, 100),
        (1, 1, 1),
        (5, 25, 125),
        (5, 25, 125),
        (238947387, 23984723, 5731086888768801) # recursive_multi_addition_2 causes a stock overflow at high numbers.
    ]

    functions = [multiplication_with_bit_shifting] # Fastest function by several orders of magnitude

    def test_recursive_multi_addition(self):
        for add_nums in self.functions:
            for a, b, expected in self.tests:
                actual = add_nums(a, b)
                assert actual == expected


if __name__ == "__main__":
    unittest.main()
