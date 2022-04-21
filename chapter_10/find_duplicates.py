# python3
# find_duplicates.py - Find duplicates in an array that may range anywhere from 0 to 32000.

from random import randint, shuffle

def find_duplicates(array):
    """
    Find duplicates in an array that may range anywhere from 0 to 32000.
    """
    array = sorted(array)

    last = None
    for curr in array: 
        if curr == last:
            print(curr)
        last = curr


def example():

    upper_bound = randint(1, 32000)
    test_array = [x for x in range(1, upper_bound)]
    
    for x in range(20):
        num = randint(1, upper_bound)
        test_array.append(num)
    
    shuffle(test_array)

    find_duplicates(test_array)


if __name__ == "__main__":
    example()