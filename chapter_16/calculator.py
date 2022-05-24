# python3
# calculator.py - Given an arithmetic expression (without parentheses) return the result of that expression

import re
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
    # When there are no more matches, 
    # that means that the expression has been evaluated
    # for that operation
    #while mo != None:
    mo = re.search(regex, expression)
    if mo != None:
        result = str(operation(float(mo.group(1)), float(mo.group(2))))
        expression = re.sub(regex, result, expression, count=1)
    
    return expression


def calculator(expression):
    """
    Given an arithmetic expression (without parentheses) return the result of that expression
    """
    

    # Define the patterns to match
    multi_regex = re.compile(r'(\d*[.]?\d*)\*(\d*[.]?\d*)')
    divide_regex = re.compile(r'(\d*[.]?\d*)\/(\d*[.]?\d*)')
    add_regex = re.compile(r'(\d*[.]?\d*)\+(\d*[.]?\d*)')
    subtract_regex = re.compile(r'(\d*[.]?\d*)\-(\d*[.]?\d*)')

    # Oder of operations dictionaries has the regex as the keys and the function as the values
    mult_and_divide = {
        multi_regex: mult_two,
        divide_regex: divide_two,
    }
    mult_div = re.compile(r'[*/]')

    add_and_subtract = {
        add_regex: add_two,
        subtract_regex: subtract_two,
    }
    add_sub = re.compile(r'[+-]')

    # Checks to make sure there aren't any unevaluated division or multiplication operators in the expression
    mult_div_check = re.search(mult_div, expression)

    while mult_div_check != None:

        # Goes through the operations following PEMDAS (parenthesis, exponent, division, addition, and subtraction)
        for regex, operation in mult_and_divide.items():

            expression = perform_operation(expression, regex, operation)
            mult_div_check = re.search(mult_div, expression)

    # Checks to make sure there aren't any unevaluated division or multiplication operators in the expression
    add_sub_check = re.search(add_sub, expression)

    while add_sub_check != None:

        # Goes through the operations following PEMDAS (parenthesis, exponent, division, addition, and subtraction)
        for regex, operation in add_and_subtract.items():

            expression = perform_operation(expression, regex, operation)
            add_sub_check = re.search(add_sub, expression)


    return float(expression)


class Test(unittest.TestCase):



    tests = [
        ('2*3+5/6*3+15', 23.5),
        ('2*3+18/6*3+15', 30),
        ('2*3*4/6+1+1-1+1', 6),
        ('3*3/4/5*2', 0.9),
    ]
    
    def test_calculator(self):
        for expression, expected in self.tests:
            actual = calculator(expression)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
