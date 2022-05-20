# python3
# pairs_with_sums.py - Finds pairs of integers in an array of integer that given_sum to a given given_sum.

from random import randint
import time

def find_int_pairs(section, given_sum, test=False):
    """
    Helper function that does the iterating to find the pairs.
    Added this as a brute force method to compare relative performance.
    """
    int_pairs = set()

    if test == True:
        section = sorted(section)

    for indx1, num1 in enumerate(section):
        for indx2, num2 in enumerate(section):
            if indx1 == indx2:
                continue
            if num1 + num2 == given_sum:
                if (num2, num1) not in int_pairs:
                    int_pairs.add((num1, num2))
            elif num1 + num2 > given_sum:
                break

    return int_pairs



def pairs_with_given_sums(array, given_sum):
    """
    Finds pairs of integers in an array of integer that given_sum to a given given_sum.
    """
    array = sorted(array)

    mid_indx = round(len(array) / 2)
    mid = array[mid_indx]
    first = array[0]
    last = array[-1]
    
    # Check how the value compares with the integers
    if last * 2 < given_sum:
        return None
    elif first * 2 > given_sum:
        return None

    # When the integer pairs are all on the left half of the array
    elif mid > given_sum:
        left_half = array[:mid_indx]

        # If the given sum is very low, 
        # this will divide the array in half until the
        # half point is smaller than the given sum.
        while mid > given_sum:
            mid_indx = round(len(left_half) / 2)
            mid = left_half[mid_indx]
            if mid > given_sum:
                left_half = left_half[: mid_indx]

        # If the given sum is less than the first 
        array_mid_indx = len(left_half) - 1
        array_mid = left_half[array_mid_indx]
        diff_1 = array_mid - given_sum
        diff_2 = given_sum - mid
        if diff_1 > diff_2:   
            while mid < given_sum:
                mid_indx += 1
                mid = left_half[mid_indx]
            left_half = array[: mid_indx + 1]
        else:
            while array_mid > given_sum:
                array_mid_indx -= 1
                array_mid = left_half[array_mid_indx]
            left_half = left_half[: array_mid_indx + 1]
        
        # Finds the integer pairs for the given section 
        int_pairs = find_int_pairs(left_half, given_sum)

    # If the given_sum is less than the last element in the array, 
    # this will lead to the most possible combinations
    elif last > given_sum:
        last_indx = len(array) - 1
        while mid > given_sum:
            last_indx -= 1
            last = array[last_indx]
        left_half = array[: last_indx + 1]
        
        # Finds the integer pairs for the given section 
        int_pairs = find_int_pairs(left_half, given_sum)

    # When the integer pairs for the given_sum is somewhere near the middle
    elif mid * 2 > given_sum and last < given_sum:

        i = 0
        while first + mid < given_sum:
            i += 1
            first = array[i]
        middle = array[i - 1 : mid_indx + 1]

        # Finds the integer pairs for the given section 
        int_pairs = find_int_pairs(middle, given_sum)
        
    # When the integer pairs are mostly in the right half of the array 
    elif mid * 2 <= given_sum:

        i = 0
        while first + last < given_sum:
            i += 1
            first = array[i]
        right_half = array[i - 1:]

        # Finds the integer pairs for the given section    
        int_pairs = find_int_pairs(right_half, given_sum)

    # if int_pairs is an empty set return None:
    if int_pairs != set():
        return int_pairs
    else:
        return None



def example():
    total_differences = []
    # Run both functions 10 times to compare performance
    for i in range(10):
        rand_array = []
        for i in range(0, 1000):

            x  = randint(1, 100000)
            rand_array.append(x)

        given_sum = randint(0, 200000)
        print(given_sum)

        # Timing both function to see how my function compares to brute force method
        start = time.perf_counter()
        pairs_1 = pairs_with_given_sums(rand_array, given_sum)
        end = time.perf_counter()
        difference_1 = end - start

        start = time.perf_counter()
        pairs_2 = find_int_pairs(rand_array, given_sum, True)
        end = time.perf_counter()
        difference_2 = end - start
        
        # if pairs_2 != None and pairs_1 != None:
            # print(pairs_2 - pairs_1)
        differences = (difference_1, difference_2)
        total_differences.append(differences)

    function_1_avg_time = sum([diff[0] for diff in total_differences]) / len(total_differences)
    function_2_avg_time = sum([diff[1] for diff in total_differences]) / len(total_differences)
    print(f"Function 1 took on avg: {function_1_avg_time} seconds, Function 2 took: {function_2_avg_time} seconds,")
    
if __name__ == "__main__":
    example()
