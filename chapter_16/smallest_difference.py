# python3
# smallest_difference.py - Calculates the smallest difference between all numbers in two arrays.

import unittest
from random import randint

def calc_diffs(array_1, array_2):
    """
    Helper function which does the actual calcs for the differences.
    """
    diff = 10 ** 99
    for num1 in array_1:
        if num1 in array_2:
            return 0
        for num2 in reversed(array_2):
            if abs(num1 - num2) < diff:
                diff = abs(num1 - num2)
            if abs(num1 - num2) > diff:
                break
    return diff

def smallest_difference(array_1, array_2):
    """
    Calculates the smallest difference between all numbers in two arrays.
    """
    max1, min1 = max(array_1), min(array_1) 
    max2, min2 = max(array_2), min(array_2) 

    if min1 >= max2:
        return abs(min1 - max2)
    elif min2 >= max1:
        return abs(min2 - max1)
    elif max2 == max1:
        return abs(max2 - max1)
    elif min2 == min1:
        return abs(min2 - min1)
    
    avg1 = sum(array_1) / len(array_1)
    avg2 = sum(array_2) / len(array_2)
    
    array_1 = sorted(array_1)
    array_2 = sorted(array_2)
    
    if avg1 >= avg2:
        diff = calc_diffs(array_1, array_2)
    else:
        diff = calc_diffs(array_2, array_1)    
    return diff


def example():

    list_1 = [randint(0, 1000) for x in range(100)]
    list_2 = [randint(1000, 100000) for x in range(100)]

    print(smallest_difference(list_1, list_2))
    print(smallest_difference(list_2, list_1))


class Test(unittest.TestCase):

    tests = [
        (
            [1, 3, 15, 11, 2],
            [23, 127, 235, 19, 8],
            3,
        ),
        (
            [1, 3, 15, 11, 4],
            [2, 14, 10, 6, 8],
            1,
        ),
        (
            [1, 3, 15, 11, 2],
            [2, 14, 10, 6, 8],
            0,
        ),
        (
            [1, 3, 15, 11, 2],
            [1, 14, 10, 6, 8],
            0,
        ),
        (
            [10, 23, 15, 74, 2938],
            [2, 5, 9, 6, 8],
            1,
        ),
        (
            [2, 5, 9, 6, 8],
            [10, 23, 15, 74, 2938],
            1,
        ),
        (
            [-1, 5, 9, 6, 8],
            [134, 23, 15, 74, 2938, -14],
            6,
        ),
    ]
    def test_smallest_difference(self):
        for list_1, list_2, expected in self.tests:
            actual = smallest_difference(list_1, list_2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
