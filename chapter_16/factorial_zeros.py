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
    for i in fact_num:
        if i != '0':
            count = 0
        elif i == '0':
            count += 1
    return count


def example():
    for x in range(100):
        print(factorial_zero(x))


class Test(unittest.TestCase):

    tests = [
        (1, 0),
        (5, 1),
        (-1, 0),
        (0, 0),
        (10, 2),
    ]
    
    def test_factorial_zeros(self):
        for n, expected in self.tests:
            actual = factorial_zero(n)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
