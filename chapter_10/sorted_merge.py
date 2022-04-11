# python3
# sorted_merge.py - Takes in two sorted arrays and returns one sorted array merging the two given arrays.

from collections import deque

import unittest

def sorted_merge(array_A, array_B):
    """
    Takes in two sorted arrays and returns one sorted array merging the two given arrays.
    """
    deque_A = deque(array_A)
    deque_B = deque(array_B)
    helper = []
    while len(deque_A) != 0 or len(deque_B) != 0:

        if len(deque_B) == 0:
            elem = deque_A.popleft()
        
        elif len(deque_A) == 0:
            elem = deque_B.popleft()
            
        elif deque_A[0] <= deque_B[0]:
            elem = deque_A.popleft()

        elif deque_B[0] < deque_A[0]:
            elem = deque_B.popleft()
            
        helper.append(elem)

    return helper


def example():

    A = [x for x in range(100)]
    B = [x for x in range(0, 200, 2)]

    A = [x for x in range(0, 1000, 7)]
    B = [x for x in range(0, 333, 3)]

    print(sorted_merge(A, B))

"""
if __name__ == "__main__":
    example()
"""

class Test(unittest.TestCase):

    A = [x for x in range(100)]
    B = [x for x in range(0, 200, 2)]
    C = [
        0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 16, 
        16, 17, 18, 18, 19, 20, 20, 21, 22, 22, 23, 24, 24, 25, 26, 26, 27, 28, 28, 29, 30, 
        30, 31, 32, 32, 33, 34, 34, 35, 36, 36, 37, 38, 38, 39, 40, 40, 41, 42, 42, 43, 44, 
        44, 45, 46, 46, 47, 48, 48, 49, 50, 50, 51, 52, 52, 53, 54, 54, 55, 56, 56, 57, 58, 
        58, 59, 60, 60, 61, 62, 62, 63, 64, 64, 65, 66, 66, 67, 68, 68, 69, 70, 70, 71, 72, 
        72, 73, 74, 74, 75, 76, 76, 77, 78, 78, 79, 80, 80, 81, 82, 82, 83, 84, 84, 85, 86, 
        86, 87, 88, 88, 89, 90, 90, 91, 92, 92, 93, 94, 94, 95, 96, 96, 97, 98, 98, 99, 100, 
        102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 
        136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 
        170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198
        ]

    A2 = [x for x in range(0, 1000, 7)]
    B2 = [x for x in range(0, 333, 3)]
    C2 = [
        0, 0, 3, 6, 7, 9, 12, 14, 15, 18, 21, 21, 24, 27, 28, 30, 33, 35, 36, 39, 42, 42, 45, 
        48, 49, 51, 54, 56, 57, 60, 63, 63, 66, 69, 70, 72, 75, 77, 78, 81, 84, 84, 87, 90, 91, 
        93, 96, 98, 99, 102, 105, 105, 108, 111, 112, 114, 117, 119, 120, 123, 126, 126, 129, 132, 
        133, 135, 138, 140, 141, 144, 147, 147, 150, 153, 154, 156, 159, 161, 162, 165, 168, 168, 
        171, 174, 175, 177, 180, 182, 183, 186, 189, 189, 192, 195, 196, 198, 201, 203, 204, 207, 
        210, 210, 213, 216, 217, 219, 222, 224, 225, 228, 231, 231, 234, 237, 238, 240, 243, 245, 
        246, 249, 252, 252, 255, 258, 259, 261, 264, 266, 267, 270, 273, 273, 276, 279, 280, 282, 
        285, 287, 288, 291, 294, 294, 297, 300, 301, 303, 306, 308, 309, 312, 315, 315, 318, 321, 
        322, 324, 327, 329, 330, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 
        427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 
        553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 
        679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 
        805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 910, 917, 924, 
        931, 938, 945, 952, 959, 966, 973, 980, 987, 994
        ]

    tests = [
        (A, B, C),
        (A2, B2, C2),
    ]

    def test_sorted_merge(self):
        for A, B, expected in self.tests:
            actual = sorted_merge(A, B)
            assert actual == expected
            assert len(A) + len(B) == len(actual)


if __name__ == "__main__":
    unittest.main()