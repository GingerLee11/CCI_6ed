# python3
# magic_index.py - Given an array and an index, the function will return that value if it is in the array.

import unittest


def magic_index(array, i):
    """
    Given an array and an index, the function will return that value if it is in the array.
    """
    half_index = round(len(array) / 2)
    half = array[half_index]

    if i not in array:
        return None

    elif half == i:
        return half
    elif half > i:
        return magic_index(array[0: half_index], i)
    elif half < i:
        return magic_index(array[half_index: len(array)], i)
    else:
        return None


class Test(unittest.TestCase):

    array = [x for x in range(100)]
    array2 = [x for x in range(0, 100, 2)]
    array5 = [x for x in range(0, 100, 5)]

    huge_array = [x for x in range(10000000)]

    tests = [
        (array, 5, 5),
        (array, 95, 95),
        (array, 50, 50),
        (array, 1, 1),
        (array2, 1, None),
        (array2, 99, None),
        (array2, 90, 90),
        (array5, 46, None),
        (array, 293847239847, None),
    ]

    huge_test = [
        (huge_array, 828937, 828937)
    ]

    def test_magic_index(self):
        for array, i, expected in self.tests:
            actual = magic_index(array, i)
            assert actual == expected

    def test_magic_index_with_large_array(self):
        for array, i, expected in self.huge_test:
            actual = magic_index(array, i)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
