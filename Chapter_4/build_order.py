# python3
# build_order.py - Takes in a list of projects and a list of the dependencies with the project and it's dependent project.
# Returns the order in which the projects must be completed based on the dependecies.

import unittest

from collections import deque


class ProjectNode:
    def __init__(self, project):
        self.project = project
        self.dependencies = []


def build_order(projects, dependecies):
    """
    Takes in a list of projects and a list of the dependencies with the project and it's dependent project.
    Returns the order in which the projects must be completed based on the dependecies.
    """

    build_queue = deque()

    for project in projects:
        node = ProjectNode(project)
        # Go through each dependency and append it to the dependencies list of the necessary project
        for dependency in dependecies:
            if dependency[1] == node.project:
                node.dependencies.append(dependency[0])

        build_queue.append(node)
    
    project_build_order = []
    
    # Append projects with no dependencies, 
    # if there are no projects with no dependencies, 
    # then there is no valid build order; return error.

    # i is used here since the index reduces by one when an element is removed from the build queue
    i = 0
    for k in range(len(projects)):
        project = build_queue[i]
        if project.dependencies == []:
            build_queue.remove(project)
            project_build_order.append(project.project)
        else:
            i += 1

    if project_build_order == []:
        return print("Error. Invalid build order. Circular dependencies.")

    # This isn't an elegant solution, but this might help in cases where there are 
    # Circular dependencies that aren't caught initially
    loop_counter = 0

    # Go through all the projects in order of dependencies
    while len(build_queue) != 0:
        project = build_queue.popleft()

        # Go through all the projects and only append projects after their dependents
        dependent_list = []
        for dependency in project.dependencies:
            if dependency not in project_build_order:
                if project not in build_queue:
                    build_queue.append(project)
            else:
                dependent_list.append(dependency)

        # Make sure that all the dependencies are met and not just the first one        
        if len(dependent_list) == len(project.dependencies):
            if project.project not in project_build_order:
                project_build_order.append(project.project)

        loop_counter += 1
        if loop_counter == len(projects) * 2:
            print("Error. Invalid build order. Circular dependencies.")
            return None
    
    return project_build_order


class Test(unittest.TestCase):

    projects_list = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i'],
        ['a', 'b', 'c', 'd', 'e', 'f',],
        ['a', 'b', 'c', 'd',],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i'],
    ]
    dependencies_list = [
        [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')],
        [('e', 'f'), ('e', 'c'), ('e', 'b'), ('g', 'b'), ('i', 'f'), ('f', 'd'), ('c', 'd'), ('b', 'd'), ('d', 'a')],
        [('c', 'a'), ('a', 'b'), ('b', 'd'), ('d', 'f'), ('f', 'e'), ('e', 'c')],
        [('a', 'b'), ('b', 'c'), ('c', 'a')],
        [],
        [('e', 'f'), ('e', 'c'), ('e', 'b'), ('g', 'b'), ('i', 'f'), ('f', 'd'), ('c', 'd'), ('b', 'd'), ('d', 'a'), ('b', 'a')],
    ]
    outputs = [
        ['e', 'f', 'a', 'b', 'd', 'c'],
        ['e', 'g', 'i', 'b', 'c', 'f', 'd', 'a'],
        None,
        None,
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i'],
        ['e', 'g', 'i', 'b', 'c', 'f', 'd', 'a'],
    ]

    def test_build_order(self):
        for expected, projects, dependencies in zip(self.outputs, self.projects_list, self.dependencies_list):
            actual = build_order(projects, dependencies)
            print(f"Actual:   {actual}\nExpected: {expected}")
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
