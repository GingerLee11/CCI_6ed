# python3
# peaks_and_valleys.py - Given an array of integers, the array is assorted by alternating peaks and valleys.
# A peak is defined as when an integer is adjacent to only integers that are less than or equal to it.
# A valley is defined as when an integer is adjacent to only integers that are greater than or equal to it.

import unittest
from random import randint

def peaks_and_valleys(array):
    """
    Given an array of integers, the array is assorted by alternating peaks and valleys.
    A peak is defined as when an integer is adjacent to only integers that are less than or equal to it.
    A valley is defined as when an integer is adjacent to only integers that are greater than or equal to it.
    """
    p_and_v_check = [False for x in range(len(array))]
    while False in p_and_v_check:
        
        for indx, num in enumerate(array):
        
            # Break out of loop if all elems are True
            if False not in p_and_v_check:
                break

            # Continue to the next integer if this is already true
            if p_and_v_check[indx] == True:
                continue

            # Peak condition
            if indx % 2 == 0:
                # Check for zero since there is no intger to the left (indx -1)
                if indx == 0:
                    if num >= array[indx + 1]:
                        p_and_v_check[indx] = True
                    else:
                        next_num = array[indx + 1]
                        array[indx] = next_num
                        array[indx + 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx + 1] = False
                # Check for last item in the array since there is no intger to the right (indx + 1)
                elif indx == len(array) - 1:
                    if num >= array[indx - 1]:
                        p_and_v_check[indx] = True
                    else:
                        prev_num = array[indx - 1]
                        array[indx] = prev_num
                        array[indx - 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx - 1] = False

                else:
                    if num >= array[indx - 1] and num < array[indx + 1]:
                        next_num = array[indx + 1]
                        array[indx] = next_num
                        array[indx + 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx + 1] = False

                    elif num >= array[indx + 1] and num < array[indx - 1]:
                        prev_num = array[indx - 1]
                        array[indx] = prev_num
                        array[indx - 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx - 1] = False

                    elif num >= array[indx + 1] and num >= array[indx - 1]:
                        p_and_v_check[indx] = True

            # Valley condition
            elif indx % 2 == 1:
                # Check for last item in the array since there is no intger to the right (indx + 1)
                if indx == len(array) - 1:
                    if num <= array[indx - 1]:
                        p_and_v_check[indx] = True
                    else:
                        prev_num = array[indx - 1]
                        array[indx] = prev_num
                        array[indx - 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx - 1] = False

                else:
                    if num <= array[indx - 1] and num > array[indx + 1]:
                        next_num = array[indx + 1]
                        array[indx] = next_num
                        array[indx + 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx + 1] = False

                    elif num <= array[indx + 1] and num > array[indx - 1]:
                        prev_num = array[indx - 1]
                        array[indx] = prev_num
                        array[indx - 1] = num
                        # Reset the values back to False since they did not meet the conditions
                        p_and_v_check[indx] = False
                        p_and_v_check[indx - 1] = False

                    elif num <= array[indx + 1] and num <= array[indx - 1]:
                        p_and_v_check[indx] = True    
    return array


def example():

    test_array = [randint(0, 1000000) for x in range(10000)]
    
    peaks_and_valleys(test_array)


class Test(unittest.TestCase):

    test_arrays = [
        [5, 8, 6, 2, 3, 4, 6],
        [5, 8, 2, 6, 3, 6, 4],
        [1, 1, 1, 1, 1, 1, 1],
        [10, 12, 13, 14, 15, 16],
    ]
    peak_and_valley_arrays = [
        [8, 5, 6, 2, 4, 3, 6],
        [8, 2, 6, 3, 6, 4, 5],
        [1, 1, 1, 1, 1, 1, 1],
        [12, 10, 14, 13, 16, 15],
    ]

    def test_peaks_and_valleys(self):
        for array, expected in zip(self.test_arrays, self.peak_and_valley_arrays):
            actual = peaks_and_valleys(array)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
