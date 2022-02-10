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


    # Go through all the projects in order of dependencies
    while len(build_queue) != 0:
        project = build_queue.popleft()

        # Go trough all the projects and only append projects after their dependents
        for dependency in project.dependencies:
            if dependency not in project_build_order:
                if project not in build_queue:
                    build_queue.append(project)
            elif project.project not in project_build_order:
                project_build_order.append(project.project)

    return project_build_order


class Test(unittest.TestCase):

    projects = ['a', 'b', 'c', 'd', 'e', 'f']

    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    output = ['e', 'f', 'a', 'b', 'd', 'c']


    def test_build_order(self):
        expected = self.output
        actual = build_order(self.projects, self.dependencies)
        print(f"Actual:   {actual}\nExpected: {expected}")
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
