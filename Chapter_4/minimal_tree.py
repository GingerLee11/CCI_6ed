# python3
# minimal_tree.py - Takes a sorted set-like list, and creates a binary search tree with minimal height

import unittest

def create_minimal_tree(sorted_set):
    """
    Takes a sorted set-like list, and creates a binary search tree with minimal height
    """
    if len(sorted_set) == 0:
        return []

    # Set the zero index (root of the tree) to the middle of the sorted set
    n = round(len(sorted_set) / 2) - 1
    minimal_tree = []

    # Need to check if the list has an odd or even number of integer elements
    # If even there will be one element left over and will need to be appended
    odd_or_even = len(sorted_set) % 2

    # Go through the sorted set and append one number lower and higher than the midpoint
    # Until half the length has been iterated through (appened two numbers per iteration)
    for i in range(0, n + 1):
        if i == 0:
            minimal_tree.append(sorted_set[n])
        else:
            minimal_tree.append(sorted_set[n-i])
            minimal_tree.append(sorted_set[n+i])

    # If the sorted set is even then there will be one number remaining
    # Which will be appended onto the end
    if odd_or_even == 0:
        minimal_tree.append(sorted_set[len(sorted_set) -1])

    return minimal_tree


class Test(unittest.TestCase):

    sorted_lists = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [],
        
    ]
    tests = [
        [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15],
        [7, 6, 8, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 14],
        [],
    ]

    def test_create_minimal_tree(self):
        for expected, sorted_list in zip(self.tests, self.sorted_lists):
            actual = create_minimal_tree(sorted_list)
            print(f"Actual:  {actual}\nExpected:{expected}\n")
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
