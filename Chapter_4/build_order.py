# python3
# build_order.py - Takes in a list of projects and a list of the dependencies with the project and it's dependent project.
# Returns the order in which the projects must be completed based on the dependecies.

import unittest


class ProjectNode:
    def __init__(self, project):
        self.project = project
        self.dependencies = []


def build_order(projects, dependecies):
    """
    Takes in a list of projects and a list of the dependencies with the project and it's dependent project.
    Returns the order in which the projects must be completed based on the dependecies.
    """

    build_path = []

    for project in projects:
        node = ProjectNode(project)
        # Go through each dependency and append it to the dependencies list of the necessary project
        for dependency in dependecies:
            if dependency[1] == node.project:
                node.dependencies.append(dependency[0])

        build_path.append(node)
    
    # This is the final build order that will be returned. 
    # Set data structure is used to avoid repetiton
    # (Might be changed depending on the nature of the implementation)
    project_build_order = set()
    for project in build_path:
        if project.dependencies == []:
            build_path.remove(project)
            project_build_order.add(project.project)

    # If no items are added that means that all projects have dependencies, which we lead to circular dependecies
    # This doesn't catch all of the adge cases, but it should help
    if project_build_order == []:
        return print("Error. Invalid build order. Circular dependencies.")

    # Add the rest of the projects in order based on dependencies
    while len(project_build_order) < len(projects):
        for project in build_path:
            if project.dependencies == []:
                    project_build_order.add(project.project)
            for dependency in project.dependencies:
                
                if dependency not in project_build_order:
                    pass
                else:
                    project_build_order.add(project.project)
    
    return project_build_order


class Test(unittest.TestCase):

    projects = ['a', 'b', 'c', 'd', 'e', 'f']

    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    output = {'e', 'f', 'a', 'b', 'd', 'c'}


    def test_build_order(self):
        expected = self.output
        actual = build_order(self.projects, self.dependencies)
        print(f"Actual:   {actual}\nExpected: {expected}")
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
