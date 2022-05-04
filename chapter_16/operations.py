# python3
# operations.py - Implementing methods for multiplication, division, and subtraction using the add operation.

def multiplication(x, y):
    """
    x * y
    """
    total = 0
    if y > 0:
        for i in range(y):
            total += x
    elif x < 0:
        for i in range(0, x, -1):
            total += abs(y)
    else:
        for i in range(x):
            total += y

    return total

def division(x, y):
    """
    Integer division; returns the nearest integer value.
    y / x
    """
    total = 0
    i = 0
    if y > 0 and x > 0:
        while total < y:
            if (total + x) <= y:
                total += x
                i += 1
            else:
                return i
    elif x > 0:
        while total > y:
            if (y + x) <= total:
                y += x
                i += (-1)
            else:
                return i
    elif y > 0:
        while total < y:
            if (y + x) >= total:
                y += x
                i += (-1)
            else:
                return i

    else: 
        while total > y:
            if (total + x) >= y:
                total += x
                i += 1
            else:
                return i
    return i

def subtraction(x, y):
    """
    x - y
    """
    return x + (-y)


def example():

    print(multiplication(-4, -5))
    print(multiplication(-4, 5))
    print(multiplication(4, -5))
    print(multiplication(4, 5))
    print(division(2, 11))
    print(division(2, -11))
    print(division(-2, -11))
    print(division(-2, 11))
    print(subtraction(5, 2))


if __name__ == "__main__":
    example()
