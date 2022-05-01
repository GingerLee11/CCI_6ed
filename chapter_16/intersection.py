# python3
# intersection.py - Finds the intersection of two line segements if there is one. Returns None otherwise.

import unittest

def calc_line_params(line):
    """
    Calculates slope (m) and y-intercept (b) for a given line.
    """
    point_a = line[0]
    point_b = line[1]
    # Calculate slope: m = y1 - y0 / x1 -x0
    m = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])

    # Calculate the y-intercept both ways and check that they are equal:
    # b = y - mx
    b0 = point_a[1] - m * point_a[0]
    b1 = point_b[1] - m * point_b[0]
    if b0 != b1:
        raise Exception("y_intercepts are not equal.")
    return m, b0


def intersection(line_a, line_b):
    """
    Finds the intersection of two line segements if there is one. Returns None otherwise.
    line_a and line_b are both lists withs pairs of tuples containing two points
    Ex: 
    line_a = [(1, 1), (3, 3)]
    line_b = [(3, 1), (1, 3)]
    """
    # Check to make sure the line segments will intersect at all before calculating any values.
    # Check y: line_a[0][1] is line_a, point_a, y
    if (line_a[0][1] > line_b[0][1] and line_a[1][1] > line_b[1][1]) or (line_b[0][1] > line_a[0][1] and line_b[1][1] > line_a[1][1]):
        return None
    # Check x:
    if (line_a[0][0] > line_b[0][0] and line_a[1][0] > line_b[1][0]) or (line_b[0][0] > line_a[0][0] and line_b[1][0] > line_a[1][0]):
        return None

    m0, b0 = calc_line_params(line_a)
    m1, b1 = calc_line_params(line_b)

    # Calc x value for intercept
    x = (b1 - b0) / (m0 - m1)

    # Calc two y values for intercept and check that they are equal 
    y0 = m0 * x + b0
    y1 = m1 * x + b1
    if y0 != y1:
        raise Exception("Intercept points are not equal.")
    else:
        intersect = (x, y0)
        return intersect


class Test(unittest.TestCase):
    line_a_list = [
        [(1, 1), (5, 5)],
        
    ]
    line_b_list = [
        [(1, 5), (5, 1)],
    ]

    expected_list = [
        (3, 3),
        ]

    def test_intersection(self):
        for line_a, line_b, expected in zip(self.line_a_list, self.line_b_list, self.expected_list):
            actual = intersection(line_a, line_b)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()