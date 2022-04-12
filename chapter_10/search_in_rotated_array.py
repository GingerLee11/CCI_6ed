# python3
# search_in_rotated_array.py - Returns the index of a given elem if present in an array.

import unittest

def search_rotated_array(array, elem):
    """
    Returns the index of a given elem if present in an array.
    """
    first = array[0]
    last = array[-1]
    biggest = max(array)
    smallest = min(array)

    if elem > biggest or elem < smallest:
        return f"{elem} is not contained within the array."

    if elem >= first:
        for indx, n in enumerate(array):
            if n == elem:
                return indx
    
    elif elem <= last:
        for indx, n in reversed(list(enumerate(array))):
            if n == elem:
                return indx
    
    return f"{elem} is not contained within the array."


class Test(unittest.TestCase):

    ex_list = [x for x in range(101)]
    array = ex_list[37:] + ex_list[:37]

    tests = [
        (array, 73, 36),
        (array, 100, 63),
        (array, 21, 85),
        (array, 37, 0),
        (array, 36, 100),
        (array, 29384723, "29384723 is not contained within the array."),
        (array, -129, "-129 is not contained within the array."),
    ]

    def test_search_rotated_array(self):
        for array, elem, expected in self.tests:
            actual = search_rotated_array(array, elem)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
