# python3
# Sorted_search_no_size.py - Searches through a array like data structure that doesn't have a size method.

import unittest


def no_size_sorted_search(array, elem):
    """
    Searches through a array like data structure that doesn't have a size method.
    """
    first = array[0]
    last = array[-1]

    if elem > last or elem < first:
        return f"{elem} is not contained within the array."

    if elem - first <= last - elem:
        for indx, n in enumerate(array):
            if n == elem:
                return indx
            if n > elem:
                return f"{elem} is not contained within the array."

    
    elif elem - first > last - elem:
        for indx, n in reversed(list(enumerate(array))):
            if n == elem:
                return indx
            if n < elem:
                return f"{elem} is not contained within the array."
    

    return f"{elem} is not contained within the array."


class Test(unittest.TestCase):

    array = [x for x in range(0, 2000001, 2)]


    tests = [
        (array, 72, 36),
        (array, 100, 50),
        (array, 20, 10),
        (array, 37, "37 is not contained within the array."),
        (array, 36, 18),
        (array, 29384723, "29384723 is not contained within the array."),
        (array, -129, "-129 is not contained within the array."),
        (array, 999999, "999999 is not contained within the array."),
        (array, 1000001, "1000001 is not contained within the array."),
        (array, 1989347, "1989347 is not contained within the array."),
        (array, 1000000, 500000),
        (array, 2000000, 1000000),
    ]

    def test_search_rotated_array(self):
        for array, elem, expected in self.tests:
            actual = no_size_sorted_search(array, elem)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
