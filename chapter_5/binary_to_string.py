# python3
# binary_to_string.py - Converts a number from 1 to 0 into a binary representation of that number as if it were an integer.
# Ex: 0.72 => 72 => 1001000

from insertion import convert_to_binary

from random import random


def binary_to_string(num):
    """
    Converts a number from 1 to 0 into a binary representation of that number as if it were an integer.
    Ex: 0.72 => 72 => 1001000
    """
    exp = len(str(num)) - 2
    num = int(num * 10 ** exp) 

    binary_num = convert_to_binary(num)

    if len(binary_num) > 32:
        return print("ERROR; binary representation is greater than 32 characters.")
    else:
        return print(binary_num)


def example():

   for x in range(10):
       num = round(random(), 10)
       print(num)
       print(binary_to_string(num))

if __name__ == "__main__":
    example()