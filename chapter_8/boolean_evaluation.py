# python3
# boolean_evaluation.py - Takes in a boolean expression and the desired result (True or False). 

def string_to_bool(s: str) -> bool:
    return s == '1'


def boolean_eval(exp: str, result: bool, memo) -> int:
    """
    Takes in a boolean expression and the desired result (True or False), defaults to True.
    Returns the number of parenthesis combinations possible to achieve the desired result.
    """
    if len(exp) == 0:
        return 0
    if len(exp) == 1:
        return 1 if string_to_bool(exp) == result else 0
    
    if exp + str(result) in memo:
        return memo[exp + str(result)]

    ways = 0
    for i in range(1, len(exp), 2):
        left = exp[:i]
        right = exp[i + 1 :]

        left_true = boolean_eval(left, True, memo)
        left_false = boolean_eval(left, False, memo)
        right_true = boolean_eval(right, True, memo)
        right_false = boolean_eval(right, False, memo)

        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if exp[i] == "|":
            total_true = (
                left_true * right_true
                + left_false * right_true
                + left_true * right_false
            )

        elif exp[i] == '&':
            total_true = left_true * right_true
        elif exp[i] == '^':
            total_true = left_true * right_false + left_false * right_true

        subways = total_true if result else (total - total_true)
        ways += subways

    memo[exp + str(result)] = ways
    return ways
        

def evaluate(exp: str, result: bool) -> int:
    memo = {}
    return boolean_eval(exp, result, memo)


def example():
    # Sanity check:
    print(evaluate("0", False))
    print(evaluate("1", True))

    # Test the function
    print(evaluate("1^0|0|1", False))
    print(evaluate("0&0&0&1^1|0", True))

if __name__ == "__main__":
    example()
