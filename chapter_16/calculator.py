# python3
# calculator.py - Given an arithmetic expression (without parentheses) return the result of that expression

import re
from collections import deque
import unittest

def mult_two(x, y):
    """
    Multiplies two numbers.
    """
    return x * y

def divide_two(x, y):
    """
    Divides two numbers.
    """
    return x / y

def add_two(x, y):
    """
    Adds two numbers.
    """
    return x + y

def subtract_two(x, y):
    """
    Subtracts two numbers.
    """
    return x - y

def perform_operation(expression, regex, operation):
    """
    Performs the operation given an arithmetic expression, regex expression, and operation function.
    """
    result = 0
    mo = ''

    mo = re.search(regex, expression)
    if mo != None:
        result = str(operation(float(mo.group(1)), float(mo.group(2))))
        expression = re.sub(regex, result, expression, count=1)

    return expression


def calculator(expression):
    """
    Given an arithmetic expression (without parentheses) return the result of that expression
    """
    operation_queue = deque()

    m_and_d_dict = {
        '*': 'm',
        '/': 'd',
    }
    a_and_s_dict = {
        '+': 'a',
        '-': 's',
    }
    # Add the queues for order of operations
    for char in expression:
        if char in m_and_d_dict:
            operation_queue.append(m_and_d_dict[char])

    for char in expression:
        if char in a_and_s_dict:
            operation_queue.append(a_and_s_dict[char])
        

    # Define the patterns to match
    mult_regex = re.compile(r'(\d*[.]?\d*)\*(\d*[.]?\d*)')
    divide_regex = re.compile(r'(\d*[.]?\d*)\/(\d*[.]?\d*)')
    add_regex = re.compile(r'(\d*[.]?\d*)\+(\d*[.]?\d*)')
    subtract_regex = re.compile(r'(\d*[.]?\d*)\-(\d*[.]?\d*)')

    # Oder of operations dictionaries has the regex as the keys and the function as the values
    order_of_operations = {
        'm': [mult_regex, mult_two],
        'd': [divide_regex, divide_two],
        'a': [add_regex,  add_two],
        's': [subtract_regex, subtract_two],
    }

    while len(operation_queue) != 0:

        # Execute an operation
        op = operation_queue.popleft()

        # Goes through the operations following PEMDAS (parenthesis, exponent, division, addition, and subtraction)
        regex, operation = order_of_operations[op]

        expression = perform_operation(expression, regex, operation)



    return float(expression)


class Test(unittest.TestCase):



    tests = [
        ('2*3+5/6*3+15', 23.5),
        ('2*3+18/6*3+15', 30),
        ('2*3*4/6+1+1-1+1', 6),
        ('3*3/4/5*2', 0.9),
        ('10-4/2*3+4*2', 12),
        ]
    
    def test_calculator(self):
        for expression, expected in self.tests:
            actual = calculator(expression)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
