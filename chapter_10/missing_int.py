# python3
# missing_int.py - Searches through a very large number of non-negative integers to see if there are any "missing" ints.
# I.e. [1, 2, 3, 5, 6, 7, 8, 9] In this list, 4 would be missing.

from  math import log10, floor
from random import randint

import unittest

def create_digit_dict(file):
    """
    Creates a dictionary for each digit (1s, 10s, 100s, 1000s). 
    The correlating values would be represented as 0, 1, 2, 3...
    """
    digit_dict = {}

    for num in file:
        # Check if 0 since this will cause an error
        if num == 0:
            digit = 0
        else:
            digit = floor(log10(num))

        if digit in digit_dict:
            low = 0
            high = len(digit_dict[digit]) - 1
            mid = 0

            if len(digit_dict[digit]) == 1:
                if num <= digit_dict[digit][0]:
                    digit_dict[digit].insert(0, num)
                elif num > digit_dict[digit][0]:
                    digit_dict[digit].append(num)
                continue

            while low <= high:
                mid = floor((low + high) / 2)
                if low == high:
                    digit_dict[digit].insert(mid + 1, num)
                    break
                elif digit_dict[digit][mid] < num:
                    low = mid + 1
                elif digit_dict[digit][mid] > num:
                    high = mid - 1
                elif digit_dict[digit][mid] == num:
                    digit_dict[digit].insert(mid, num)
                    break
            
        else:
            digit_dict[digit] = [num]
    
    return digit_dict


def missing_int(digit_dict):
    """
    Searches through a very large number of non-negative integers to see if there are any "missing" ints.
    I.e. [1, 2, 3, 5, 6, 7, 8, 9] In this list, 4 would be missing.
    """
    all_digits = [x for x in range(len(digit_dict))]
    increments_of_10 = [0]
    for x in range(1, len(digit_dict)):
        increments_of_10.append(10 ** x)
    num_of_ints = [10 ** (i+1) - 10 ** (i) for i in range(len(digit_dict))]
    # Add one the the first total since 10 ** 0 == 1 not 0
    num_of_ints[0] += 1
    # List of the digits where integers may be missing
    possible_missing = []
    # Check to see if the actual number of digits matches how many there should be
    for digit, total_ints in zip(all_digits, num_of_ints):

        total = len(digit_dict[digit])
        if total !=  total_ints:
            possible_missing.append(digit)

    missing_ints = []
    for x_10, digit in zip(increments_of_10, all_digits):
        if x_10 not in digit_dict[digit]:
            missing_ints.append(x_10)

    for pos_digit in possible_missing:
        if pos_digit == 0:
            last_num = 0
        else:
            last_num = 10 ** pos_digit
        for curr_num in digit_dict[pos_digit]:

            if curr_num - last_num > 1:
                difference = curr_num - last_num
                for x in range(1, difference):
                    missing_ints.append(curr_num - x)
            
            last_num = curr_num

    return missing_ints



def example():

    missing_nums = []
    for x in range(10):
        num = randint(1, 99998)
        if num not in missing_nums:
            missing_nums.append(num)

    print(sorted(missing_nums))
    list_of_ints = [x for x in range(100000) if x not in missing_nums]
    d_dict = create_digit_dict(list_of_ints)
    missing_ints = missing_int(d_dict)
    print(sorted(missing_ints))


class Test(unittest.TestCase):
    
    def generate_missing_numbers(self):
        self.missing_nums = []
        for x in range(10):
            num = randint(1, 999998)
            if num not in self.missing_nums:
                self.missing_nums.append(num)

        list_of_ints = [x for x in range(1000000) if x not in self.missing_nums]
        return list_of_ints

    def test_missing_int(self):
        int_file = self.generate_missing_numbers()
        expected = self.missing_nums
        actual = missing_int(create_digit_dict(int_file))
        assert sorted(expected) == sorted(actual)

if __name__ == "__main__":
    unittest.main()