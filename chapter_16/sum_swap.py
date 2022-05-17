# python3
# sum_swap.py - Finds two values in two arrays that if swapped would result in both arrays having the same sum.
# If those two values are not present, returns None.

import unittest

def sum_swap(array1, array2):
    """
    Finds two values in two arrays that if swapped would result in both arrays having the same sum.
    If those two values are not present, returns None.
    """
    sum1 = sum(array1)
    sum2 = sum(array2)
    sum_diff = abs(sum1 - sum2)
    if sum_diff % 2 == 1:
        return None
    if sum1 == sum2:
        return None
    elif sum1 > sum2:
        
        # TODO: Add a check if not an integer
        # Odd differences might not be possible to swap
        diff = round(sum_diff / 2)
        for indx1, num1 in enumerate(array1):
            for indx2, num2 in enumerate(array2):
                if num1 - num2 == diff:
                    array1[indx1] = num2
                    array2[indx2] = num1
                    sum1 = sum(array1)
                    sum2 = sum(array2)
                    if sum1 == sum2:
                        return (num1, num2)
                    else:
                        return None

    else:
        diff = sum_diff / 2
        for indx2, num2 in enumerate(array2):
            for indx1, num1 in enumerate(array1):
                if num2 - num1 == diff:
                    array1[indx1] = num2
                    array2[indx2] = num1
                    sum1 = sum(array1)
                    sum2 = sum(array2)
                    if sum1 == sum2:
                        return (num1, num2)
                    else:
                        return None


class Test(unittest.TestCase):

    tests = [
        (
            [4, 1, 2, 1, 1, 2],
            [3, 6, 3, 3],
            (1, 3),
        ),
        (
            [3, 6, 3, 3],
            [4, 1, 2, 1, 1, 2],
            (3, 1),
        ),
        (
            [3, 6, 3, 2],
            [4, 1, 2, 1, 1, 2],
            None,
        ),
        (
            [1, 6, 3, 3],
            [4, 3, 2, 1, 1, 2],
            None,
        ),
    ]
    
    def test_sum_swap(self):
        for array1, array2, expected in self.tests:
            actual = sum_swap(array1, array2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
