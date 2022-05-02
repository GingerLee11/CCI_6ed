# python3
# factorial_zeros.py - calculates the nummber of trailing zeros contained within factorial n.

from math import factorial
import unittest

def factorial_zero(n):
    """
    calculates the nummber of trailing zeros contained within factorial n.
    """
    if n < 0:
        return 0
    fact_num = str(factorial(n))
    count = 0
    for i in reversed(fact_num):
        if i != '0':
            return count
        elif i == '0':
            count += 1
    return count


def example():
    tests_10 = [10, 100, 1000, 10000, 100000]
    tests_8 = [8, 64, 512, 4096, 32768]
    for n in tests_10:
        print(factorial_zero(n))
    for n in tests_8:
        print(factorial_zero(n))


class Test(unittest.TestCase):

    tests = [
        (1, 0),
        (5, 1),
        (-1, 0),
        (0, 0),
        (10, 2),
        (100000, 24999),
    ]
    
    def test_factorial_zeros(self):
        for n, expected in self.tests:
            actual = factorial_zero(n)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
