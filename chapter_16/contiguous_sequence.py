# python3
# contiguous_sequence.py - Returns the largest sum in an array containing negative and positive integers.

import unittest
from random import randint


def contiguous_sequence(array):
    """
    Returns the largest sum in an array containing negative and positive integers.
    """
    last = None
    max_sum = 0
    sum = 0
    for n in array:
        if n < 0:
            if last != None:
                if abs(n) < last or (sum + n) > 0:
                    sum += n
                else:
                    sum = 0
        else:
            sum += n

        if sum > max_sum:
            max_sum = sum

        last = n

    return max_sum


def example():
    test_array = []
    for i in range(10000):
        int_sign = randint(0, 1)
        if int_sign == 0:
            num = randint(1, 10000)
            test_array.append(num)
        else:
            num = randint(-9999, -1)
            test_array.append(num)
            
    print(contiguous_sequence(test_array))



class Test(unittest.TestCase):

    tests = [
        ([2, -8, 3, -2, 4, -10], 5),
        ([-5, 2, -3, 10, -4, 1, -2], 10),
        ([-5, -2, -3, -10, -4, 1, -2, 3], 3),
        ([5, -2, 3, -1, 4, -4, -2, 5], 9),
    ]
    def test_contiguous_sequence(self):
        for array, expected in self.tests:
            actual = contiguous_sequence(array)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
    