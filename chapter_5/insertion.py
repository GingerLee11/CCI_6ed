# python3
# insertion.py - Takes in two 32 bit values N and M and inserts M into N at position i to j. 
# Position j must be such that M has enough bits to fit in N.

from collections import deque

def convert_to_decimal(binary_number):
    """
    Takes in a binary number as a string and converts it to decimal number.
    """
    n = 0
    dec_num = 0
    binary_queue = deque(str(binary_number))
    while len(binary_queue) != 0:
        bit = binary_queue.pop()
        dec_num += 2 ** n * int(bit)
        n += 1
    return dec_num


def convert_to_binary(num):
    """
    Takes in a decimal number and converts it to binary.
    """
    if num==0: 
        return ''
    else:
        return convert_to_binary(num // 2) + str(num % 2)
    



def insertion(N, M, i, j):
    """
    Takes in two 32 bit values N and M and inserts M into N at position i to j. 
    Position j must be such that M has enough bits to fit in N.
    """

    if len(str(M)) > j + 1 - i:
        return False

    M = convert_to_decimal(M)
    N = convert_to_decimal(N)

    M <<= i
    N = N | M

    N = convert_to_binary(N)

    return print(N)


insertion(10000000000, 10011, 2, 6)