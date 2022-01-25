# python3
# route_between_nodes.py - Given a directed graph the function finds if there is a route between the two nodes.

def route_search(graph_dict, checked_list, start, end):
    """
    Helper recursive function that searches through the graph for a route between the two given nodes.
    """
    # if start not in graph_dict:
    #   return False
    
    if start == end:
        return True

    else:
        for i, node in enumerate(graph_dict[start]):
            if node == end:
                return True
            elif node in checked_list:
                continue
            elif i == len(graph_dict[start]) - 1:
                checked_list.append(start)
                start = node
                return route_search(graph_dict, checked_list, start, end)
            else:
                start = node
                return route_search(graph_dict, checked_list, start, end)

def route_between_nodes(graph_dict, starting_node, end_node):
    if starting_node not in graph_dict:
        return print("Inital value is not contained within the given graph.")
    elif starting_node == end_node: 
        return print("Initial and end node are the same. Enter different values to find a route.")

    else:
        checked = []
        route = route_search(graph_dict, checked, starting_node, end_node)
        return route

directed_graph_dict = {
    0: [1], 
    1: [2], 
    2: [0, 3], 
    3: [4], 
    4: [2, 5], 
    6: [7, 9], 
    7: [8], 
}

directed_graph_dict = {
    0: [1, 2, 3, 4, 5], 
    1: [2], 
    2: [6, 8], 
    3: [8], 
    5: [10, 18, 19], 
    6: [1, 7], 
    8: [9], 
    11: [12, 13], 
    12: [14], 
    13: [15, 16], 
    14: [13], 
    17: [0], 
}
'''
print(route_between_nodes(directed_graph_dict, 0, 9)) # True
print(route_between_nodes(directed_graph_dict, 0, 4)) # True
print(route_between_nodes(directed_graph_dict, 0, 5)) # True
print(route_between_nodes(directed_graph_dict, 0, 11)) # False
print(route_between_nodes(directed_graph_dict, 4, 19)) # False
print(route_between_nodes(directed_graph_dict, 11, 13)) # True
print(route_between_nodes(directed_graph_dict, 17, 0)) # True
print(route_between_nodes(directed_graph_dict, 17, 9)) # True
print(route_between_nodes(directed_graph_dict, 7, 9)) # "Initial value not in graph"
print(route_between_nodes(directed_graph_dict, 0, 0)) # "Initial value is same as final value"
'''