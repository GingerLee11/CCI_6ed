# python3
# boolean_evaluation.py - Takes in a boolean expression and the desired result (True or False). 

from distutils.util import strtobool


def boolean_eval(boolean_exp, result=True, start='', remainder='', x=0, y=0, total_combos=0):
    """
    Takes in a boolean expression and the desired result (True or False), defaults to True.
    Returns the number of parenthesis combinations possible to achieve the desired result.
    """

    # If x is zero then this slice will only return one character so the whole string is removed.
    if x == 0:
        test_exp = start + boolean_exp[y:] + remainder
    else:
        test_exp = test_exp = start + boolean_exp[y:x] + remainder
    test_exp = bool(strtobool(test_exp))

    # Base Case
    if test_exp == result: 
        total_combos += 1

    remainder = boolean_exp[x:]
    x -= 2
    remainder = boolean_exp[x:]
    
    if len(start) + len(remainder) >= len(boolean_exp) - 3:
        start = boolean_exp[:y]
        y += 2
        start = boolean_exp[:y]
        x = 0
        remainder = ''
    if '(' not in start:
        start += '('

    return boolean_eval(boolean_exp, result, start, ')' + remainder, x, y, total_combos)


def example():
    # Sanity check:
    print(boolean_eval("0", False))
    print(boolean_eval("1", True))

    # Test the function
    print(boolean_eval("1^0|0|1", False))
    print(boolean_eval("0&0&0&1^1|0", True))

if __name__ == "__main__":
    example()