# python3
# sub_sort.py - Given an array it returns the indicies needed to sort an array. 
# I.e. only the values from a certain sub selection of the array need to be sorted.

import unittest
from random import randint

def sub_sort(array):
    """
    Given an array it returns the indicies needed to sort an array. 
    I.e. only the values from a certain sub selection of the array need to be sorted.
    """
    if array == sorted(array):
        return (0, len(array) - 1)

    first, last = None, None
    for indx, n1 in enumerate(array):
        if first != None:
            break
        for i in range(indx, (len(array) - indx)):
            n2 = array[indx + (i)]
            if n1 > n2:
                first = indx
                break

    indx = len(array) - 1
    for n1 in reversed(array):
        if last != None:
            break
        for i in range(0, indx - 1, 1):
            n2 = array[indx - (i)]
            if n1 < n2:
                last = indx
                break
        indx -= 1

    return (first, last)


def example():

    ex_array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

    print(sub_sort(ex_array))


class Test(unittest.TestCase):
    large_array = [1, 2, 1, 4, 5, 6, 39, 8, 9, 10]
    for i in range(100000):
        x = randint(3, 1000)
        large_array.append(x)
    large_array.append(2)
    for i in range(100):
        i += 100000
        large_array.append(i)

    tests = [
        ([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], (3, 9)),
        ([1, 2, 4, 6, 7, 7, 7, 10, 11, 12, 16, 18, 19], (0, 12)),
        (large_array, (1, 100010))
        
    

    ]
    def test_sub_sort(self):
        for array, expected in self.tests:
            actual = sub_sort(array)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
