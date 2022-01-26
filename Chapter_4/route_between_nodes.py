# python3
# route_between_nodes.py - Given a directed graph the function finds if there is a route between the two nodes.

import unittest


def route_search(graph, start, end, checked=None):
    """
    Recursive function that searches through the graph for a route between the two given nodes.
    """
    if checked is None:
        checked = set()
    
    for node in graph[start]:
        if node not in checked:
            checked.add(node)
            if node == end or route_search(graph, node, end, checked):
                return True
    return False


class Test(unittest.TestCase):
    undirected_graph_dict = {
        0: [1, 2, 3, 4, 5, 17], 
        1: [2], 
        2: [6, 8], 
        3: [8], 
        4: [0],
        5: [10, 18, 19], 
        6: [1, 7], 
        7: [6],
        8: [9], 
        9: [8],
        10: [5, 19],
        11: [12, 13], 
        12: [14], 
        13: [15, 16], 
        14: [13], 
        15: [13],
        16: [13],
        17: [0], 
        18: [19],
        19: [10],
    }

    tests = [
        (0, 9, True),
        (0, 4, True),
        (0, 5, True),
        (0, 11, False),
        (4, 19, True),
        (11, 13, True),
        (17, 0, True),
        (17, 9, True),
        (7, 16, False),
        (16, 17, False),
    ]

    def test_route_search(self):
        for [start, end, expected] in self.tests:
            actual = route_search(self.undirected_graph_dict, start, end)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()